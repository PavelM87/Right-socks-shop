# Generated by Django 3.0.8 on 2020-07-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200727_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='material',
            field=models.CharField(max_length=150, verbose_name='Материал'),
        ),
    ]
