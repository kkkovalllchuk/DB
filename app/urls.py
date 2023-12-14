from django.urls import path
from app import views


urlpatterns = [
    path('admin/fill_data', views.fill_data),
    path('admin/delete_data', views.delete_data),
]
