# Generated by Django 5.0.6 on 2024-07-01 16:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_auto_20240701_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='issue_description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_2description',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
    ]
