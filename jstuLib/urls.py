"""jstuLib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from main import views
# Django路由正则匹配设置
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #主页
    url(r'^$', views.home, name='home'),
    #展示查询结果
    url(r'^show/$', views.show, name='show'),
    #根据图书/论文返回推荐
    url(r'^recommend/$', views.recommend, name='recommend'),
    #反馈
    url(r'^like/$', views.like, name='like'),
]
