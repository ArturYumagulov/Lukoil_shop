from django.shortcuts import render
from content.models import Slider


def index(requests):
    slides = Slider.objects.filter(is_active=True)
    context = {'slides': slides}
    return render(requests, "base.html", context)
