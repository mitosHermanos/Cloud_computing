from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Counter


def counter_inc(request):
    print(request)
    counter = Counter.objects.get(id = '1')
    counter.count_num = counter.count_num + 1
    counter.save()
    return HttpResponse(status = 200)