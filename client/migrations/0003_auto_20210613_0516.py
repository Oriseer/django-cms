# Generated by Django 3.2.4 on 2021-06-13 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20210613_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_upload',
        ),
        migrations.AddField(
            model_name='clientfiles',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='client.client'),
            preserve_default=False,
        ),
    ]
