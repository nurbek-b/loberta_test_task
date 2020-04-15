import json
from .models import Url
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response


def home(request):
    links = Url.objects.all()
    return render(request, 'main_app/home.html', {'links': links})


def on_off_for_check(request, pk):
    if request.method == "POST" and request.is_ajax():
        link = Url.objects.get(pk=request.POST.get('link_id'))
        check = request.POST.get('check')
        if link.check:
            link.check = False
            link.save()
        else:
            link.check = True
            link.save()
        link_data = serializers.serialize('json', [link, ])
        data = json.loads(link_data)
        return JsonResponse(data, safe=False)
