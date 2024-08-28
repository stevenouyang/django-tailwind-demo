from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("product/<slug:slug>/", views.single_product, name="single_product"),
    path("htmx-form/", views.htmx_form, name="htmx_form"),
]
