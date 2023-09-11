from django.contrib import admin
from .models import book
 # Register your models here.

@admin.register(book)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
book._meta.get_fields()]
