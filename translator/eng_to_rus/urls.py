from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('', views.main, name='main'),
    path('english', views.english, name='english'),
    path('translation', views.translate, name='translation'),
    path('other-languages', views.other_lang, name='other-lang'),
    path('german', views.german, name='german'),
    path('deu-trs', views.german_trs, name='deu-trs'),
    path('espanol', views.espanol, name='espanol'),
    path('esp-trs', views.esp_trs, name='esp-trs'),
    path('tutorials', views.tutorials_page, name='tuts'),
    path('lang-tutorials', views.tutorials, name='tutorials'),
    path('pre-tutorials', views.pre_tutorials, name='pre-tutorials')
]
