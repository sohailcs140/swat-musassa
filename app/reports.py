from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.shortcuts import render
from .models import Employe
from datetime import date, timedelta
from django.conf import settings



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




# Employee Report

class ReportView(View):
    
    
    def get(self, request):
        
        employees = None
        
        if request.GET.get("expire"):
            
            employees = Employe.objects.filter(expiry_date__lte=date.today()).order_by("-expiry_date")
            context = {"employees": employees, "report_for":"List of Expired Visas", 'title':"visas report"}
            
        elif request.GET.get("range") and request.GET.get("s") and request.GET.get("e"):
            
            employees = Employe.objects.filter(expiry_date__range=(request.GET.get("s"),
                                                                   request.GET.get("e")))
            context = {"employees": employees, 
                       'title':"visas report",
                       "report_for":"Visas Expiring or Expired in the Given Date Range",
                       'range':{'s': request.GET.get("s"), 'e': request.GET.get("e") }
                       }
            
        elif request.GET.get("month"):
            
            employees = Employe.objects.filter(expiry_date__lte=date.today() + timedelta(days=30),
                                               expiry_date__gte=date.today()
                                               ).order_by("expiry_date")
            context = {"employees": employees, 
                       'title':"visas report","report_for":"Visas Scheduled to Expire in next 30 days.",
                       }
        
        if employees is not None:
            
            return render_to_pdf("core/reports/visas_list.html", context)
        
        
        return render(request, "core/reports.html")

    
    
    



def get_employee_report(reqeust, id):
    
    employee = None
    try:
       employee = Employe.objects.get(id=id)
    except Exception as e:
        pass
    
    context = {'employee':employee, 'media_root':settings.MEDIA_ROOT}
    
    return render_to_pdf("core/reports/employe_report.html",context)