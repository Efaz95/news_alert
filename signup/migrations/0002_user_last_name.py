# Generated by Django 2.2.4 on 2019-08-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
    ]