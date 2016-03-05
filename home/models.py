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


class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]


class MovableImage(AbstractImage):
    css = models.TextField(blank=True)
    admin_form_fields = (
        'title',
        'file',
        'tags',
        'css',
        'focal_point_x',
        'focal_point_y',
        'focal_point_width',
        'focal_point_height',
    )


class MovableImageRendition(AbstractRendition):
    image = models.ForeignKey(MovableImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )

    @property
    def attrs_dict(self):
        return OrderedDict([
            ('src', self.url),
            ('alt', self.alt),
            ('style', self.image.css)
        ])
