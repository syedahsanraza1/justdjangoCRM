from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('',views.home_page,name='lead-list'),
    path('leads/create/',views.create_leads,name='lead-create'),
    path('leads/<int:pk>/',views.lead_detail,name='lead-detail'),
    path('leads/<int:pk>/update/',views.lead_update, name='lead-update'),
    path('leads/<int:pk>/delete/',views.delete_lead,name='lead-delete'),
    


]