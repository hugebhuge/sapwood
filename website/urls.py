'''from django.urls import path
from .views import consultation_create

urlpatterns = [
    path("consultation/", consultation_create, name="consultation"),
]'''

from django.urls import path
from .views import home, consultation_create


urlpatterns = [
    path("", home),
    path("consultation/", consultation_create),
]