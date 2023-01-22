"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from config import settings
from django.conf.urls import handler404


urlpatterns = [
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pubg-accounts/',include('pubg_account.urls')),
    path('',include('pages.urls')),
    path('captcha/', include('captcha.urls')),
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
handler404 = 'pages.views.error_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)