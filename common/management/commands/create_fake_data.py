from faker import Faker
from tqdm import tqdm

from django.db import transaction
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

fake = Faker()

from core.models import User, Organization, OrganizationMember
from addressio.models import PostOffice, Address, AddressConnector


class CommonProperties:
    current_datetime = timezone.now()
    previous_datetime = current_datetime - timedelta(days=1500)
    all_address = []
    post_office = PostOffice.objects.first()
    for i in range(3):
        address = Address.objects.create(
            country="Bangladesh",
            house_street="1",
            label="house",
            division=post_office.division,
            district=post_office.district,
            upazila=post_office.upazila,
            post_office=post_office,
        )
        all_address.append(address)


class Command(BaseCommand):
    help = "some fake data to get you started"

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Creating 3 fake users")
            # storign unique emails
            emails = list(set([fake.email() for _ in range(3)]))
            user_obj = []
            for email in tqdm(emails):
                user = User(
                    first_name=fake.name(),
                    last_name=fake.name() + "fake",
                    email=email,
                    password="123456",
                )
                user.save()
                for address in CommonProperties.all_address:
                    AddressConnector.objects.create(address=address, user=user)
                user_obj.append(user)

            User.objects.bulk_create(user_obj, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS("***All data created successfully***"))
