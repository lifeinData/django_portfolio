from django.shortcuts import render

# import the objects to use for this page
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
