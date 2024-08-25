from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView
                                       )
from .forms import (UserAuthenticationForm, User, UserCreateForm, UserUpdateForm, 
                    UserPasswordResetForm,
                    UserPasswordChangeForm)
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class UserLoginView(LoginView):
    
    
    template_name = "users/login.html"
    authentication_form = UserAuthenticationForm
    redirect_authenticated_user = True 

    def form_valid(self, form) -> HttpResponse:
        response =  super().form_valid(form)

        messages.success(request=self.request, message="Login Success")
        return response
    
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        
        messages.error(request=self.request, message=f"Field to login. email or password is incorect")
        
        return response
    
    

class UserLogoutView(SuccessMessageMixin, LogoutView):
    
    # next_page = "/"
    success_message = "User logout"


class UserPasswordResetView(PasswordResetView):
    
    template_name="users/password_reset.html"
    success_url = reverse_lazy("password-reset-done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    
    template_name = "users/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    
    template_name = "users/password_reset_confirm.html"
    form_class = UserPasswordResetForm
    success_url = reverse_lazy("password_reset_complete")
    
    def form_valid(self, form) -> HttpResponse:
        response =  super().form_valid(form)
        
        messages.success(request=self.request, message="Password has been changed now you can login with new password.")
        return response

class UserPasswordResetComplete(PasswordResetCompleteView):
    
    template_name = "users/password_reset_complete.html"


class UserCreateView(ModelFormMixin, ListView):
    
    model = User
    template_name="users/users_list.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("user-create-list")
    context_object_name = "users"
    paginate_by = 10
    paginate_orphans = 3
    
    
    def __init__(self):
        
        super().__init__()
        
        self.object = None
        self.object_list = []
    
    def post(self, *args, **kwargs):
        
        try:
            
            
            email = self.request.POST.get("email")

            if User.objects.filter(email=email).exists():
                messages.error(request=self.request, message="Email is already taken.")
                return redirect(self.request.path)
            
            
            if self.get_form().is_valid():
                
                
                user = self.get_form().save(commit=True)
                user.set_password(self.request.POST.get("password"))
                user.save()
                messages.success(request=self.request, message="User created successfully")
                return redirect(self.request.path)
            
            
            resp = self.form_invalid(form=self.get_form())
            err = self.get_form().errors.values()
            messages.error(request=self.request, message=f"{err}")
            
            
            return resp
        
        
        except Exception as e:
            
            messages.error(request=self.request, message=f"{e}")
            return redirect(self.request.path)
        



class UserUpdateView(View):
    

    def post(self, request, id):
        
        
        try:
            
            user = User.objects.get(id=id)
            form = UserUpdateForm(request.POST,request.FILES, instance=user)
        
            if form.is_valid():
                form.save()

                messages.success(request, 'user updated successfully')

            else:
                messages.success(request, form.errors)
            
        except Exception as e:
            
            messages.error(request, e)
        
        return redirect("user-create-list")
    
    

class UserDeleteView(View):
    

    def post(self, request, id):
        
        
        try:
            
            if User.objects.count() <=1:
                
                raise Exception("Cannot delete the last user. Please add another user before deleting this one.")
            
            user = User.objects.get(id=id)
            user.delete()
            messages.success(request, 'user deleted successfully')

            
            
        except Exception as e:
            
            messages.error(request, e)
        
        return redirect("user-create-list")
    


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    
    template_name = "users/password_change.html"
    success_url = "/"
    form_class = UserPasswordChangeForm
    success_message = "Your password was changed successfully."
    
   
        
        
        