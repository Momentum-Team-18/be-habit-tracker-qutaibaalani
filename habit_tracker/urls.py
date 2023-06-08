from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("create/", views.newHabit, name="newHabit"),
    path("habit/<int:pk>/", views.habitDetails, name="habitDetails"),
    path("record/<int:pk>", views.newRecord, name="newRecord"),
    path("record/<int:pk>/edit", views.editRecord, name="editRecord"),
    path("record/<int:pk>/delete", views.deleteRecord, name="deleteRecord"),
]
