# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)

    uuid = models.UUIDField(default=uuid.uuid4())

    name = models.CharField(max_length=32)

    addr = models.CharField(max_length=32)

    phone = models.IntegerField(default=2)

    def __str__(self):
        return self.name


# 作者查书，设计到作者里面
class Author(models.Model):
    id = models.AutoField(primary_key=True)

    uuid = models.UUIDField(default=uuid.uuid4())

    name = models.CharField(max_length=16)

    author_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)

    # 多对多
    books = models.ManyToManyField(to="Book")

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)

    uuid = models.UUIDField(default=uuid.uuid4())

    title = models.CharField(max_length=6)

    price = models.DecimalField(max_digits=5, decimal_places=2)

    publish_day = models.DateField(auto_now_add=True)

    # 书-出版社 多对一关联
    publisher = models.ForeignKey(to="Publisher", to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)

    uuid = models.UUIDField(default=uuid.uuid4())

    city = models.CharField(max_length=32)

    email = models.EmailField()

    def __str__(self):
        return self.city