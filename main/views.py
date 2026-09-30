import datetime
from django.shortcuts import render

from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini

from django.http import JsonResponse

# Create your views here.

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from main.models import Experience
from main.models import Interest
from main.models import Education
from main.models import Project
from main.forms import ProjectForm, ExperienceForm, InterestForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Finna Aprilia",
        "npm": "2506538110",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Undergraduate Information Systems Student at Universitas Indonesia "
            "with an interest in technology, digital business, and design."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_education(request):
    context = {
        "name": "Finna Aprilia",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)


def show_experience(request):
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Finna Aprilia",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def show_interest(request):
    json_response = get_interests_json(request)

    interests = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    interests = [interest.object for interest in interests]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Finna Aprilia",
        "interest_list": interests,
        "title_query": title_query,
    }

    return render(request, "interest.html", context)


# def show_project(request):
#     json_response = get_projects_json(request)

#     projects = serializers.deserialize(
#         "json",
#         json_response.content.decode("utf-8"),
#     )
#     projects = [project.object for project in projects]
#     title_query = request.GET.get("title", "").strip()

#     is_editor = (
#             request.user.is_authenticated
#             and request.user.groups.filter(name="Editor").exists()
#         )

#     context = {
#         "name": "Finna Aprilia",
#         "project_list": projects,
#         "title_query": title_query,
#         "is_editor": is_editor,
#     }

#     return render(request, "project.html", context)


def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Finna Aprilia",
        "title_query": title_query,
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")    # Tambahkan baris ini
def create_project(request):

    # Dua baris berikut yang ditambahkan pada langkah ini.
    # Cek apakah akun yang sedang login adalah superuser (admin/kamu);
    # kalau bukan, hentikan permintaannya dengan 403.
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Finna Aprilia",
        "form": form,
    }
    return render(request, "projects_form.html", context)


# def get_projects_json(request):
#     title_query = request.GET.get("title", "").strip()
#     projects = Project.objects.all()

#     if title_query:
#         projects = projects.filter(title__icontains=title_query)

#     projects_json = serializers.serialize("json", projects)
#     return HttpResponse(projects_json, content_type="application/json")


# Agar fitur star tetap berfungsi saat data diubah ke JSON:
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")    # Tambahkan baris ini
def delete_project(request, project_id):

    # Dua baris berikut yang ditambahkan pada langkah ini.
    # Cek apakah akun yang sedang login adalah superuser (admin/kamu);
    # kalau bukan, hentikan permintaannya dengan 403.
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

@login_required(login_url="/login/")
def edit_project(request, project_id):

    is_editor = (
                request.user.is_authenticated
                and request.user.groups.filter(name="Editor").exists()
            )
    
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    # inisialisasi form dengan mengisi data lama
    form = ProjectForm(request.POST or None, instance=project)

    # jika form dikirim (POST) dan datanya valid, maka simpan perubahannya
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbaharui")
        return redirect("main:show_project")

    context = {
        "name": "Finna Aprilia",
        "form": form,
        "project": project,
        "is_edit": True,
    }
    return render(request, "projects_form.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Finna Aprilia",
        "form": form,
    }
    return render(request, "experiences_form.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def create_interest(request):
    form = InterestForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Hobi baru berhasil ditambahkan!")
        return redirect("main:show_interest")

    context = {
        "name": "Finna Aprilia",
        "form": form,
    }
    return render(request, "interests_form.html", context)

def get_interests_json(request):
    title_query = request.GET.get("title", "").strip()
    interests = Interest.objects.all()

    if title_query:
        interests = interests.filter(title__icontains=title_query)

    interests_json = serializers.serialize("json", interests)
    return HttpResponse(interests_json, content_type="application/json")

def delete_interest(request, interest_id):
    interest = get_object_or_404(Interest, pk=interest_id)

    if request.method == "POST":
        interest.delete()
        messages.success(request, "Hobi berhasil dihapus!")
        return redirect("main:show_interest")

    return redirect("main:show_interest")



def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Finna Aprilia",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Finna Aprilia",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login")    #  menghapus cookie last_login menggunakan method delete_cookie()
                                            #  agar informasi di browser klien tetap sinkron dan bersih
    return response


# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")