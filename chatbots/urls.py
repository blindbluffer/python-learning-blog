from django.contrib import admin
from django.urls import path

from chatbots.views import home, get_response

from django.conf.urls.static import static
from django.conf import settings

app_name = 'chatbots'

urlpatterns = [
    path('', home,name='chatbot'),
    path('get-response/', get_response),
]

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
