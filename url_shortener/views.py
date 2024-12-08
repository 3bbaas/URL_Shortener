import os
import re

import pyshorteners
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.shortcuts import render

BITLY_API_KEY = os.environ.get("BITLY_API_KEY")
CUTLLY_API_KEY = os.environ.get("CUTLLY_API_KEY")


def generate_url(request):
    shortened_url = None
    error_message = None

    shortened_url_patterns = [
        r'^https?://(www\.)?tinyurl\.com/.*',
        r'^https?://(www\.)?bit\.ly/.*',
        r'^https?://(www\.)?chilp\.it/.*',
        r'^https?://(www\.)?clck\.ru/.*',
        r'^https?://(www\.)?cutt\.ly/.*',
        r'^https?://(www\.)?da\.gd/.*',
        r'^https?://(www\.)?is\.gd/.*',
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
                        error_message = "The provided URL is already shortened."
                        return render(request, 'home.html', {'error_message': error_message})

            except ValidationError:
                error_message = "Invalid URL. Please enter a valid URL."
                return render(request, 'home.html', {'error_message': error_message})

            try:
                if site == "tinyurl":
                    s = pyshorteners.Shortener()
                    shortened_url = s.tinyurl.short(long_url)
                elif site == "bitly":
                    s = pyshorteners.Shortener(api_key=BITLY_API_KEY)
                    shortened_url = s.bitly.short(long_url)
                elif site == "chilpit":
                    s = pyshorteners.Shortener()
                    shortened_url = s.chilpit.short(long_url)
                elif site == "clckru":
                    s = pyshorteners.Shortener()
                    shortened_url = s.clckru.short(long_url)
                elif site == "cuttly":
                    s = pyshorteners.Shortener(api_key=CUTLLY_API_KEY)
                    shortened_url = s.cuttly.short(long_url)
                elif site == "dagd":
                    s = pyshorteners.Shortener()
                    shortened_url = s.dagd.short(long_url)
                elif site == "isgd":
                    s = pyshorteners.Shortener()
                    shortened_url = s.isgd.short(long_url)
            except pyshorteners.exceptions.ShorteningErrorException:
                error_message = "Failed to shorten the URL. Please try again later."

    return render(request, 'home.html', {'shortened_url': shortened_url, 'error_message': error_message})
