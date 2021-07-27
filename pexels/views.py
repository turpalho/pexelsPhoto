from django.http import HttpResponse
from django.shortcuts import render
from pexels_api import API



def index(request):
    resultPhotos = GetPexelsPhotos()
    return render(request, 'pexels/index.html', {'photos' : resultPhotos})

def GetPexelsPhotos():
    PEXELS_API_KEY = '563492ad6f917000010000010b3e3bada02a4f9cbc6e436a30e26c0f'
    api = API(PEXELS_API_KEY)
    # Search five 'kitten' photos
    #api.search('kitten', page=1, results_per_page=50)
    api.popular(page=1, results_per_page=300)

    # Get photo entries
    photos = api.get_entries()
    return photos