# Generated by Django 3.0.7 on 2020-07-18 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0004_wordlist_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordlist',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
