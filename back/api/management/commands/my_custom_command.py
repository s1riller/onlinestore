from django.core.management.base import BaseCommand
from api.models import Medicine, Answer
from django.db.models import F
import random


class Command(BaseCommand):
    help = 'Associate all Medicines with random Answers'

    def handle(self, *args, **options):
        medicines = Medicine.objects.all()
        answers = Answer.objects.all()

        for medicine in medicines:
            random_answer = random.choice(answers)
            medicine.treats = random_answer
            medicine.save()

        self.stdout.write(self.style.SUCCESS('Successfully associated all Medicines with random Answers'))
