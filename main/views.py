from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from main.models import Experience
from main.models import Interest


def show_main(request):
    context = {
        "name": "Finna Aprilia",
        "npm": "2506538110",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Undergraduate Information Systems Student at Universitas Indonesia "
            "with an interest in technology, digital business, and design."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Finna Aprilia",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_interest(request):
    context = {
        "name": "Finna Aprilia",
        "interest_list": Interest.objects.all(),
    }

    return render(request, "interest.html", context)