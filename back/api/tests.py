from django.test import TestCase
from api.models import ImageProduct
from django.core.files import File

class ImageModelTest(TestCase):
    def test_image_model_save_and_retrieve(self):
        with open('api/images/awesomeAvatar.png', 'rb') as img_file:
            image1 = ImageProduct(
                title="image 1",
                image=File(img_file, name='awesomeAvatar.png')
            )
            image1.save()

        with open("api/images/i.jpeg", 'rb') as img_file:
            image2 = ImageProduct(
                title="image 2",
                image=File(img_file, name='i.jpeg')
            )
            image2.save()

        all_images = ImageProduct.objects.all()

        self.assertEquals(len(all_images), 2)
        self.assertEquals(all_images[0].title, image1.title)
        self.assertEquals(str(all_images[0].image), image1.image.name)
        self.assertEquals(all_images[1].title, image2.title)
        self.assertEquals(str(all_images[1].image), image2.image.name)
