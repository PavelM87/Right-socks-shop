# Generated by Django 3.0.8 on 2020-07-27 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_squashed_0006_remove_specification_print'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specific',
        ),
    ]
