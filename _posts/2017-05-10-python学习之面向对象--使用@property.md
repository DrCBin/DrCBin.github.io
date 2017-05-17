---
title: python学习之面向对象--使用@property
category: python
excerpt: |
    python学习系列笔记！
---

通常情况,我们封装属性是为了能更好的限制属性不被任意修改.

```python
class Student:
    score = 0


>>> stu = Student()
>>> stu.score = 999   # 显然，成绩这么高不太符合逻辑
```

所以我们要对score进行赋值的限制,通常,我们使用函数来进行过滤,并且把需要保护的数据设为私有的

```python
class Student:
    __score__ = 0
    def set_score(self, score):
        if score > 100 or score < 0:
            raise TypeError
        self.__score__ = score
```

这样,当我们想给属性设置值的时候,只能通过调用方法,从而保证数据的安全和有效

但随之而来的另一个问题,我们想访问的时候也只能通过方法了.所以，上面的类还要添加一个方法

```python
class Student:
    ...
    def get_score():
        return self.__score__
```

然后我们使用的时候就通过调用函数使用. 但是这样好麻烦,能像访问public属性那样访问私有属性，又能做到函数的过滤，那不是好? 所以, `@property`来了.

这样改:

```python
class Student:
    __score__ = 0

    @property
    def score(self):
        return self.__score__

    @score.setter
    def score(self, value):
        if score > 100 or score < 0:
            raise TypeError
        self.__score__ = value

>>> stu = Student()
>>> stu.score
0
>>> stu.score = 999
TypeError
>>> stu.score = 99
>>> stu.score
99
```

恩，好了，方便多了

`@property`把`score`方法变成了可以直接读的舒心, 然后`score.setter`又可以把另一个方法变成可以设置值的属性.
