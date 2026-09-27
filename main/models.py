from django.db import models

# Create your models here.

import uuid
from django.db import models
from django.contrib.auth.models import User  # Tambahkan baris ini

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Interest(models.Model):
    INTEREST_CHOICES = [
        ('technology', 'Technology'),
        ('business', 'Business'),
        ('music', 'Music'),
        ('art and culture', 'Art and Culture'),
        ('sport', 'Sport'),
        ('movies and cinema', 'Movies and Cinema'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=INTEREST_CHOICES, default='technology')
    thumbnail = models.URLField(blank=True)
    def __str__(self):
        return self.title


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    major = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.institution


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)

    # Tambahkan field berikut: satu proyek bisa di-star banyak pengguna,
    # dan satu pengguna bisa mem-star banyak proyek
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

    def __str__(self):
        return self.title