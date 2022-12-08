from django.urls import re_path as url
from WarchestApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^warchest$',views.warchestApi),
    url(r'^warchest/([0-9]+)$',views.warchestApi),
    url(r'^warchest/savefile',views.SaveFile),
    url(r'^warchest/viewusers',views.viewUsers)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)