# Generated by Django 2.2.10 on 2020-06-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200627_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.TextField(null=True),
        ),
    ]