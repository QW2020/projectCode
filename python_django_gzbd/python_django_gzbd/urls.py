#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
函数作为参数传递，不加括号，相当于绑定事件，事件触发再执行
path路径末尾带/，Django中设置了APPEND_SLASH=True, 当URL后面缺少斜杠时，会自动拼上斜杠，并重定向
'''

from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from app_gzbd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'helloWorld/',views.hello_world),
    # url(r'^test/index$', views.test_index),
    path('test/index/', views.test_index_page),
    path(r'index/',views.index),
    path(r'indexSimple/',views.index_simple),

    # --- user ---
    path(r'login/',views.login),
    path(r'register/',views.register),
    re_path(r'^user/(\d+)$',views.user),
    re_path(r'^users$',views.users),

    # --- gzbd ---
    path(r'gzbd/',views.gzbd),

    # --- common ---
    path(r'dashBoardPage/',views.dashboard_page),
]
