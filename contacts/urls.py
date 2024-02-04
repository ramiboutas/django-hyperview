from django.urls import path

from . import views

urlpatterns = [
    path("", views.contact_index, name="contact-index"),
    path("contact-new", views.contact_new, name="contact-new"),
    path("contact/<int:id>", views.contact_detail, name="contact-detail"),
    path("contact/<int:id>/edit", views.contact_edit, name="contact-edit"),
    path("contact/<int:id>/delete", views.contact_delete, name="contact-delete"),
]
