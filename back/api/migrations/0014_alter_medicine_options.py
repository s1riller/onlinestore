# Generated by Django 4.2.6 on 2023-12-17 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_imageproduct_options_imageproduct_alt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Медикамент', 'verbose_name_plural': 'Медикаменты'},
        ),
    ]