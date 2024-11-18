from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Aeroport
from .models import Avion
 
admin.site.register(Aeroport)
admin.site.register(Avion)
