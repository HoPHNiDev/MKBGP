from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .telegramm import send_message
from django.http import JsonResponse
import datetime


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@csrf_protect
def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def send_callback_to_telegram(request):
    print(request)
    if request.method == "POST":
        message = f"Имя: {request.POST['name']}\nТелефон: {request.POST['phone']}\nТема: заявка на обрытнай звонок с сайта MKBGP.com\n\n\nName: {request.POST['name']}\nPhone number: {request.POST['phone']}\nTheme: Request for a callback from the website MKBGP.com\n\n{str(datetime.datetime.now()).split('.')[0]}"
        response = {
            'sended': send_message(message)
        }
        return JsonResponse(response)
    # Create your views here.
