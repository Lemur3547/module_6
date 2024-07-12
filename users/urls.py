from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, email_verification_message, email_verification_token, ResetPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('email_confirm/', email_verification_message, name='email_confirm'),
    path('email_confirm/<str:token>/', email_verification_token, name='email_confirm_token'),

    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
]
