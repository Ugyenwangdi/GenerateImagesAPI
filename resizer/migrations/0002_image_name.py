# Generated by Django 4.0.4 on 2022-05-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.TextField(max_length=50, null=True),
        ),
    ]