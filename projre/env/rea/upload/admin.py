from django.contrib import admin
from .models import( LandingSummary,LandingCategory,LandingFeatures,LandingAbout
    ,LandingGallery,LandingTestimonials)

admin.site.register(LandingSummary),
admin.site.register(LandingCategory),
admin.site.register(LandingFeatures),
admin.site.register(LandingAbout),
admin.site.register(LandingGallery),
admin.site.register(LandingTestimonials),


