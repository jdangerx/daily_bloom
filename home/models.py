from __future__ import unicode_literals
from collections import OrderedDict

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.models import AbstractImage, AbstractRendition


class HomePage(Page):
    pass


class PullQuote(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'home/pullquote.html'


class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('pullquote', PullQuote()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]

