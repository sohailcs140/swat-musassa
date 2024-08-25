from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, get_object_or_404, render, HttpResponseRedirect
from django.http import Http404
from .models import SaudiKapilDetail, Employe, VisaRenewal
from .forms import SaudiKapilForm, EmployeForm, VisaRenewalForm
from .filters import SaudiKapilFilter, EmployeFilter, VisaRenewalFilter
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from core.models import VisaType
from django.conf import settings


"""
EMPLOYER (Saudi Kapil) VIEWS START
"""
class SaudiKapilCreateListView(ModelFormMixin, ListView):
    
    model = SaudiKapilDetail
    form_class = SaudiKapilForm
    paginate_by = 10
    paginate_orphans = 3
    success_url = reverse_lazy("app:saudi-kapil-create-list")
    template_name = "app/employer/kapil_details.html"
    context_object_name = "kapils"


    def post(self, *args, **kwargs):
    
        if self.get_form().is_valid(): 
            resp = self.form_valid(form=self.get_form())
            messages.success(self.request, "Your record has been successfully created")
            return resp
        
        resp = self.form_invalid(form=self.get_form())
        
        messages.error(self.request, "Please fix this errors. {errors}".format(errors=self.get_form().errors))
        return resp
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.object = None
        self.object_list = []
    
    
    def paginate_queryset(self, queryset, page_size:int):
        
        paginator = self.get_paginator(queryset,page_size)
        page = self.request.GET.get("page")
        
        try:
            
            page_obj = paginator.page(page)

        except PageNotAnInteger:
        
            page_obj = paginator.page(1)
            
        except EmptyPage:
            
            page_obj = paginator.page(paginator.num_pages)
        
        
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())
    
    
    def get_queryset(self) :
        query =  super(SaudiKapilCreateListView, self).get_queryset()
        filter_query = SaudiKapilFilter(self.request.GET,queryset=query)        
        return filter_query.qs
       
    
class SauidiKapilUpdateView(View):
         
    def post(self, request, id):
        
        try:
            saudi_kapil = get_object_or_404(SaudiKapilDetail, id=id)
            form = SaudiKapilForm(request.POST,files=request.FILES, instance=saudi_kapil)

            if form.is_valid():
    
                form.save()
            
                messages.success(request, "Your record has been updated successfully!")
                
            else:
                messages.error(request, f"Something went wrong. Please try again.{form.errors}")
            
            
            return redirect(reverse_lazy("app:saudi-kapil-create-list")+f"?iqama_number={saudi_kapil.cnic}")
        
        except Http404:
            
            messages.error(request, f"something went wrong.{form.errors}")
            return redirect("app:saudi-kapil-create-list")  
            
                    
class SauidiKapilDeleteView(View):
    
    def post(self, request, id):
    
        try:
            
            saudi_kapil = SaudiKapilDetail.del_items.get(id=id)
        
            saudi_kapil.delete()
            messages.success(request, "Your record has been successfully deleted")
        
        except Exception  as e:
            
            messages.error(request, f"something went wrong. f{e}")
        
        url = reverse_lazy("app:saudi-kapil-create-list")
        
        if request.GET.get("redirect_page", "") == "recycle_bin":
            url =  reverse_lazy("core:recycle-bin") + "?tab=employers"
        
        return redirect(url)
        

class EmployerDetailView(View):
    
    def get(self, request, id):
        
        try:
            employer = SaudiKapilDetail.all_objects.get(id=id)
            
            
            context ={"employer": employer}
            
            return render(request, "app/employer/employer.html", context=context)
            
            
        except Exception as e:
            
            messages.error(request, f"{e}")
            return redirect(request.path)



def employer_deactivate(request, id):
    
    try:
        kapil = SaudiKapilDetail.objects.get(pk=id)
        kapil.active = False
        kapil.save()
        messages.success(request, "Your record has been successfully deleted. You can restore it from the Recycle Bin.")
    
    except Http404:
        
        messages.success(request, "Something went wrong, or the ID is invalid. Please try again.")

    return redirect("app:saudi-kapil-create-list")



def employer_activate(request, id):
    
    try:
        kapil = SaudiKapilDetail.del_items.get(pk=id)
        kapil.active = True
        kapil.save()
        messages.success(request, "Your record has been successfully restored.")

        
        
    except Exception as e:    
        messages.error(request, f"Something went wrong, or the ID is invalid. Please try again. {e}")
    
    url = reverse_lazy("core:recycle-bin")+"?tab=employers"
    return redirect(url)



"""
EMPLOYE VIEWS START
"""
class EmployeCreateListView(ModelFormMixin, ListView):
    
    model = Employe
    form_class = EmployeForm
    paginate_by = 10
    paginate_orphans = 3
    success_url = reverse_lazy("app:employe-create-list")
    template_name = "app/employee/employees.html"
    context_object_name = "employees"


    def post(self, *args, **kwargs):
    
        if self.get_form().is_valid(): 
            resp = self.form_valid(form=self.get_form())
            messages.success(self.request, "Your record has been successfully created")
            return resp
        
        resp = self.form_invalid(form=self.get_form())
        
        messages.error(self.request, "An error occurred while processing your request. Please try again.")
        return resp
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.object = None
        self.object_list = []
    
    
    def paginate_queryset(self, queryset, page_size:int):
        
        paginator = self.get_paginator(queryset,page_size)
        page = self.request.GET.get("page")
        
        try:
            
            page_obj = paginator.page(page)

        except PageNotAnInteger:
        
            page_obj = paginator.page(1)
            
        except EmptyPage:
            
            page_obj = paginator.page(paginator.num_pages)
        
        
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())
    
    
    def get_queryset(self) :
        query =  super(EmployeCreateListView, self).get_queryset()
        filter_query = EmployeFilter(self.request.GET,queryset=query)        
        return filter_query.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employers'] = SaudiKapilDetail.objects.all()
        context['visa_types'] = VisaType.objects.all()
        context['countries'] = settings.COUNTRIES_WITH_FLAGS
        return context


class EmployeUpdateView(View):
         
    def post(self, request, id):
        
        try:
            employe = get_object_or_404(Employe, id=id)
            form = EmployeForm(request.POST,files=request.FILES, instance=employe)

            if form.is_valid():
    
                form.save()
            
                messages.success(request, "Your record has been updated successfully!")
                
            else:
                messages.error(request, f"Something went wrong. Please try again. {form.errors}")
            return redirect(reverse_lazy("app:employe-create-list")+f"?iqama_number={employe.cnic}")        
        except Exception as e:
            messages.error(request, f"something went wrong. {e}")
            return redirect("app:employe-create-list")  


class EmployeDetailView(View):
    
    def get(self, request, id):
        
        try:
            emp =Employe.all_objects.get(id=id)
            
            
            return render(request, "app/employee/employee.html", context={"employee": emp})
            
            
        except Http404:
            
            messages.error(request, "invalid id")
            return redirect(request.path)
        
        
        
def employee_deactivate(request, id):
    
    try:
        employe = get_object_or_404(Employe, id=id)
        employe.active = False
        employe.save()
        messages.success(request, "Your record has been successfully deleted. You can restore it from the Recycle Bin.")
    
    except Exception as e:
        
        messages.error(request, f"Something went wrong, or the ID is invalid. Please try again. {e}")
    
    
    return redirect("app:employe-create-list")



def employee_activate(request, id):
    
    try:
        employe = Employe.del_items.get(id=id)
        employe.active = True
        employe.save()
        messages.success(request, "Your record has been successfully restored.")
    
    except Exception as e:  
          
        messages.error(request, f"Something went wrong, or the ID is invalid. Please try again. {e}")
    
    url = reverse_lazy("core:recycle-bin")+"?tab=employees"
    return redirect(url)



class EmployeDeleteView(View):
    
    def post(self, request, id):
    
        try:
            
            employe = Employe.all_objects.get(id=id)
        
            employe.delete()
            messages.success(request, "Your record has been successfully deleted")
        
        except Exception  as e:
            
            messages.error(request, f"something went wrong. {e}")
        
        url = reverse_lazy("app:employe-create-list")
        
        if request.GET.get("redirect_page", "") == "recycle_bin":
            url =  reverse_lazy("core:recycle-bin") + "?tab=employees"
            
        return redirect(url)
        

"""
VISA RENEWAL VIEWS START
"""
class VisaRenewalCreateListView(ModelFormMixin, ListView):
    
    model = VisaRenewal
    template_name = "app/visa_renewal.html"
    form_class = VisaRenewalForm
    paginate_by = 10
    paginate_orphans = 3
    success_url = reverse_lazy("app:visa-renew")
    context_object_name = "visa_renewals"
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.object = None
        self.object_list = list()
    
    
    
    def post(self, *args, **kwargs):
    
        if self.get_form().is_valid(): 
            resp = self.form_valid(form=self.get_form())
            messages.success(self.request, "Your record has been successfully created")
            return resp
        
        resp = self.form_invalid(form=self.get_form())
        
        messages.error(self.request, "An error occurred while processing your request. Please try again.")
        return resp
    
    
    
    def paginate_queryset(self, queryset, page_size:int):
        
        paginator = self.get_paginator(queryset,page_size)
        page = self.request.GET.get("page")
        
        try:
            
            page_obj = paginator.page(page)

        except PageNotAnInteger:
        
            page_obj = paginator.page(1)
            
        except EmptyPage:
            
            page_obj = paginator.page(paginator.num_pages)
        
        
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())


    
    def get_queryset(self) :
        query =  super().get_queryset()
    
        filter_query = VisaRenewalFilter(self.request.GET, queryset=query)
        
        return filter_query.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employers'] = SaudiKapilDetail.objects.all()
        context['visa_types'] = VisaType.objects.all()
        context['employees'] = Employe.objects.all()
        return context


class UpdateVisaRenewalView(View):
    
    
    def post(self, request, id):
        
        try:
            renew = VisaRenewal.objects.get( id=id)
            form = VisaRenewalForm(request.POST, instance=renew)

            if form.is_valid():
    
                form.save()
            
                messages.success(request, "Your record has been updated successfully!")
                
            else:
                messages.error(request, f"Please fix this errors. {form.errors}")
            return redirect(reverse_lazy("app:visa-renew")+f"?employe_iqama={renew.employe.cnic}")
        
        except Exception as e:
            messages.error(request, f"something went wrong. {e}")
            return redirect("app:visa-renew") 
        


class DeleteVisaRenewalView(View):
    
    def post(self, request, id):
    
        try:
            
            renew = VisaRenewal.objects.get(id=id)
        
            renew.delete()
            messages.success(request, "Your record has been successfully deleted")
        
        except Exception  as e:
            
            messages.error(request, f"something went wrong. {e}")
        
        
        return redirect("app:visa-renew")