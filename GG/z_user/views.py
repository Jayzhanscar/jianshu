# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.http import HttpResponse
from django.shortcuts import render
from model.user.login import UserInfo
from hashlib import sha1
from django.template.loader import get_template
from django.template import Context
import json
from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response
from ContentApp.models import Blog
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from conf import common
from ContentApp.models import Blog, Expert, Remark, AttentionTable
from django.utils.encoding import smart_str
# from conf.get_name import write_to_cache, read_from_cache
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# import urllib.parse
from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def relogin(request):
    return render(request, 'user/login.html', )


@csrf_exempt
def info(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        # print(action == 'Refresh', action)
        if str(action) == 'Refresh':
            # count = [x for x in range(5)]
            # print(count)
            # print(random.randint(0, 6))
            count = random.randint(0, 6)
            count1 = count + 6
            obj = Expert.objects.all()[count:count1]
            list_export = []
            # for i in obj:
                # print(i.name, i.img, i.introduce)
            # print(type(list_export))
            # 对象转为列表数据返回
            data_list = obj[:]
            for i in data_list:
                list_export.append({'id': i.id, 'name': i.name, 'img': i.img, 'introduce': i.introduce[0:10]})
                # print(i.name, 'ppp')
            # print(list_export)
            return HttpResponse(json.dumps(list_export), content_type="application/json")
        if str(action) == 'getmore':
            pk = request.POST.get('pk', None)
            print(type(pk))
            if pk:
                pk = int(pk) + int(1)
                pk1 = pk + 5
                obj = Blog.objects.all()[pk:pk1]
                blog_list = []
                for i in obj:
                    print(i.title, i.user_id, i.type,  i.create_date)
                    U = UserInfo.objects.filter(id=i.user_id)
                    if U:
                        for j in U:
                            print(j.userName)
                            blog_list.append(
                                {'id': i.user_id, 'title': i.title, 'type': i.type, 'views': i.views, 'talk_count':
                                    i.talk_count, 'like_count': i.like_count, 'author': j.userName, 'pk': int(pk),
                                 'content': i.tagline[0:100], 'pic': j.img.name, 'create_date': str(i.create_date)})
                print(type(blog_list), '----', blog_list)
                if len(blog_list) < 1:
                    return HttpResponse('all')
                return HttpResponse(json.dumps(blog_list), content_type="application/json")
            else:
                return HttpResponse('500')
    elif request.method == 'GET':
        userid = request.COOKIES.get('user_id')
        p = UserInfo.objects.filter(Account=userid)
        articles = Blog.objects.all().order_by('-views')[0:15]
        experts = Expert.objects.all()[0:5]
        return render(request, 'user/index.html', locals())
# 注册账号时采用post请求


# 发表页面
@csrf_exempt
def publish(request):
    user = request.COOKIES["user_id"]
    if user:
        try:
            count = Blog.objects.filter(author=user).count()
            p = UserInfo.objects.filter(Account=user)
        except:
            print('获取失败')

    return render(request,'content/publish.html',locals())


# 用户中心
@csrf_exempt
def user_center(request):
    userid = request.COOKIES.get('user_id')
    if request.method == 'POST':
        try:
            my_img = UserInfo.objects.get(Account=userid)
            my_img.img = request.FILES.get('img')
            my_img.imgname = request.FILES.get('img').name
            my_img.save()
        except Exception as e:
            print('保存错误', e)
        return render(request, 'user/usercenter.html')
    p = UserInfo.objects.filter(Account=userid)
    for i in p:
        img_name = i.img.url
    if userid:
        articles = Blog.objects.filter(author=userid)
        obj1 = AttentionTable.objects.filter(Concern=userid)
        print(obj1)
        for i in obj1:
            print(i)
    if not userid:
        return HttpResponseRedirect('/user/relogin')
    return render(request, 'user/usercenter.html', locals())


@csrf_exempt
def register(request):
    username = request.POST.get('name')
    userpwd = request.POST.get('pwd')
    userpwd1 = request.POST.get('pwd1')
    useremail = request.POST.get('email')
    # 判断两次密码
    if userpwd != userpwd1:
        print('密码不一致')
        return HttpResponse('8')
    # 判断用户名是否重复
    else:
        try:
            users = UserInfo.objects.filter(Account=useremail)
            if users:
                print('用户已存在')
                return HttpResponse('7')
            else:
                userpassword = make_password(userpwd, None, 'pbkdf2_sha256')
                # 创建数据表对象
                # 创建对象
                print('我要开始保存了')
                try:
                    user = UserInfo()
                    user.userName = username
                    user.userPwd = userpassword
                    user.Account = useremail
                    user.save()
                    print('我已经保存好了')
                    return HttpResponse(common.USER_SUCCEED)
                except Exception as e:
                    print("error:", e)
        except Exception as e:
            print(e)


# 验证账号 post请求
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        userpwd = request.POST.get('pwd')
        try:
            users_name = UserInfo.objects.filter(Account=username)
            if users_name:
                boolpwd = check_password(userpwd, users_name[0].userPwd)
                if boolpwd:
                    User = UserInfo.objects.get(Account=username)
                    resp = {'data': 1}
                    response = HttpResponse(json.dumps(resp), content_type="application/json")
                    response.set_cookie('user_id', User.Account, 36000)
                    # cooike 保存用户ID
                    response.set_cookie('UID', User.id, 36000)
                    # 把用户名写到redis缓存里面去
                    # write_to_cache(username)
                    return response
                else:
                    back_data = {'data': 'no user'}
                    return HttpResponse(back_data, content_type="application/json")
            else:
                back_data = {'data': 'request faild'}
                return HttpResponse(back_data, content_type="application/json")
        except Exception as e:
            print(e)


# 修改用户信息
@csrf_exempt
def edit_user(request):
    if request.method == "POST":
        userid = request.POST.get('user_id')
        user_name = request.POST.get('name')
        qianm = request.POST.get('qianming')
        qq = request.POST.get('qq')
        if user_name:
            try:
                u = UserInfo.objects.get(userName=userid)
                u.userName = user_name
                u.qianming = qianm
                u.qq = qq
                u.save()
                response = HttpResponse(user_name)
                response.set_cookie('user_id', user_name)
                return response
            except:
                print('保存错误')
                return HttpResponse('error')
        else:
            return HttpResponse('no name')
