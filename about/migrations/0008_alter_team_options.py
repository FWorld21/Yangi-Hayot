# Generated by Django 3.2.7 on 2021-09-14 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Человека', 'verbose_name_plural': 'Команда'},
        ),
    ]