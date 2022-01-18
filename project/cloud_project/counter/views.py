from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Counter


def counter_inc(request):

    counter, created = Counter.objects.get_or_create(id = '1')
    if created:
        counter.count_num = counter.count_num + 1
        # created.save()
    else:
        counter.count_num = counter.count_num + 1
    counter.save()
    return HttpResponse(status = 200, content = counter.count_num)