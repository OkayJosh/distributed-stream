import json
from django.core import serializers
from django.views.generic.base import TemplateView
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import PriceIndex
from asgiref.sync import sync_to_async

class IndexView(TemplateView):
    template_name = "index.html"

@sync_to_async
def return_all_price():
    # queryset = PriceIndex.objects.filter(name__filter="Maize").values()
    # data = json.dumps(json.loads(serializers.serialize("json",PriceIndex.objects.filter(name__lte="Maize").values())))
    data = json.dumps(list(PriceIndex.objects.filter(name__lte="Maize").values()))
    # data = json.dumps(json.loads(PriceIndex.objects.all()))
    return json.loads(data)

async def websocket_view(socket):
    await socket.accept()
    # await socket.send_json(json.dumps(json.loads(serializers.serialize("json",PriceIndex.objects.all()))))
    for fields in await return_all_price():
        await socket.send_json(fields)
    await socket.close()