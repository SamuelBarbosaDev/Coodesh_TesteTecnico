# Generated by Django 4.1.2 on 2022-10-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_links_options_remove_spacex_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='iid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]