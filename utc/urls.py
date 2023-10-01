from django.urls import path
from . import views

urlpatterns = [
    path("api/<str:input_value>/",views.convert_to_utc, name="timestamp")
]
