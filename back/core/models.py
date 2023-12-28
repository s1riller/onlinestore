from django.db import models
from versatileimagefield.fields import VersatileImageField


# Create your models here.


class BaseImage(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    alt = models.CharField(max_length=200,null=True,blank=True)
    image = VersatileImageField(null=True, blank=True,upload_to='images')

    class Meta:
        abstract = True
        verbose_name = "image"
        verbose_name_plural = "images"

    def __str__(self):
        res = ''
        if self.title:
            res = self.title
        else:
            res = self.image.url
        return res