from django.urls import path

from . import views

app_name = "event"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("vote/<int:question_id>/", views.vote, name="vote"),
]
