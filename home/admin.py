from django.contrib import admin
from . models import *

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    fields = ['property', 'image']

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['agent', 'title']


admin.site.register(Agent)
admin.site.register(Category)
admin.site.register(State)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Image)