# Generated by Django 4.2.6 on 2023-12-17 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_product_imageproduct_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='medicine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.medicine'),
        ),
    ]
