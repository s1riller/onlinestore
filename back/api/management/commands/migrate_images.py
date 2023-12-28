import requests
import time
from django.core.files.base import ContentFile
from api.models import Medicine
from requests.exceptions import MissingSchema


def migrate_images():
    i = 0
    for medicine in Medicine.objects.all():
        if medicine.img:

            try:
                response = requests.get(medicine.img)
                print(response)
                print(medicine.id)
                if response.status_code == 200:
                    time.sleep(1)
                    # Создаем ContentFile из скачанного содержимого
                    img_content = ContentFile(response.content)
                    i = i + 1
                    # Сохраняем файл в поле img модели
                    medicine.img.save(f'{medicine.pk}_image.jpg', img_content, save=True)
            except requests.RequestException as e:
                print(f"Ошибка при запросе: {e}")
            except MissingSchema:
                # Если URL не валидный (например, отсутствует схема), пропускаем его
                print(f"Невалидный URL: {medicine.img}")
