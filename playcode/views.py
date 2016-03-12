from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

import requests

# Constants
COMPILE_URL = u"https://api.hackerearth.com/v3/code/compile/"
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

            data = {
                'client_secret': CLIENT_SECRET,
                'async': 0,
                'source': source,
                'lang': lang,
                'time_limit': 5,
                'memory_limit': 262144,
            }

            # Post data to HackerEarth API
            r = requests.post(RUN_URL, data=data)
            # r = requests.post(COMPILE_URL, data=data)
            print(r.json())

            # Returning output data back to browser.
            # It is not possible with Normal submit
            return JsonResponse(r.json(), safe=False)
            # return JsonResponse(data)
    # Get goes here
    return render(request, 'home.html')
