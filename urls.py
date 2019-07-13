from django.urls import path
from falcon import views

urlpatterns = [
    path("", views.home, name="home"),
    path("falcon/<name>", views.falcon_launch_simplified, name="falcon_launch"),
]
