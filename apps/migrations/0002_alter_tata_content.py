# Generated by Django 4.1.7 on 2023-07-18 03:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tata',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
