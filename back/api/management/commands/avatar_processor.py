
import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import User

class Command(BaseCommand):
    help = 'Process avatars and save them locally'

    def handle(self, *args, **options):
        users = User.objects.filter(processed_photo=False)

        for user in users:
            image_url = user.avatar.url
            response = requests.post(
                'https://ru.clippingmagic.com/api/v1/images',

                data={
                    'image.url': f"http://localhost:8000{user.avatar.url}",
                    'format': 'result',
                    'test': 'true',  # TODO: Remove for production
                },
                headers={
                    'Authorization': 'Basic MTgwNzg6ZGpvZ2FicmdtYnYyY3E5ZnE1cmxndWZoZWpjMjJmc2l0cXFvYmRzM3ZnZmhicmdpbzRvMg=='
                },
            )

            if response.status_code == requests.codes.ok:
                unique_filename = os.path.join(settings.MEDIA_ROOT, 'avatars', f'{user.id}_{user.username}_processed.png')
                user.avatar.save(unique_filename, ContentFile(response.content), save=True)
                user.processed_photo = True
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully processed avatar for user {user.username}'))
            else:
                self.stderr.write(self.style.ERROR(f'Error processing avatar for user {user.username}: {response.status_code}, {response.text}'))
