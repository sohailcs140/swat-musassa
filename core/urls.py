from django.urls import path
from .views import( VisaCreateView, VisaUpdateView,VisaTypeDelete,RecycleBinView,
                   visa_type_activate, visa_type_deactivate,
                   )
from .send_emails import SendEmailsView, SendEmailView


app_name = "core"

urlpatterns = [
    path("visa/", view=VisaCreateView.as_view(), name="visa-type-create"),
    path("visa/<str:id>/update/", view=VisaUpdateView.as_view(), name="visa-type-update"),
    path("visa/<str:id>/delete/", view=VisaTypeDelete.as_view(), name="visa-type-delete"),
    path("visa/<str:id>/deactivate/", view=visa_type_deactivate, name="visa-type-deactivate"),
    path("visa/<str:id>/activate/", view=visa_type_activate, name="visa-type-activate"),
    path("recycle-bin/", RecycleBinView.as_view(), name="recycle-bin"),
    path("send_emails/", SendEmailsView.as_view(), name="send-emails"),
    path("employe/<str:id>/send-mail/", SendEmailView.as_view(), name="send-email"),
    
  
]
