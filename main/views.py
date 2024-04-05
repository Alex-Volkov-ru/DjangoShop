from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

    

def index(request):
    
    categories = Categories.objects.all()

    context = {
        'title' : 'Home - Главная',
        'content': 'Магазин мебели Козий Хоум',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title' : 'Home - Добро пожаловать в наш мебельный магазин! У нас вы найдете широкий выбор качественной мебели для всех помещений вашего дома. Наш ассортимент включает в себя современные диваны, стильные кровати, удобные столы и многое другое. Мы гарантируем высокое качество продукции и индивидуальный подход к каждому клиенту. Посетите нас и преобразите свой дом с нами!',
        'content': 'О нас',
        'text_on_page': 'Наш мебельный магазин отличается не только разнообразием товаров, но и превосходным сервисом. Мы ценим каждого клиента и стремимся сделать его покупки максимально комфортными. У нас вы найдете не только мебель, но и аксессуары для интерьера, которые помогут создать уютную атмосферу в вашем доме. Посетите наш магазин и убедитесь сами в его высоком уровне обслуживания!'
    }
    return render(request,'main/about.html', context)