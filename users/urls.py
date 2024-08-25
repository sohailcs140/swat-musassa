from django.urls import path
from .views import (UserLoginView, UserCreateView, UserUpdateView, UserDeleteView, 
                    UserPasswordChangeView, UserLogoutView, UserPasswordResetView,
                    UserPasswordResetDoneView, UserPasswordResetConfirmView,
                    UserPasswordResetComplete
                    )

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("create-list/", UserCreateView.as_view(), name="user-create-list"),
    path("user/<str:id>/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/<str:id>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("password-change/", UserPasswordChangeView.as_view(), name="password-change"),
    path("user/logout/", UserLogoutView.as_view(), name="logout"),
    
    path("user/password-reset/", UserPasswordResetView.as_view(), name="password-reset"),
    path("user/password-reset-done/", UserPasswordResetDoneView.as_view(), name="password-reset-done"),
    path("user/<uidb64>/<token>/password-reset-confirm/", UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("user/password-reset-complete/", UserPasswordResetComplete.as_view(), name="password_reset_complete"),
]
