from django.urls import path
from . import views

app_name = "artlog"

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("art/<int:pk>/", views.artwork_detail, name="detail"),
]