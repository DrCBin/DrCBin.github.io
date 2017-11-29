---
layout: post
title: "Django学习之进阶--多表Model继承时的名字冲突"
categories: [Tech]
excerpt: django学习系列笔记
tags:
  - django
---


django的model多继承时,父类会有子类的model名的小写作为字段.

```python
from django.db import models

class Animal(models.Model):
    pass

class
```
