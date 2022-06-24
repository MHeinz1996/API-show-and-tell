from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

pp = pprint.PrettyPrinter(indent=2, depth=2)

# Create your views here.
def index(request):
    return render(request, "show_and_tell/index.html")

def colorizer(request):
    
    if request.GET.get('img'):
        img_url = request.GET.get('img')
    else:
        # Generates a random pokemon if they input an invalid ID
        img_url = 'https://images.unsplash.com/photo-1564566800380-aa5a49acb065?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80'   
    
    response = HTTP_Client.post(
        "https://api.deepai.org/api/colorizer",
         data={
        'image': img_url
        },
        headers={'api-key': os.environ['api-key']}
    )
    output = response.json()
    print(output['output_url'])
    return render(request, 'show_and_tell/colorized.html', {'output': output})

def text_to_img(request):

    if request.GET.get('text'):
        word = request.GET.get('text')
    else:
        # Generates a random pokemon if they input an invalid ID
        word = 'dog'
    
    response = HTTP_Client.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': word,
        },
        headers={'api-key': os.environ['api-key']}
    )
    output = response.json()
    print(output['output_url'])
    return render(request, 'show_and_tell/text_to_img.html', {'output': output})