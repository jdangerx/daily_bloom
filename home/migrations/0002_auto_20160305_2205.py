# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovableImageRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(height_field='height', upload_to='images', width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, default='', editable=False, max_length=255)),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Filter')),
            ],
        ),
        migrations.AddField(
            model_name='movableimage',
            name='css',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movableimagerendition',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renditions', to='home.MovableImage'),
        ),
        migrations.AlterUniqueTogether(
            name='movableimagerendition',
            unique_together=set([('image', 'filter', 'focal_point_key')]),
        ),
    ]
