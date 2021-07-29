from django.contrib import admin
from .models import Photographer


# admin.site.register(Photographer)
# Register your models here.
@admin.register(Photographer)
class PhotographerModel(admin.ModelAdmin):
    list_filter = ('vendor_id', 'company_name')
    list_display = ('vendor_id', 'company_name')

