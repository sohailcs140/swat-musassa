from django.urls import path
from .views import (
    SaudiKapilCreateListView,SauidiKapilUpdateView, SauidiKapilDeleteView,
    EmployeCreateListView, EmployeUpdateView, EmployeDetailView , EmployeDeleteView,
     EmployerDetailView, VisaRenewalCreateListView, UpdateVisaRenewalView, DeleteVisaRenewalView,
    employer_activate, employer_deactivate,
    employee_activate, employee_deactivate
)

from .reports import ReportView, get_employee_report


app_name = "app"

urlpatterns = [
    # Employer Paths
    path("employer/create-list/", SaudiKapilCreateListView.as_view(), name="saudi-kapil-create-list"),
    path("employer/<str:id>/update/", SauidiKapilUpdateView.as_view(), name="saudi-kapil-update"),
    path("employer/<str:id>/delete/", SauidiKapilDeleteView.as_view(), name="saudi-kapil-delete"),
    path("employer/<str:id>/", EmployerDetailView.as_view(), name="saudi-kapil-detail"),
    path("employer/<str:id>/deactivate/", view=employer_deactivate, name="saudi-kapil-deactivate"),
    path("employer/<str:id>/activate/", view=employer_activate, name="saudi-kapil-activate"),
    
    # Employe Paths
    path("employee/create-list/", EmployeCreateListView.as_view(), name="employe-create-list"),
    path("employee/<str:id>/update/", EmployeUpdateView.as_view(), name="employe-update"),
    path("employee/<str:id>/delete/", EmployeDeleteView.as_view(), name="employe-delete"),
    path("employee/<str:id>/", EmployeDetailView.as_view(), name="employe-detail"),
    path("employee/<str:id>/deactivate/", view=employee_deactivate, name="employe-deactivate"),
    path("employee/<str:id>/activate/", view=employee_activate, name="employe-activate"),
    
    
    # Visa Renewal Paths
    path("visa-renew/", VisaRenewalCreateListView.as_view(), name="visa-renew"),
    path("visa-renew/<str:id>/update/", UpdateVisaRenewalView.as_view(), name="visa-renew-update"),
    path("visa-renew/<str:id>/delete/", DeleteVisaRenewalView.as_view(), name="visa-renew-delete"),
    path("reports/visas/", view=ReportView.as_view(), name="visa-reports"),
    path("employee/<str:id>/report/", get_employee_report, name="employee_report")
    
]
