# Generated by Django 2.2.10 on 2020-06-27 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20200628_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='scopes',
        ),
        migrations.RenameField(
            model_name='articletags',
            old_name='tag',
            new_name='scope',
        ),
    ]
