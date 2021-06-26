from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Sentence


def sentences(request):
    return HttpResponse(
        serialize('json', Sentence.objects.all()[:10]),
        content_type='application/json')
