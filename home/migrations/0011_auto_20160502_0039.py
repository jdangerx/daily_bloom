# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-02 00:39
from __future__ import unicode_literals

from django.db import migrations
import home.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160501_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('transformed_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('width', home.blocks.NumberBlock(help_text='Percentage', initial=100, label='Width in percentage'))))), ('gallery', wagtail.wagtailcore.blocks.StructBlock((('images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock())), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('width', home.blocks.NumberBlock(help_text='Percentage', initial=100, label='Width in percentage'))))), ('canvas', wagtail.wagtailcore.blocks.StructBlock((('js', wagtail.wagtailcore.blocks.TextBlock(label='JavaScript file')), ('width', home.blocks.NumberBlock(help_text='Percentage', initial=100, label='Width in percentage')), ('height', home.blocks.NumberBlock(help_text='Percentage', initial=100, label='Height in percentage'))))), ('HTML', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('YouTube', home.blocks.YouTubeEmbed(label='YouTube share link:')))),
        ),
    ]
