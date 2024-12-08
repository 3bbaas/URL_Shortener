import re

import pyshorteners
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.shortcuts import render

from .forms import get_url


def generate_url(request):
    form = get_url(request.POST or None)
    shortened_url = None
    error_message = None

    shortened_url_patterns = [
        r'^https?://(www\.)?tinyurl\.com/.*',
        r'^https?://(www\.)?bit\.ly/.*',
        r'^https?://(www\.)?chilpit\.ly/.*',
        r'^https?://(www\.)?clckru\.ly/.*',
        r'^https?://(www\.)?cuttly\.ly/.*',
        r'^https?://(www\.)?dagd\.ly/.*',
        r'^https?://(www\.)?isgd\.ly/.*',
    ]

    if request.method == "POST":
        long_url = request.POST.get('long_url', '').strip()
        site = request.POST.get('service', '')

        if long_url and site:
            validator = URLValidator()
            try:
                validator(long_url)

                for pattern in shortened_url_patterns:
                    if re.match(pattern, long_url):
                        error_message = f"The provided URL is already shortened with {pattern}."
                        return render(request, 'home.html', {'error_message': error_message})

            except ValidationError:
                error_message = "Invalid URL. Please enter a valid URL."
                return render(request, 'home.html', {'form': form, 'error_message': error_message})

            try:
                if site == "tinyurl":
                    s = pyshorteners.Shortener()
                    shortened_url = s.tinyurl.short(long_url)
                elif site == "bitly":
                    s = pyshorteners.Shortener(api_key='de36c105ae76331609a19ff1ce2d391012d5710a')
                    shortened_url = s.bitly.short(long_url)
                elif site == "chilpit":
                    s = pyshorteners.Shortener()
                    shortened_url = s.chilpit.short(long_url)
                elif site == "clckru":
                    s = pyshorteners.Shortener()
                    shortened_url = s.clckru.short(long_url)
                elif site == "cuttly":
                    s = pyshorteners.Shortener(api_key='3745d515279a2c9396a5144c99c0017ed81b9')
                    shortened_url = s.cuttly.short(long_url)
                elif site == "dagd":
                    s = pyshorteners.Shortener()
                    shortened_url = s.dagd.short(long_url)
                elif site == "isgd":
                    s = pyshorteners.Shortener()
                    shortened_url = s.isgd.short(long_url)
            except pyshorteners.exceptions.ShorteningErrorException as e:
                error_message = "Failed to shorten the URL. Please try again later."

    return render(request, 'home.html', {'form': form, 'shortened_url': shortened_url, 'error_message': error_message})