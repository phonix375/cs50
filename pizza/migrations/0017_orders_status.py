# Generated by Django 3.0 on 2020-01-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0016_auto_20200116_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default='panding', max_length=30),
        ),
    ]
