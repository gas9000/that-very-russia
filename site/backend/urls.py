"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (
    index,
    news_page,
    team_page,
    partners_page,
    history_lines_page,
    contacts_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('news/', news_page, name='news'),
    path('teams/', team_page, name='teams'),
    path('partners/', partners_page, name='partners'),
    path('history/', history_lines_page, name='history'),
    path('contacts/', contacts_page, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

