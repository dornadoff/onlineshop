# Generated by Django 4.1.7 on 2023-03-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0005_savat'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='miqdor',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='savat',
            name='umumiy',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
