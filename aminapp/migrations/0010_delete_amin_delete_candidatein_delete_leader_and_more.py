# Generated by Django 5.0.3 on 2024-04-26 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aminapp', '0009_alter_leader_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Amin',
        ),
        migrations.DeleteModel(
            name='Candidatein',
        ),
        migrations.DeleteModel(
            name='Leader',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='city',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='country',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='educationalqualificatiom',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='postalcode',
        ),
        migrations.RemoveField(
            model_name='createregister',
            name='region',
        ),
    ]
