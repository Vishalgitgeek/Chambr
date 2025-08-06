from django.urls import path
from .views import home, room_detail

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)