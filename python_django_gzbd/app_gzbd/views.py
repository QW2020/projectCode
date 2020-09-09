#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
gzbd app views
'''

from django.core import serializers
from common.result import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from app_gzbd.models import *
import random,datetime,json

# Create your views here.
'''
http://127.0.0.1:8080/helloWorld/ ---- get
'''
def hello_world(request):
    # 插入数据
    user = User(user_name="qw" + str(random.randint(1, 10)), password="111",
                      create_date=datetime.datetime.now());
    # user.save();
    # users = User.objects.all()
    # print("==== 查询所有 ====", users)

    users = User.objects.filter(id=1)
    print("==== 条件查询 ====", type(users))

    # user = User.objects.get(id=1)
    # print("==== 获取单个对象 ====", user)

    # 更新数据
    # user.user_name = "hymanqin" + str(random.randint(1, 10))
    # user.save()

    # users = serializers.serialize("json", User.objects.order_by("user_name")[0:2])
    # print("==== 排序&limit ====" + users)

    user_json = serializers.serialize("json", [users])
    print("==== 序列化 ====")

    # return HttpResponse("Hello World");
    return JsonResponse(json.loads(user_json), safe=False);

'''
http://127.0.0.1:8080/test/index/ ---- get
'''
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

'''
http://127.0.0.1:8080/index/ ---- get
'''
def index(request):
    context = {};
    return render(request, "index.html", context);

'''
http://127.0.0.1:8080/indexSimple/ ---- get
'''
def index_simple(request):
    context = {};
    return render(request, "indexSimple.html", context);

'''
http://127.0.0.1:8080/dashBoardPage/ ---- get
'''
def dashboard_page(request):
    context = {};
    return render(request, "common/dashBoard.html", context);

'''
http://127.0.0.1:8080/login/ ---- get
'''
def login(request):
    context = {};
    return render(request, "account/login.html", context);

'''
http://127.0.0.1:8080/register/ ---- get
'''
def register(request):
    context = {};
    return render(request, "account/register.html", context);

'''
查询、删除
http://127.0.0.1:8080/user/1  --- get、delete
'''
def user(request,id):
    if request.method == "GET":
        user = User.objects.get(id=id);
        user_result = {};
        user_result["id"] = user.id;
        user_result["user_name"] = user.user_name;
        user_result["password"] = user.password;
        user_result["create_date"] = user.create_date;
        return JsonResponse(user_result, safe=False);
    elif request.method == "DELETE":
        User.objects.filter(id=id).delete();
        return JsonResponse(Result(status=200,message="delete success.").result(),safe=False);
    else:
        return JsonResponse(Result(status=500,message="No operation for user").result(),safe=False);

'''
http://127.0.0.1:8080/users?userName=qw&password=111  --- get
http://127.0.0.1:8080/users  --- post
{"user_name":"qw5","password":111}
http://127.0.0.1:8080/users  --- put
{"id":"1","user_name":"hyman","password":"111"}
'''
def users(request):
    if request.method == "GET":
        user_name = request.GET.get("userName");
        password = request.GET.get("password");
        user = User.objects.filter(user_name=user_name, password=password).first();
        print(user,user_name,password)
        if user:
            # user_result = {};
            # user_result["id"] = user.id;
            # user_result["user_name"] = user.user_name;
            # user_result["password"] = user.password;
            # user_result["create_date"] = user.create_date;
            return JsonResponse(Result(status=200,message="login success.").result(), safe=False);
        else:
            return JsonResponse(Result(status=500, message="No user find").result(), safe=False);
    elif request.method == "POST":
        # 获取查询参数、form表单参数
        # user_name = request.POST.get("userName")
        # password = request.POST.get("password")
        # 获取 json 数据
        query = json.loads(request.body);
        user_name = query.get("userName");
        password = query.get("password");
        user = User(user_name=user_name,password=password,create_date=datetime.datetime.now());
        user.save();
        return JsonResponse(Result(status=200, message="Insert success").result(), safe=False);
    elif request.method == "PUT":
        # 获取 json 数据
        query = json.loads(request.body);
        user_name = query.get("userName");
        password = query.get("password");
        user = User.objects.get(id=id);
        user.user_name = user_name;
        user.save();
        return JsonResponse(Result(status=200, message="Update success").result(), safe=False);
    else:
        return JsonResponse({"status": 200, "message": "No opration for user"}, safe=False);

'''
http://127.0.0.1:8080/gzbd
'''
def gzbd(request):
    gzbds = Epidemic.objects.all()[0:7];
    gzbd_list = [];
    for item in gzbds:
        epidemic = {};
        epidemic["id"] = item.id;
        epidemic["region"] = item.region;
        epidemic["date"] = item.date;
        epidemic["diagnosis"] = item.diagnosis;
        epidemic["overseas_import"] = item.overseas_import;
        epidemic["cure"] = item.cure;
        epidemic["death"] = item.death;
        gzbd_list.append(epidemic)
    return JsonResponse(gzbd_list,safe=False);
