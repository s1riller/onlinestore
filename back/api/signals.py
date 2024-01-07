from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, SupplierOrder, SupplierOrderItem, OrderItem


@receiver(post_save, sender=Product)
def check_min_quantity(sender, instance, created, **kwargs):
    if created or instance.quantity < instance.min_quantity:
        # Если товар создан или остаток меньше минимального, создаем заказ у поставщика
        supplier_order = SupplierOrder.objects.create()
        quantity_to_order = instance.min_quantity - instance.quantity
        SupplierOrderItem.objects.create(product=instance, order=supplier_order, quantity=quantity_to_order)


@receiver(post_save, sender=OrderItem)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        # Если объект OrderItem был только что создан (т.е. товар был добавлен в заказ), уменьшаем количество товара
        instance.product.quantity -= instance.quantity
        instance.product.save()