from django.urls import resolve
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy as _



class LoginRequiredMiddleware:
    
    
    def __init__(self, get_response):
        
        self.get_response = get_response
    
    
    
    def __call__(self, request):
        
        
        url_name = resolve(request.path_info).url_name
        
        
        if not request.user.is_authenticated and not url_name in settings.LOGIN_EXEMPT_URLS:
            
            return redirect(_("login"))
        
        
        return self.get_response(request)