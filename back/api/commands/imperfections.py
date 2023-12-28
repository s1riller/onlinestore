import os
import django
from django.db import transaction
from api.models import Imperfection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

@transaction.atomic
def seed_imperfections():
    # Создаем несовершенства
    Imperfection.objects.create(name="Мешки")
    Imperfection.objects.create(name="Морщины")
    Imperfection.objects.create(name="Шрамы")
    print("OKOKOK")

if __name__ == "__main__":
    seed_imperfections()
