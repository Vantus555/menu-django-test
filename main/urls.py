from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path("", index.as_view()),
]