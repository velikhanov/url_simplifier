from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("simplify", views.simplify_url, name="simplify_url"),
    path("url/<str:url_hash>", views.redirect_hash, name="redirect"),
]