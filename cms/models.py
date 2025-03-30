from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import StructBlock, TextBlock
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail.search import index


class HomePage(Page):
    # Swiper images for events
    swiper_images = StreamField(
        [
            (
                "image",
                StructBlock([("image", ImageChooserBlock())]),
            ),
        ],
        blank=True,
        use_json_field=True,
    )

    # Team members
    team_members = StreamField(
        [
            (
                "member",
                StructBlock(
                    [
                        ("name", TextBlock()),
                        ("role", TextBlock(required=False)),
                        ("image", ImageChooserBlock(required=False)),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
    )

    # Testimonial section
    testimonials = StreamField(
        [
            (
                "testimonial",
                StructBlock(
                    [
                        ("name", TextBlock()),
                        ("text", TextBlock()),
                        ("image", ImageChooserBlock()),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
    )

    # Define the search index for this page
    search_fields = Page.search_fields + [
        index.SearchField("team_members"),
        index.SearchField("swiper_images"),
        index.SearchField("testimonials"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("swiper_images"),
        FieldPanel("team_members"),
        FieldPanel("testimonials"),
    ]

    def get_events_page(self):
        # Get the first live EventPage child, regardless of slug
        return self.get_children().live().type(EventPage).first()

    template = "website/home.html"


class EventPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    # Specify the exact location of your HTML template
    template = "website/events_list.html"

    # Restrict child pages to EventDetailsPage
    subpage_types = ["cms.EventDetailsPage"]


class EventDetailsPage(Page):
    # Fields for the event page
    intro = RichTextField(blank=True)
    date = models.DateTimeField(help_text="Date and time of the event")
    description = RichTextField(help_text="A detailed description of the event")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Upload the main event image",
    )

    # Specify the exact location of your HTML template
    template = "website/event_details.html"
    
    # Define the search index for this page
    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("description"),
    ]
   
    # register Page amd define the editable fields in the Wagtail admin
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("date"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]

    # Customize the URL slug
    def get_url_path(self, request=None):
        return super().get_url_path(request)
