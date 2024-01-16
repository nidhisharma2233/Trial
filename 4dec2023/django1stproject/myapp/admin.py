from django.contrib import admin
from .models import registermodel
@admin.register(registermodel)
class arthonosys(admin.ModelAdmin):
    list_display = ['username','last_name','email','dob','gender']
