# Generated by Django 4.2 on 2023-04-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('order', 'title'), 'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
        migrations.AddField(
            model_name='page',
            name='default',
            field=models.BooleanField(default=None, null=True, verbose_name='default page'),
        ),
        migrations.AddConstraint(
            model_name='page',
            constraint=models.UniqueConstraint(models.F('section'), models.F('default'), name='pages_default_section_page_unique'),
        ),
    ]
