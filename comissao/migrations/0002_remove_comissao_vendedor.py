# Generated by Django 2.2.3 on 2019-07-08 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comissao',
            name='vendedor',
        ),
    ]
