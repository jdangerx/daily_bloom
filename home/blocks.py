from django import forms
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


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
    width = NumberBlock(required=False, help_text="Percentage")

    class Meta:
        icon = 'image'
        template = 'home/transformed_image.html'
