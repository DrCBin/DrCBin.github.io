---
layout: post
title: "Django学习之进阶-实例与Model,字符串与Model之间的转换"
categories: [Tech]
excerpt: django学习系列笔记
tags:
  - django
---


# 已知实例, 获取Model名字

```python
# 假设已知实例为book, Model
>>> model = book.__class__.__name
'Book'   # 成功获取
```


# 已知Model, 获取Model名字
```python
>>> model = Book.__name__
'Book'   # 成功获取
```


# 已知model名字,获取model
```python
# model名字:'Book', app名字:'app'

# 方法一
>>> from django.apps import apps
>>> model = apps.get_model(app_label='app', model_name='Book')
>>> model
<class 'app.models.Book'>   # 获取成功


# 方法二
>>> from django.contrib.fields import ContentType
>>> content_model = ContentType.objects.get(app_label='app', model='book')   # 一定要小写的model名
>>> model = content_model.model_class()
>>> model
<class 'app.models.Book'>   # 获取成功
```


# 已知model,获取app_label
```python
# model:Book,app名字:app

>>> Book.Meta.app_label
'app'              # 获取成功
```
