---
layout: post
title: "python学习之基础--生成器和迭代器"
categories: [Tech]
excerpt: python学习系列笔记！
tags:
  - python
---


# 列表生成式 #

有时候，我们需要生成一个具有某种规律的列表,如`[1,2,3,4,5,6,7,8,9]`,或者`[2,4,6,8,10]`等.列表里面的值都是可以通过一个表达式得到的.

```python
L1 = [x for x in range(1,10)]

L2 = [x for x in range(1, 20) if x%2 == 0]

L3 = [x*2 for x in range(1,5)]
```

简单来说语法是这样的:`[值 值生成方式]`, 其中值的生成方式可以有很多，比如来自别的列表等，值的过滤方法也很多，可以进行if判断等各种


# 生成器(generator) #

上述的列表生成式已经可以帮我们做很多事情了，但是如果生成列表量很大，生成的算法有特别复杂的话，势必会浪费很多资源.基于这个原因，如果出一种可以不一开始就生成值，而只是将生成值的方法记录下来，当需要值的时候再去计算，就会使得资源能有效利用.这就是**生成器** .

构造生成器的方法:

- 将列表生成式的`[]`换成`()`即可.
- 在函数中使用`yield`关键字.

```python
# 使用()生成
L1 = (x*2 for x in range(1,10))
for x in L1:
    print(x)


# 使用yield生成
# 定义
def L(max=10):
    for x in range(1, max):
        yield x*2

# 使用,生成两个生成器
L1 = L(20)

L2 = L(30)

# 迭代生成器

for x in L1:
    print(x)
```

除了使用for循环迭代，还有一种不常用的`next()`迭代

```python
>>> L1 = L(2)

>>> next(L1)
2

>>> next(L1)
4

>>> next(L1)
%(*&%( 报错
```
L1只有两个项, 再调用next迭代的话就会报错.

# 迭代器和可迭代对象 #

可以被`for`迭代的这类对象统称为可迭代对象:`Iterable`

可以被`next()`调用并不断返回一个值的对象叫做迭代器:`Iterator`

生成器都是`Iterator`对象.

`Iterable`对象的判断
```python
from collections import Iterator
l = []
isinstance(l, Iterator)
```

将一个`Iterable`转换成`Iterator`:使用`iter()`函数
```python
iter([1,2,3])
```

为什么有的可以是迭代器， 有的却只能是可迭代对象

list等可迭代对象都有一个共同特征，他们的值已经是固定了的。而可迭代兑现的值计算是惰性的，当使用的时候才会去计算.二一个`list`,`str`等他们的值必须是固定的，而不能等待需要使用的时候再去计算，这便是阻止他们成为迭代器的原因.
