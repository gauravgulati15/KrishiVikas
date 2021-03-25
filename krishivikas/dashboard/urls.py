from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "dashboard"

urlpatterns = [
    path('<int:id>', views.show_detail, name="show_detail"),
]