from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name="main"),
    path('registration', register, name="registration"),
    # path('', RegisterUser.as_view()),
    path('account/', account, name="account")
]