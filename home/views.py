from django.shortcuts import render, get_object_or_404
from .models import Home, Facility, SliderImage,Events,principal,staffDetails,Photogallery,news,Videogallery# Include SliderImage

def index(request):
    context = {
        'home': Home.objects.all(),
        'facility': Facility.objects.all(),
        'slider_images': SliderImage.objects.all(),
        'Events': Events.objects.all(), 
        'news': news.objects.all(), 
        'facility_images': {facility: facility.images.all() for facility in Facility.objects.all()},  # Map facilities to their images
    }
    return render(request, "index.html", context)

def facility_detail(request, id):
    facility = get_object_or_404(Facility, id=id)
    # Fetch the related images for the facility
    images = facility.images.all()  # Assuming related_name='images' in the ForeignKey
    return render(request, 'facility_detail.html', {'facility': facility, 'images': images})

def about(request):
    context = {
     'principal':principal.objects.all(),
     'staffDetails':staffDetails.objects.all()
     }
    return render(request, 'Aboutus.html',context)

def Academics(request):
    context = {
        'Photogallery':Photogallery.objects.all()
    }
    return render(request, 'Academics.html',context)

def Admission(request):
    context = {
        'Videogallery':Videogallery.objects.all(),
        'Photogallery':Photogallery.objects.all()
    }
    return render(request, 'Admission.html',context)

def Program(request):
    return render(request, 'program.html')

def Deafblind(request):
    return render(request, 'Deafblind.html')
