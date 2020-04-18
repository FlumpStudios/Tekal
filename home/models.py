from django.db import models
import os
import sys

from django.core.mail import send_mail
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel,FieldRowPanel, ObjectList,TabbedInterface
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.fields import ParentalKey
from colorfield.fields import ColorField
import feedparser
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


# class carouselOrderable(Orderable, models.Model):
#     page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='carouselOrderable')
    
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )

#     class Meta:
#         verbose_name = "carousel item"
#         verbose_name_plural = "carousel items"

#     panels = [
#          ImageChooserPanel('image')
#     ]

#     def __str__(self):
#         return self.page.title + " -> " + self.gallery.name


# class galleryOrderable(Orderable, models.Model):
#     page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='galleryOrderable')
#     gallery = models.ForeignKey('gallery', on_delete=models.CASCADE, related_name='+')

#     class Meta:
#         verbose_name = "gallery item"
#         verbose_name_plural = "gallery items"

#     panels = [
#         SnippetChooserPanel('gallery'),
#     ]

#     def __str__(self):
#         return self.page.title + " -> " + self.gallery.name


class enumeratedListOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='enumeratedListOrderable')
    enumeratedList = models.ForeignKey('enumeratedList', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Panel item"
        verbose_name_plural = "Panel items"

    panels = [
        SnippetChooserPanel('enumeratedList'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class PricingEnumeratedListOrderable(Orderable, models.Model):
    page = ParentalKey('PricingPage', on_delete=models.CASCADE, related_name='PricingEnumeratedListOrderable')
    enumeratedList = models.ForeignKey('enumeratedList', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Panel item"
        verbose_name_plural = "Panel items"

    panels = [
        SnippetChooserPanel('enumeratedList'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class iconListOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='iconListOrderable')
    iconItem = models.ForeignKey('iconItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Panel item"
        verbose_name_plural = "Panel items"

    panels = [
        SnippetChooserPanel('iconItem'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class featuresIconListOrderable(Orderable, models.Model):
    page = ParentalKey('FeaturesPage', on_delete=models.CASCADE, related_name='featuresIconListOrderable')
    iconItem = models.ForeignKey('iconItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Panel item"
        verbose_name_plural = "Panel items"

    panels = [
        SnippetChooserPanel('iconItem'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class testimonialOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='testimonialOrderable')
    testimonialItem = models.ForeignKey('testimonialItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Testimonial List item"
        verbose_name_plural = "Testimonial List items"

    panels = [
        SnippetChooserPanel('testimonialItem'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class socialMediaOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='socialMediaOrderable')
    socialMediaItem = models.ForeignKey('socialMediaItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Social Media item"
        verbose_name_plural = "Social Media items"

    panels = [
        SnippetChooserPanel('socialMediaItem'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name


class qAOrderable(Orderable, models.Model):
    page = ParentalKey('PricingPage', on_delete=models.CASCADE, related_name='qAOrderable')
    qaList = models.ForeignKey('qaList', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Q&A item"
        verbose_name_plural = "Q&A items"

    panels = [
        SnippetChooserPanel('qaList'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.page.question


@register_snippet
class socialMediaItem(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)    
    icon = models.CharField(max_length=50)

    panels = [
        FieldPanel('link'),
        FieldPanel('name'),
        FieldPanel('icon')
    ]

    def __str__(self):
        return self.name


@register_snippet
class enumeratedList(models.Model):    
    title = models.CharField(max_length=50,  blank=True)
    subtitle = models.CharField(max_length=50,  blank=True)    
    text = RichTextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    linkText = models.CharField(max_length=100, blank=True)
    linkUrl = models.CharField(max_length=100, blank=True)    

    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),       
        FieldPanel('text'),
        FieldPanel('icon'),
        FieldPanel('linkText'),
        FieldPanel('linkUrl')
    ]

    def __str__(self):
        return self.title


@register_snippet
class iconItem(models.Model):    
    title = models.CharField(max_length=50)        
    icon = models.CharField(max_length=50)
    text = RichTextField(blank=True)        
    linkText = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('icon'),
        FieldPanel('text'),
        FieldPanel('linkText'),                
        FieldPanel('link')
    ]

    def __str__(self):
        return self.title

@register_snippet
class testimonialItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author = models.CharField(max_length=50)
    testimonial = RichTextField(blank=True)
    
    panels = [
        FieldPanel('author'),
        FieldPanel('testimonial')
    ]

    def __str__(self):
        return self.author

@register_snippet
class qaList(models.Model):
    question = models.CharField(max_length=120)
    answer = models.CharField(max_length=5000)
    

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]

    def __str__(self):
        return self.question

class HomePage(Page):
    subpage_types = ['home.BlogIndexPage', 'home.FormPage', 'home.FeaturesPage', 'home.PricingPage','home.ContentPage']

    def has_address(self):
        return self.client_organisationName or self.client_addressLine1 or self.client_addressLine2 or self.client_town or self.client_county or self.client_postcode

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        medium_blogs = feedparser.parse(str("https://medium.com/feed/" + self.medium_username) if self.medium_username else "" )
        videoFormatIsVimeo = str(self.intro_video_id).isdigit()
        context['medium_blogs'] = medium_blogs.entries[:self.medium_blog_display_limit]
        context['has_address'] = self.has_address()
        context['videoFormatIsVimeo'] = videoFormatIsVimeo
        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)
        return context      

    #DATABASE FIELDS
    intro_header = models.CharField(max_length=50,default="Welcome to our website!")    
    intro_text = RichTextField(blank=True)
    intro_continue_button_text = models.CharField(max_length=50, default='Continue', blank=True)    
    intro_video_id = models.CharField(max_length=50, blank=True, default="")
    video_background_brightness = models.DecimalField(default=1, max_digits=3, decimal_places=2)
    
    client_firstname = models.CharField(max_length=50, default="Joe", blank=True)    
    client_surname = models.CharField(max_length=50, default="Blogs", blank=True)    
    client_organisationName = models.CharField(max_length=50, default="My Company", blank=True)
    client_addressLine1 = models.CharField(max_length=50, default="Line 1",  blank=True)
    client_addressLine2 = models.CharField(max_length=50, default="Line 2",  blank=True)
    client_town = models.CharField(max_length=50, default="Town",  blank=True)
    client_county = models.CharField(max_length=50, default="County",  blank=True)
    client_country = models.CharField(max_length=50, default="Country",  blank=True)
    client_postcode = models.CharField(max_length=50, default="XX00 0XX ",  blank=True)
    client_email = models.CharField(max_length=50, default="joe@bloggs.com" )
    client_phone = models.CharField(max_length=50, default="01234 456789",  blank=True)
    client_phone_availability = models.CharField(max_length=100, default="Mon to Fri 9am to 6pm",  blank=True)
    
    client_moblie = models.CharField(max_length=50, default="01234 456789",  blank=True)    
    
    blurb_header = models.CharField(max_length=50, default="Blurb", blank=True)    
    blurb_subheader = models.CharField(max_length=50, default="this is a blurb", blank=True)
    blurb_text = RichTextField(blank=True)            
    show_blurb = models.BooleanField(default=True)
    
    image_gallery_title = models.CharField(max_length=50, default="Gallery")  
    image_gallery_text = RichTextField(blank=True)
    
    second_blurb_header = models.CharField(max_length=50, default="Blurb 2", blank=True)    
    second_blurb_subheader = models.CharField(max_length=50, default="My Second Blurb 2", blank=True)
    second_blurb_text = RichTextField(blank=True)
    second_blurb_buttonText = models.CharField(max_length=50, default="Find out more", blank=True)
    show_second_blurb = models.BooleanField(default=True)
    
    third_blurb_header = models.CharField(max_length=50, default="Blurb", blank=True)    
    third_blurb_subheader = models.CharField(max_length=50, default="this is a blurb", blank=True)
    third_blurb_text = RichTextField(blank=True)            
    third_show_blurb = models.BooleanField(default=True)
    
    enumerated_list_header = models.CharField(max_length=50, default="Approach", blank=True)
    enumerated_list_text = RichTextField(blank=True)    
    
    icon_list_header = models.CharField(max_length=50, default="Services", blank=True)    
    
    testimonials_header = models.CharField(max_length=50, default="Testimonials", blank=True)
    
    contact_title = models.CharField(max_length=50, default="Contact", blank=True)        
    contact_subtitle = models.CharField(max_length=50, default="Get in contact", blank=True)    
    show_contact_form = models.BooleanField(default=True)

    footer_info_title = models.CharField(max_length=50, default="About", blank=True) 
    footer_info = RichTextField(blank=True)   

    primary_colour = ColorField(default="#f37e77")
    #secondary_colour = models.CharField(max_length=50, default="#ffffff")
    
    blog_title = models.CharField(max_length=50, default="Blogs", blank=True)    
    blog_text = RichTextField(blank=True)
    
    medium_username = models.CharField(max_length=50, null=True, blank=True)
    medium_blog_display_limit = models.IntegerField(blank=True, default=6)

    #DEVELOPER SECTION
    custom_javacript = models.TextField(blank=True)
    custom_css = models.TextField( blank=True)
    custom_html = models.TextField(blank=True)
    

    intro_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    blurb_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    second_blurb_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    third_blurb_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    third_blurb_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )



    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('client_firstname'),
                FieldPanel('client_surname'),
                FieldPanel('client_organisationName'), 
                FieldPanel('client_addressLine1'),  
                FieldPanel('client_addressLine2'),  
                FieldPanel('client_town'),  
                FieldPanel('client_county'),  
                FieldPanel('client_country'),  
                FieldPanel('client_postcode'),  
                FieldPanel('client_email'),          
                FieldPanel('client_phone'),
                FieldPanel('client_moblie'),
                FieldPanel('client_phone_availability'),
                InlinePanel('socialMediaOrderable', label="Social Media Item")

            ],
            heading="Personal Information",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('primary_colour'),
                ImageChooserPanel('logo'),
                ImageChooserPanel('favicon')
            ],
            heading="Presentation",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('intro_header'),
                FieldPanel('intro_text'),
                FieldPanel('intro_continue_button_text'),
                ImageChooserPanel('intro_background'),
                FieldPanel('intro_video_id'),
                FieldPanel('video_background_brightness')
            ],
            heading="Introduction",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('icon_list_header'),                
                InlinePanel('iconListOrderable', label="Panel item")                
            ],
            heading="Panels",  
        ),
    ]    

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('blurb_header'),
                FieldPanel('blurb_subheader'),
                FieldPanel('blurb_text'),
                ImageChooserPanel('blurb_background'),
                FieldPanel('show_blurb'),                
            ],
            heading="Blurb",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('second_blurb_header'),
                FieldPanel('second_blurb_subheader'),
                FieldPanel('second_blurb_text'),                
                ImageChooserPanel('second_blurb_background'),      
                FieldPanel('show_second_blurb'),                
            ],
            heading="Second Blurb",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('third_blurb_header'),
                FieldPanel('third_blurb_subheader'),
                FieldPanel('third_blurb_text'),                
                ImageChooserPanel('third_blurb_image'),                
                ImageChooserPanel('third_blurb_background'),
                FieldPanel('third_show_blurb'),                
            ],
            heading="Third Blurb",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('enumerated_list_header'),    
                FieldPanel('enumerated_list_text'),
                InlinePanel('enumeratedListOrderable', label="Panel Item")                
            ],
            heading="Panel Items",  
        ),
    ]   



    











    # content_panels += [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('image_gallery_title'),
    #             FieldPanel('image_gallery_text'),                
    #             InlinePanel('galleryOrderable', label="Gallery Item"),                
    #         ],
    #         heading="Gallery",  
    #     ),
    # ]   




    # content_panels += [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('testimonials_header'),                
    #             InlinePanel('testimonialOrderable', label="Testimonial Item"),
    #             FieldPanel('show_testimonials_in_navigation')
    #         ],
    #         heading="Icon List",  
    #     ),
    # ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('blog_title'),  
                FieldPanel('blog_text'),                                              
                FieldPanel('medium_username'),   
                FieldPanel('medium_blog_display_limit')
            ],
            heading="Blog",  
        ),
    ]

    # content_panels += [
    #     MultiFieldPanel(
    #         [
    #             FieldPanel('contact_title'),                
    #             FieldPanel('contact_subtitle'),
    #             FieldPanel('show_contact_form'),
    #             FieldPanel('show_contact_in_navigation')
    #         ],
    #         heading="Contact Form",  
    #     ),
    # ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('footer_info_title'),                
                FieldPanel('footer_info')
            ],
            heading="Footer",  
        ),    
    ]

    developer_panels = [
        MultiFieldPanel(
            [
                FieldPanel('custom_javacript'),
                FieldPanel('custom_css'),
                FieldPanel('custom_html')
                                
            ],
            heading="Developer Settings",
        ),
    ]

    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     ImageChooserPanel('intro_background'),
    #     ]  

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            # This is our custom banner_panels. It's just a list, how easy!
            ObjectList(developer_panels, heading="Developer Tools"),
            ObjectList(Page.promote_panels, heading='Promotional'),
            ObjectList(Page.settings_panels, heading='Settings'),
        ]
    )

class BlogIndexPage(Page):
    template = "blog/blog_index_page.html"   

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )

    parent_page_types = ['home.HomePage']
    page_title = models.CharField(max_length=50, default="Features", blank=True) 
    medium_blog_display_limit = models.IntegerField(blank=True, default=6)   

    def get_context(self, request):
        homepage = HomePage.objects.parent_of(self).live().first()
        context = super().get_context(request)
        context['home'] = homepage
        medium_blogs = feedparser.parse(str("https://medium.com/feed/" + homepage.medium_username) if homepage.medium_username else "" )        
        context['medium_blogs'] = medium_blogs.entries[:self.medium_blog_display_limit]
        context['recent_medium_blogs'] = medium_blogs.entries[:4]
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_image'),
                FieldPanel('page_title'), 
                FieldPanel('medium_blog_display_limit')              
            ],
            heading="Page information",  
        ),
    ]

class ContentPage(Page):
    template = "generic/content_page.html"    

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    custom_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_image'),
                FieldPanel('custom_content')              
            ],
            heading="Page information",  
        ),
    ]

class FeaturesPage(Page):
    parent_page_types = ['home.HomePage']
    template = "features/features_page.html"

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    features_blurb_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )    

    intro_content = RichTextField(blank=True)

    features_blurb_header = models.CharField(max_length=50, default="Blurb", blank=True)    
    features_blurb_subheader = models.CharField(max_length=50, default="this is a blurb", blank=True)
    features_blurb_text = RichTextField(blank=True)            
    features_show_blurb = models.BooleanField(default=True)
    
    def get_context(self, request):
        context = super().get_context(request)
        context['home'] = HomePage.objects.parent_of(self).live().first()
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_image'),                           
            ],
            heading="Header",  
        )
    ]
    
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('intro_content'),      
            ],
            heading="Intro",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                InlinePanel('featuresIconListOrderable', label="Panel Item")    
            ],
            heading="Panels",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('features_blurb_header'),
                FieldPanel('features_blurb_subheader'),
                FieldPanel('features_blurb_text'),
                ImageChooserPanel('features_blurb_background'),
                FieldPanel('features_show_blurb'),
            ],
            heading="Blurb",  
        ),
    ]



class PricingPage(Page):
    
    parent_page_types = ['home.HomePage']

    template = "pricing/pricing_page.html"

    intro_content = RichTextField(blank=True)

    question_and_answers_intro = RichTextField(blank=True)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_image')     
            ],
            heading="Header",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('intro_content')
            ],
            heading="Intro",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [                
                InlinePanel('PricingEnumeratedListOrderable', label="Panel item")
            ],
            heading="Pricing panels",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('question_and_answers_intro'),
                InlinePanel('qAOrderable', label="Q&A Item")
            ],
            heading="Q&A",  
        ),
    ]
    

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    template = "contact/form_page.html"
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    
    def get_context(self, request):
        homepage = HomePage.objects.parent_of(self).live().first()
        context = super().get_context(request)
        context['home'] = homepage
        return context


    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('hero_image'),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]