from django.contrib import admin
from .models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_date', 'edit_date')



admin.site.register(Slider, SliderAdmin)
