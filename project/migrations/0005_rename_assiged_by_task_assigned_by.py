# Generated by Django 3.2.7 on 2021-10-09 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_task_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assiged_by',
            new_name='assigned_by',
        ),
    ]
