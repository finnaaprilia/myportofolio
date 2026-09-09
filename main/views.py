from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Finna Aprilia",
        "npm": "2506538110",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada bisnis digital dan dunia desain."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Finna Aprilia",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)