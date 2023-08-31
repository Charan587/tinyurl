import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ShortenedURL

def home(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_key = generate_short_key()
        short_url = f"http://127.0.0.1:8000/{short_key}/"
        ShortenedURL.objects.create(long_url=long_url, short_key=short_key)
        return JsonResponse({'short_key': short_key})
    return render(request, 'home.html')

def generate_short_key():
    characters = string.ascii_letters + string.digits
    short_key = ''.join(random.choice(characters) for _ in range(6))
    return short_key

def redirect_original(request, short_key):
    url_object = get_object_or_404(ShortenedURL, short_key=short_key)
    return redirect(url_object.long_url)
