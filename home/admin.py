from django.contrib import admin
from . models import Agent, Category, Property 

# Register your models here.

admin.site.register(Agent)
admin.site.register(Category)
admin.site.register(Property)