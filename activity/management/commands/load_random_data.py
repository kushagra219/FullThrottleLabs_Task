import sys
import random
from datetime import date, timedelta, datetime
from faker import Faker
from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist

from ...models import ActivityPeriod
from django.contrib.auth import get_user_model
User = get_user_model()

obj = Faker()

class Command(BaseCommand):
    help = 'Populate User and Activity Period table with random dummy data.'

    def handle(self, *args, **options):
        # if len(args) == 0:
        #     sys.stdout.write('You must specify a username.\n')
        #     sys.exit(1)

        for _ in range(5):
            real_name = obj.name()
            print(real_name)
            username = real_name.split()[0]

            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                user = User.objects.create(username=username)
                user.real_name = real_name
                user.save()

            for _ in range(2):
                start_date = obj.date_time()
                end_date = start_date + timedelta(days=90)
                ActivityPeriod.objects.create(
                    user=user,
                    start_time=start_date,
                    end_time=end_date
                )