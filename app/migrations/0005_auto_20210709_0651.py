# Generated by Django 3.2.3 on 2021-07-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210709_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='marca',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
