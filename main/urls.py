from django.urls import path

from main.views import show_main, show_education, show_experience, show_interest, show_project, create_project, get_projects_json, delete_project
from main.views import create_experience, get_experiences_json, delete_experience, create_interest, get_interests_json, delete_interest
from main.views import register, login_user, logout_user, toggle_star, edit_project, create_project_ajax, create_experience_ajax, delete_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("education/", show_education, name="show_education"),
    path("experience/", show_experience, name="show_experience"),
    path("interest/", show_interest, name="show_interest"),

    path("project/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:project_id>/edit/", edit_project, name="edit_project"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),

    path("experience/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("experiences/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("experiences/add-ajax/", create_experience_ajax, name="create_experience_ajax"),

    path("interest/add/", create_interest, name="create_interest"),
    path("api/interest/", get_interests_json, name="get_interests_json"),
    path("interest/<uuid:interest_id>/delete/", delete_interest, name="delete_interest"),
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    # Tambahkan path ini ke dalam urlpatterns
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
]