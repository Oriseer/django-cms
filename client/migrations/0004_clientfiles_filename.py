# Generated by Django 3.2.4 on 2021-06-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20210613_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientfiles',
            name='filename',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
