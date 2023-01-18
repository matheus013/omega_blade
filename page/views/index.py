from django.shortcuts import render

from datetime import datetime, timedelta


def index(request):
    return render(request, 'cyborg/index.html', {})
