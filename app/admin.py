from django.contrib import admin
from app.models import Zno


@admin.register(Zno)
class ZnoAdmin(admin.ModelAdmin):
    change_list_template = "admin/zno/change_list.html"   
