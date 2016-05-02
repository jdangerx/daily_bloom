import re
import six

from django import forms
from django.utils.safestring import mark_safe

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class NumberBlock(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.DecimalField(required=required, help_text=help_text)
        super(NumberBlock, self).__init__(**kwargs)


class PullQuote(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'home/pullquote.html'


class TransformedImage(blocks.StructBlock):
    image = ImageChooserBlock()
    alignment = blocks.ChoiceBlock([
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right")
    ])
    width = NumberBlock(initial=100, label="Width in percentage", help_text="Percentage")

    class Meta:
        icon = 'image'
        template = 'home/transformed_image.html'


class Gallery(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock())
    alignment = blocks.ChoiceBlock([
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right")
    ])
    width = NumberBlock(initial=100, label="Width in percentage", help_text="Percentage")

    class Meta:
        icon = 'image'
        template = 'home/gallery.html'


class YouTubeEmbed(blocks.field_block.RawHTMLBlock):
    def validate_video_id(self, video_id):
        # TODO: query http://gdata.youtube.com/feeds/api/videos/VIDEO_ID instead
        if video_id == "":
            return
        if len(video_id) != 11:
            raise ValueError("Invalid YouTube video ID (too long): {}".format(video_id))
        if re.search(r"[^a-zA-Z0-9_]", video_id):
            raise ValueError("Invalid YouTube video ID (bad chars): {}".format(video_id))

    def value_from_form(self, value):
        if len(value.split("=")) > 1:
            video_id = value.split("=")[-1]
        else:
            video_id = value.split("/")[-1]
        self.validate_video_id(video_id)
        val = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/{}"
 frameborder="0" allowfullscreen></iframe>'''.format(video_id)
        return mark_safe(val)

    def value_for_form(self, value):
        m = re.search(r'src="https://www.youtube.com/embed/([a-zA-Z0-9_]+)"', value)
        val = ""
        if m:
            val = "https://youtu.be/{}".format(m.group(1))
        return six.text_type(val)
