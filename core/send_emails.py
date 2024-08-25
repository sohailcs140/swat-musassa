from app.models import Employe, TrackEmail
from threading import Thread
from django.views import View
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import OuterRef, Subquery, Q, F
from datetime import timedelta, date
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib import messages


@method_decorator(csrf_exempt, name='dispatch')
class SendEmailsView(View):
    
    error_list = list()
    thread_list = list()
    
    def send_email(self, options:dict, employee:Employe):
        
        try:
            
            send_mail(**options)
            
            TrackEmail.objects.create(employe=employee, issue_date=employee.issue_date, expiry_date=employee.expiry_date)
            
        except Exception as e:
            
            SendEmailsView.error_list.append({options['recipient_list'][0]: e})
    
    
    def post(self, request):
        
        track_emails = TrackEmail.objects.filter(
            employe=OuterRef("pk"), 
            issue_date=F("employe__issue_date"),expiry_date=F("employe__expiry_date")
                                                 ).values_list("employe__id",flat=True)
        
        employees = Employe.objects.filter(Q(expiry_date__lte=date.today()+timedelta(days=30)) and ~Q(email = None)).exclude(id__in=Subquery(track_emails))
        
        
        for employee in employees:
            
            subject = "Visa Expiration alert"
            recipient_list = [employee.email.strip()]
            fail_silently = False
            html_message = render_to_string("core/email.html", context={'employee': employee})
            
            options = {'subject': subject, 'recipient_list': recipient_list,
                       'html_message':html_message,'message':"", 'fail_silently': fail_silently,
                       'from_email':settings.DEFAULT_FROM_EMAIL
                       }
            
            new_thread = Thread(target=self.send_email, args=(options, employee))
            
            SendEmailsView.thread_list.append(new_thread)
            
            new_thread.start()
        
        
        for thread in SendEmailsView.thread_list:
            thread.join()
        
        
        context = {
            "emails": TrackEmail.objects.filter(created_at__date=date.today()).order_by("-created_at")
            ,"employees": Employe.objects.filter(expiry_date=date.today())
        }
        
        
        
        return HttpResponse(render_to_string("includes/partials/notifications.html", context))
    
    



class SendEmailView(View):
    
    
    def get(self, reqeust, id):
        
        
        try:
            
            employe = Employe.objects.get(id=id)
            
            if not employe.email:
                
                raise Exception("Employee has no email.")
            
            
            send_mail(subject="Visa Expiration",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    html_message=render_to_string("core/email.html", context={'employee': employe}),
                    recipient_list=[employe.email.strip()],
                    fail_silently=False,
                    message=""
                    )
            
            
            messages.success(reqeust, "email send successfully")
            
            
        except Exception as e:
            
            messages.error(reqeust, "{e}".format(e=e))
        
        
        
        context = {
        "emails": TrackEmail.objects.filter(created_at__date=date.today()).order_by("-created_at"),
        }
        
        return render(reqeust, "includes/partials/notifications.html", context)