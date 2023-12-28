# abstract_user/users/models.py
import requests
from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import BaseImage
from django.conf import settings
import core.models


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        default='avatars/images.png',  # Путь к изображению по умолчанию
        blank=True,
    )

    processed_photo = models.BooleanField(verbose_name='Обработанное фото',
                                          default=False)


class Imperfection(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkinType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    img = models.TextField(default='')

    def __str__(self):
        return self.text


class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


def file_location(instance, filename):
    # Используйте существующее поле, например, 'name'
    file_path = f"medicine/{instance.name}-{filename}"
    return file_path



class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    treats = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None, null=True)
    img = models.ImageField(upload_to=file_location, null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Медикамент"
        verbose_name_plural = "Медикаменты"


def __str__(self):
    return self.name


class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.JSONField()
    time = models.TimeField()
    medicine = models.TextField(default='')
    rate = models.IntegerField(null=True, blank=True, default=0)


class ImageProduct(BaseImage):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True, related_name='images')

    def __str__(self):
        return self.title






class Order(models.Model):
    # Ссылка на пользователя, совершившего заказ
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='orders',null=True)
    products = models.ManyToManyField(Medicine, through='OrderItem', related_name='orders')
    # Контактная информация
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    postal_code = models.CharField(max_length=20, blank=True, null=True)  # Необязательно

    # Информация о доставке
    delivery_date = models.DateTimeField()  # Дата и время доставки
    delivery_instructions = models.TextField(blank=True, null=True)  # Дополнительные инструкции

    # Финансовая информация
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Общая стоимость заказа
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Стоимость доставки

    # Статус заказа
    ORDER_STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending')

    # Дата создания и обновления заказа
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} by {self.user}'

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
