# Generated by Django 2.2.10 on 2020-06-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200627_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.TextField(null=True, verbose_name='Тематический раздел'),
        ),
    ]