from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="main"),
    # path('', RegisterUser.as_view()),
    path('account/', account, name="account")
]