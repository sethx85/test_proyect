"""blockchain_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from views.health import HealthCheck
from views.views import KriptoWallet
from views.render import index

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from django.templatetags.static import static



#favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
favicon_view = RedirectView.as_view(url=static('favicon.ico'))
#RedirectView.as_view(url=staticfiles_storage.url('static/favicon.ico')

urlpatterns = [
    path('admin/', admin.site.urls)
]

#VIEWS.
urlpatterns += [
    path('', index),
    path('health/', HealthCheck.as_view()),
    path('recharge/', KriptoWallet.as_view()),
    path('checkBalance/', KriptoWallet.as_view()),
]

#STATICS.
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
