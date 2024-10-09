from django.contrib import admin
from .models import Home, Facility, SliderImage, Events, principal, staffDetails, Photogallery, Videogallery, news, FacilityImage

# Inline for FacilityImage to handle multiple images
class FacilityImageInline(admin.TabularInline):  # You can also use StackedInline
    model = FacilityImage
    extra = 1  # Number of empty image forms to display by default

# FacilityAdmin with inline for images
class FacilityAdmin(admin.ModelAdmin):
    inlines = [FacilityImageInline]

# Register your models
admin.site.register(Home)
admin.site.register(Facility, FacilityAdmin)  # Use the customized admin for Facility
admin.site.register(SliderImage)
admin.site.register(Events)
admin.site.register(principal)
admin.site.register(staffDetails)
admin.site.register(Photogallery)
admin.site.register(Videogallery)
admin.site.register(news)
