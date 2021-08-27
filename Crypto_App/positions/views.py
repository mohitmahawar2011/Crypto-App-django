from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import Position
# Create your views here.

def home_view(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    # return HttpResponse(data)

    context = {'data': data}

    return render(request, 'positions/main.html', context)


def Search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Position.objects.filter(name__icontains = search)

        context = {'posts': post}
        print(post.name)

        return render(request,'positions/search.html',context)
    