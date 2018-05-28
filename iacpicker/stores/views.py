from django.shortcuts import render
from django.http import HttpResponse

from .models import Store

# Create your views here.
def index(request):

    store = Store.objects.random()

    context = {
        'store' : store
    }

    return render(request, 'stores/index.html', context)