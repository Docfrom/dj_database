import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone.objects.create(
                id=phone[0],
                name=phone[1],
                image=phone[2],
                price=phone[3],
                release_date=phone[4],
                lte_exists=phone[5],
                slug=slugify(phone[1]),
            )