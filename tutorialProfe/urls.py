from django.contrib import admin
from django.urls import path
from laboratorio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("index/detele/<int:equipo_id>", views.delete, name="delete"),
]
