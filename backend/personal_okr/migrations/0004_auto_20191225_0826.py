# Generated by Django 3.0 on 2019-12-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_okr', '0003_auto_20191217_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyresult',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='objective',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
