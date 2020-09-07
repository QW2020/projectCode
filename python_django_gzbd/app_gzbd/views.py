#!/user/bin/env python3
# -*- coding: utf-8 -*-
from django.core import serializers

__author__ = "HymanQin";

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_gzbd.models import User
import random,datetime,json

# Create your views here.
def hello_world(request):
    # 插入数据
    user = User(user_name="qw" + str(random.randint(1, 10)), password="111",
                      create_date=datetime.datetime.now());
    # user.save();
    users = User.objects.all()
    print("==== 查询所有 ====", users)

    # users = User.objects.filter(id=1)
    # print("==== 条件查询 ====", users)

    # user = User.objects.get(id=1)
    # print("==== 获取单个对象 ====", user)

    # 更新数据
    # user.user_name = "hymanqin" + str(random.randint(1, 10))
    # user.save()

    # users = serializers.serialize("json", User.objects.order_by("user_name")[0:2])
    # print("==== 排序&limit ====" + users)

    user_json = serializers.serialize("json", users)
    print("==== 序列化 ====")

    # return HttpResponse("Hello World");
    return JsonResponse(json.loads(user_json), safe=False);

def test_index_page(request):
    context = {};
    context["name"] = "qw";
    context["name_list"] = ["qw1","qw2"];
    context["number"] = 1024;
    context["birthday"] = datetime.datetime.now();
    context["person"] = {"name":"qw","age":24};
    context["person1"] = {"name":"Qw1","age":24};
    context["url"] = "http://www.baidu.com"
    context["a"] = "<a href='http://www.baidu.com'>点击2</a>"
    context["isman"] = True
    context["age"] = 24
    return render(request, "test/index.html", context);

def index(request):
    context = {};
    return render(request, "index.html", context);

def index_simple(request):
    context = {};
    return render(request, "indexSimple.html", context);

def dashboard_page(request):
    context = {};
    return render(request, "common/dashBoard.html", context);

def login(request):
    context = {};
    return render(request, "account/login.html", context);

def register(request):
    context = {};
    return render(request, "account/register.html", context);