from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

import requests
# Constant Variables

# constants
RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
CLIENT_SECRET = 'cd70993ac2dbee9e7c7b2c533a104a7d621632fa'


def home(request):
    if request.method == 'POST':
        # POST goes here . is_ajax is must to capture ajax requests.
        if request.is_ajax():
            # Always use get on request.POST.
            # Correct way of querying a QueryDict.
            lang = request.POST.get('lang')
            source = request.POST.get('source')
            data = {"lang": lang, "source": source}

            # Returning same data back to browser.
            # It is not possible with Normal submit
            print(data)
            return JsonResponse(data)
    # Get goes here
    return render(request, 'home.html')
