"""proving_mail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from message import views as message_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sendmail/$',message_views.sendmail,name='sendmail'),
    url(r'show_result',message_views.show_result,name='result'),
    url(r'change_pwd',message_views.change_pwd,name='change'),
]
