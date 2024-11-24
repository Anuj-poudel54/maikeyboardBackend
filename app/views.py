
import urllib.parse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import urllib

from django.http import JsonResponse

# Create your v
@csrf_exempt
def translate(request, text, to="mai", from_="en"):

    text = urllib.parse.unquote(text)
    text = urllib.parse.unquote_plus(text)
    res = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={to}&tl={from_}&dt=t&q={text}")
    res = res.json()

    return JsonResponse(res, safe=False)
