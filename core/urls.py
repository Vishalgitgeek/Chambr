from django.urls import path
# from .views import home, room_detail
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view = views.home, name='home'),
    path('room/<str:room_name>/', view = views.room_detail, name='room_detail'),
    path('create_room/', view = views.create_room, name='create_room'),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)