from django.urls import path
from django.conf.urls import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', SubtaskView.as_view(), name='Home'),

              ] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)