import os

import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views import View

from creator.models import Document
from creator.render import Render


class Home(View):
    template_name = 'creator/home.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {})


class CreateCv(View):
    def post(self, *args, **kwargs):
        nickname = self.request.POST.get('nickname', '')
        url = 'https://bio.torre.co/api/bios/{}'.format(nickname.strip())
        if not nickname:
            return JsonResponse({'message': 'Ingrese un nickname'}, status=202)
        try:
            resp = requests.get(url)
            file = Render.render(nickname, resp)
            data = {
                'nickname': nickname,
                'file': 'cvs/%s' % file[0],
                'url': str(resp.url),
                'ip': get_client_ip(self.request)
            }
            doc = Document.objects.create(**data)
            t = loader.get_template('creator/render.html')
            renderhtml = t.render({'document': doc})
            return JsonResponse({'renderhtml': renderhtml}, status=200)
        except ConnectionError:
            return JsonResponse({'message': 'Error al conectar con el api'}, status=500)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
