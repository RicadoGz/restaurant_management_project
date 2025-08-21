from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import RestaurantProfile
from django.shortcuts import render
@api_view(['GET'])
def api_home(request, format=None):
    """
    The entry point for our API.
    """
    # Get the first profile object. If it doesn't exist, create it with the default name.
    # This ensures the site works correctly on the first run.
    #if not have it just creat one 
    profile, created = RestaurantProfile.objects.get_or_create(pk=1)

    return Response({
        'restaurant_name': profile.name,
       
    })

def api_about(request, format=None):
    """
    The about page for our API.
    """
    profile, created = RestaurantProfile.objects.get_or_create(pk=1)
    return render(request, 'home/about.html',  {'profile': profile})
