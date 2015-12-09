# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151208_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('tittle', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published')),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Blog'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
