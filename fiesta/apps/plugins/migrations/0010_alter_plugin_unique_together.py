# Generated by Django 4.0.6 on 2022-08-02 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0009_alter_sectionsconfiguration_options'),
        ('plugins', '0009_alter_plugin_configuration'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plugin',
            unique_together={('app_label', 'section')},
        ),
    ]
