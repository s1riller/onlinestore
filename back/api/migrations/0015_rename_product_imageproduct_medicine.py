# Generated by Django 4.2.6 on 2023-12-17 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_medicine_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageproduct',
            old_name='product',
            new_name='medicine',
        ),
    ]