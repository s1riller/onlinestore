# Generated by Django 4.2.6 on 2023-12-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_answer_img_alter_usertestresult_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertestresult',
            name='rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]