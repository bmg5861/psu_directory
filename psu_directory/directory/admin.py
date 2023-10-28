from django.contrib import admin
from .models import Staff

class imageAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "discription", "image"]

admin.site.register(Staff, imageAdmin)
# Register your models here.
