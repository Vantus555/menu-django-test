from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path("", index.as_view()),
    path("page_1", page_1.as_view()),
    path("page_1_1", page_1_1.as_view()),
    path("page_1_2", page_1_2.as_view()),
    path("page_1_1_1", page_1_1_1.as_view(), name="page_1_1_1"),
    path("page_1_1_2", page_1_1_2.as_view()),

    path("page_2", page_2.as_view(), name="page_2"),

    path("page_3", page_3.as_view(), name="page_3"),

    path("sub_page_1", sub_page_1.as_view(), name="sub_page_1"),
    path("sub_page_1_1", sub_page_1_1.as_view(), name="sub_page_1_1"),
    path("sub_page_1_1_1", sub_page_1_1_1.as_view(), name="sub_page_1_1_1"),

    path("sub_page_2", sub_page_2.as_view(), name="sub_page_2"),
]
