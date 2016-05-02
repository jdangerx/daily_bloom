from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from home.blocks import PullQuote, TransformedImage, Gallery, YouTubeEmbed


class HomePage(Page):
    template = 'home/home_page.html'


class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('pullquote', PullQuote()),
        ('transformed_image', TransformedImage()),
        ('gallery', Gallery()),
        ('HTML', blocks.field_block.RawHTMLBlock()),
        ('YouTube', YouTubeEmbed(label="YouTube share link:")),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]
