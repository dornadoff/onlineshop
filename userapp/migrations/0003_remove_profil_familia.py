# Generated by Django 4.1.7 on 2023-03-08 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_profil_familia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='familia',
        ),
    ]
