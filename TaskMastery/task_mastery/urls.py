from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *

app_name = 'task_mastery'

urlpatterns = [
    path('', LoginUser.as_view(), name="main"),
    path('registration', register, name="registration"),
    # path('', RegisterUser.as_view()),
    path('account', account, name="account"),
    path('logout', logout_user, name="logout"),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name="task_mastery/password_reset_form.html",
             email_template_name="registration/password_reset_email.html",
             success_url=reverse_lazy("task_mastery:password_reset_done")
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name = "task_mastery/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="task_mastery/password_reset_confirm.html",
             success_url=reverse_lazy("task_mastery:password_reset_complete")
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="task_mastery/password_reset_complete.html"), name='password_reset_complete'),
    
]