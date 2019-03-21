# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Images

@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = Images(
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/upload_img.html')


@csrf_exempt
def showImg(request):
    imgs = Images.objects.all()
    content = {
        'imgs': imgs,
    }
    for i in imgs:
        print i.img.url
    return render(request, 'img_tem/show_img.html', content)

# Create your views here.
