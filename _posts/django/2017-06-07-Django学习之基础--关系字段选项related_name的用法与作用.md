---
layout: post
title: "Django学习之基础--关系字段选项`related_name`的用法于作用"
categories: [Tech]
excerpt: django学习系列笔记
tags:
  - django
---


关系字段选项:`related_name`,只能作用于关系字段`ForeignKeyField`和`ManyToManField`.

作用:当`一个模型`使用关系字段去关联`另一个模型`时,其中`一个模型`为主动关联的模型,`另一个模型`为被动关联的模型.很自然的能从主动模型中查寻到关联了哪个模型.但是为了能从被关联模型中追溯有那些模型关联了他,这就是`related_name`的作用.从被关联模型中反向追溯主动关联他的模型

不想反向追溯: 如果你的模型没有反向追溯的必要,你也可以不要反向追溯,只需设置值以`+`结尾就行:`related_name='+'`

不添加这个字段选项: 如果你没有手动添加这个字段选项,那么被关联对象会自动以`主动关联模型名字_set`的形式设置值

### 基础用法

用法: 添加字段选项`related_name='name'`.


调用: 在被关联对象中调用`ModelName.name`即可反向追溯.

eg:

```python
from django.db import models

class Auth(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    name = models.CharField(max_length=100)
    auth = models.ForeignKeyField(Auth, related_name='books')  # Auth.books便课反向追溯到它本人有哪些书

>>> a = Auth(name='chenbin')

>>> b1 = Book(anme='book1', auth=a)
>>> b1 = Book(anme='book2', auth=a) # 写法不对,重在表达意思
>>> a.books  # 反向追溯有那些书

['book1', 'book2']
```


### 进阶用法

基于上面的基础用法,我们可以知道,其实`related_name`的作用可以说是给被关联的那个model添加一个隐式的字段或者说是属性.

现在我们考虑一个模型,叫做`BaseModel`

```python
class Auth(models.Model):
    pass

class BaseModel(models.Model):
    auth = models.ForeignKeyFields(Auth, related_name='works')  # 作者的作品叫做works

class Book(BaseModel):
    '''
    作品的一种:书

    '''
    pass

class Music(BaseModel):
    '''
    另一种作品:音乐
    '''
    pass


>>> a = Auth()
>>> b = Book(auth=a)
>>> m = Music(auth=a)

>>> a.works
???     # 计算机怎么知道给啥呢？

```

鉴于上面的情况,所以我们需要动态的根据不同的类来改变`related_name`的值

有两个变量需要用`%(app_label)`和`%(class)`.

`app_label`:每个应用安装都会有唯一的应用名称,这个变量代表的就是应用名称

`class`: 可以为每个类设置一个类名,这个变量代表类名

用法:`related_name=xxx%(app_labels)sxxx%(class)sxxx`, 可以任意组合,`)`后面的s代表小写的意思

这样就能保证每个`related_name`的值是唯一的了
