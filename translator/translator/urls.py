from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eng_to_rus.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
