from .models import VisaType
from .forms import VisaTypeForm
from django.views.generic import  ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import ModelFormMixin
from django.core.paginator import PageNotAnInteger, EmptyPage
from .filters import VisaTypeFileter
from django.views import View
from django.shortcuts import redirect, get_object_or_404, render
from django.http import Http404
from app.models import Employe, VisaRenewal, SaudiKapilDetail
from datetime import date, timedelta


class VisaCreateView(ModelFormMixin, ListView):
    
    model  = VisaType
    template_name = "core/visa_type.html"
    form_class = VisaTypeForm
    success_url = reverse_lazy("core:visa-type-create")
    paginate_by = 5
    paginate_orphans = 3
    context_object_name = "visatypes"
    
    
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.object = None
    
    
    def get_context_data(self, **kwargs) :
        context =  super(VisaCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context 
    
    
    def post(self, request):
        
        form = self.get_form()
        
        if form.is_valid(): 
            response = self.form_valid(form=form)
            messages.success(self.request, "Your record has been successfully created")
            return response
        
        
        response = self.form_invalid(form=form)
        messages.error(self.request, "An error occurred while processing your request. Please try again.")
        return response


    
    def paginate_queryset(self, queryset, page_size: int):
        
        paginator = self.get_paginator(queryset, page_size)
        page = self.request.GET.get('page')
        
        try:
            page_obj = paginator.page(page)
            
        except PageNotAnInteger:
            
            page_obj = paginator.page(1)
        except EmptyPage:
            
            page_obj = paginator.page(paginator.num_pages)
        
        
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())
    
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        filter_query = VisaTypeFileter(self.request.GET, queryset=queryset)
        return filter_query.qs


class VisaUpdateView(View):
    
    def post(self, request, id):
        try:
            visa = get_object_or_404(VisaType, pk=id)
            form = VisaTypeForm(request.POST, instance=visa)

        
            if form.is_valid():
                
                form.save()
                messages.success(request, "Your record has been updated successfully!")
                
            else:
                messages.error(request, "Something went wrong. Please try again.")
            
            return redirect(reverse_lazy("core:visa-type-create"))
        
        except Http404:
            
            messages.error(request, "something went wrong.")
            return redirect("core:visa-type-create")


class VisaTypeDelete(View):
    
    
    def post(self, request, id):
        
        try:
            
            visa = VisaType.del_items.get(id=id)
        
            visa.delete()
            messages.success(request, "Your record has been successfully deleted")
        
        except Exception as e:
            
            messages.error(request, f"something went wrong. {e}")
        
        url = reverse_lazy("core:recycle-bin")
        
        if request.GET.get("redirect_page", "") == "recycle_bin":
            url = reverse_lazy("core:recycle-bin") + "?tab=visas"
            
        return redirect(url)


def visa_type_deactivate(request, id):
    
    try:
        visa = get_object_or_404(VisaType, id=id)
        visa.active = False
        visa.save()
        messages.success(request, "Your record has been successfully deleted. You can restore it from the Recycle Bin.")
    
    except Http404:
        
        messages.success(request, "Something went wrong, or the ID is invalid. Please try again.")
    
    
    return redirect("core:visa-type-create")


def visa_type_activate(request, id):
    
    try:
        visa = VisaType.del_items.get(id=id)
        visa.active = True
        visa.save()
        messages.success(request, "Your record has been successfully restored.")
    
  
    except Exception as e:    
        messages.error(request, f"Something went wrong, or the ID is invalid. Please try again. {e}")
    
    url = reverse_lazy("core:recycle-bin") + "?tab=visas"
    return redirect(url)
    



class DashboardView(View):
    
    
    def get(self, request):
    
        visas_expire_in_month = Employe.objects.filter(expiry_date__lte=date.today()+timedelta(days=30), expiry_date__gte=date.today()).order_by("expiry_date")
        visas_expire_in_week = Employe.objects.filter(expiry_date__lte=date.today()+timedelta(weeks=1), expiry_date__gte=date.today()).order_by("expiry_date")
        total_visas = VisaRenewal.objects.all().count() + Employe.objects.all().count()
        
        total_expire_visas = Employe.objects.filter(
            expiry_date__lte=date.today()
        ).count()
        
        
        context = {
            'count_emp':Employe.objects.all().count(),
            'count_employer':SaudiKapilDetail.objects.all().count(),
            'visas_expire_in_month':visas_expire_in_month,
            'visas_expire_in_week':visas_expire_in_week,
            
            "chart_data":{
                "total_visas":total_visas,
                "total_expire_visas":total_expire_visas,
                "visas_expire_in_month":visas_expire_in_month.count(),
                "visas_expire_in_week":visas_expire_in_week.count(),
            }
        }
        
        
        
        return render(request, template_name="core/dashboard.html", context=context)



class RecycleBinView(View):
    
    def get(self, request):
        
        
        context = {
            'employees':Employe.del_items.all(),
            'employers': SaudiKapilDetail.del_items.all(),
            'visas': VisaType.del_items.all()
        }
        return render(request, "core/recycle_bin.html",  context)