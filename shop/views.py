from django.shortcuts import render, get_object_or_404
from .models import Dish

def index(request):
    dishes = Dish.objects.all()  # Dish 테이블의 모든 레코드 조회

    context = {
        'dishes': dishes
    }
    return render(request, 'index.html', context)
# Create your views here.


def detail(request,id):
    dish = get_object_or_404(Dish, id=id)
    return render(request, 'detail.html', {'dish': dish})


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def team(request):
    return render(request, 'team.html')