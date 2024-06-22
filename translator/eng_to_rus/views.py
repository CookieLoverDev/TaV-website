from django.shortcuts import render, redirect
from translate import Translator
from .models import Video, Premium_video
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)
        

def main(request):
    return render(request, 'main.html')

#Cтраница с переводчиком с англ
def english(request):
    return render(request, 'english.html')

#вызов функции для перевода с англ и вызов страницы с переводом
def translate(request):
    word = request.GET.get('word')
    translator = Translator(to_lang='ru', from_lang='eng')
    translation = translator.translate(word)
    context = {
        'translation':translation
    }
    return render(request, 'translation.html', context)

#Вывод страницы со всеми доступными языками
def other_lang(request):
    return render(request, 'other-languages.html')

#Вывод страницы с переводчиком с немецкого
def german(request):
    return render(request, 'german.html')

#Функция для перевода с немецкого и страницы перевода
def german_trs(request):
    word = request.GET.get('word')
    translator = Translator(to_lang='ru', from_lang='GERMAN')
    translation = translator.translate(word)
    context = {
        'translation':translation
    }
    return render(request, 'translation.html', context)

#Вывод страницы с переводчиком с испанского
def espanol(request):
    return render(request, 'espanol.html')

#Функция для перевода с испанского и страницы перевода
def esp_trs(request):
    word = request.GET.get('word')
    translator = Translator(to_lang='ru', from_lang='SPANISH')
    translation = translator.translate(word)
    context = {
        'translation':translation
    }
    return render(request, 'translation.html', context)

def tutorials_page(request):
    return render(request, 'tutorials_page.html')

def tutorials(request):
    videos = Video.objects.all()
    context = {
        'videos':videos
    }
    return render(request, 'tutorials_logic.html', context)

@login_required(login_url='login')
def pre_tutorials(request):
    videos = Premium_video.objects.all()
    context = {
        'videos':videos
    }
    return render(request, 'pre_tutorials_logic.html', context)