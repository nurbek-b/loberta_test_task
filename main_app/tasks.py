import json
import requests
from .models import Url
from django.core import serializers
from django.http import JsonResponse
from url_status_checker.celery import app


@app.task
def check_url_status():
    for link in Url.objects.filter(check=True):
        try:
            link.status = requests.get(link.url).status_code
            link.save()
            link_data = serializers.serialize('json', [link, ])
            data = json.loads(link_data)
            print(data)
            return JsonResponse(data, safe=False)
        except:
            return None
