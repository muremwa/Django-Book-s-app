# Generated by Django 2.0 on 2018-03-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180324_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
