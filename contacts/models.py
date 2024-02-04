from django.db import models

from django.urls import reverse
from django.utils.functional import cached_property
from django.utils import timezone


class Contact(models.Model):
    TYPES = (
        ("p", "Private"),
        ("b", "Business"),
        ("s", "School"),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    contact_type = models.CharField(max_length=4, choices=TYPES)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Contact({self.first_name} {self.last_name} | {self.phone_number} | {self.email})"

    @cached_property
    def detail_url(self):
        return reverse("contact-detail", kwargs={"id": self.id})

    @cached_property
    def edit_url(self):
        return reverse("contact-edit", kwargs={"id": self.id})

    @cached_property
    def delete_url(self):
        return reverse("contact-delete", kwargs={"id": self.id})
