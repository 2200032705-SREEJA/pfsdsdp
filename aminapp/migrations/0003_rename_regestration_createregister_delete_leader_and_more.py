# Generated by Django 4.2.6 on 2023-11-04 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aminapp', '0002_regestration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='regestration',
            new_name='createregister',
        ),
        migrations.DeleteModel(
            name='Leader',
        ),
        migrations.DeleteModel(
            name='Party',
        ),
        migrations.AlterModelTable(
            name='createregister',
            table='createregister_table',
        ),
    ]
