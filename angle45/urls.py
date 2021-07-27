from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from pexels.views import index

urlpatterns = [
    path('', TemplateView.as_view(template_name="account/login.html")),
    path('photos/', index),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
