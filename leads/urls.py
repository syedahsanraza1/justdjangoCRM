from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('',views.home_page),
    path('leads/<pk>/',views.lead_detail)


]