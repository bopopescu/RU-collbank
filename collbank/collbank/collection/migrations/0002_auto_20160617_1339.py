# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=50)),
                ('help_url', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='annotation',
            name='type',
            field=models.CharField(help_text="see: <a href=''></a>", max_length=5, verbose_name='Kind of annotation'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(help_text="see: <a href='http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms#type'>Dublin type</a>", max_length=5, verbose_name='Type of this resource'),
        ),
    ]