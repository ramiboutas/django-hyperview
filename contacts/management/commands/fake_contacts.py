from django.core.management.base import BaseCommand
from django.db import transaction

from faker import Faker

from contacts.models import Contact


class Command(BaseCommand):
    help = "Fake contacts and save them in the db"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Processing...")
        contacts = []
        fake = Faker()
        for id in range(50):
            contacts.append(
                Contact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    email=fake.email(),
                )
            )
        Contact.objects.bulk_create(contacts)
