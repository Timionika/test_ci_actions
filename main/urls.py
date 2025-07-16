"""
URL configuration for main project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("company/", include("company.urls")),
    path("admin/", admin.site.urls),
    path("", include("social_django.urls", namespace="social")),
]
