# Generated by Django 2.1.5 on 2019-01-28 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='badge',
            field=models.ImageField(blank=True, null=True, upload_to='pylint_badge'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='public_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
