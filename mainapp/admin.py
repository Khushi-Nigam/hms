from django.contrib import admin
from . models import Patient,Doctor,Login
# Register your models here.
admin.site.register(Patient)
admin.site.register(Login)
admin.site.register(Doctor)