---
title: python学习之面向对象--使用@property
category: python
excerpt: |

---


python中允许使用多继承


通常情况下,我们是保留一个主线继承,然后添加一些额外的功能混入继承里面.

```python

# 最基础的Animal类
class Animal:
    print("i'm Animal")

# 细分为哺乳动物类和鸟类
class Mammal(Animal):
    def breed():
        print('胎生...')
class Bird(Animal):
    def breed():
        print('卵生...')


# 还想在分为可飞行和不可飞行
class MammalFlyable(Mammal):
    def fly():
        print("i can fly..")
class MammalRunable(Mammal):
    def fly():
        print("i can run..")
class BirdFlyable(Bird):
    def fly():
        print("i can fly..")
class BirdRunable(Bird):
    def fly():
        print("i can run..")
```


如果在加一些,那么类的定义数量就成倍增长了.

但是如果我们吧`Flyable`和`Runable`单独写成一个类呢.

```python
class Flyable:
    def fly():
        print('i can fly')
class Runable:
    def run():
        print('i can run')


# 然后定义鸟和哺乳动物
class Mammal(Animal, Runable):
    def breed():
        print('胎生...')
class Bird(Animal, Flyable):
    def breed():
        print('卵生...')
```

这样就实现了飞和走的功能，又使得飞和走能重复利用，而不是需要的时候又在定义一遍.

然后我们的继承还是按照动物来说比较合适的分类来继承的,只是**额外添加**了一些次要的功能,这种方式叫做`Mixin:混入`.

有点像java的接口


**继承冲突**:多继承的情况下,可能第一个父类有了某个方法,第二个父类也有这个方法.这时候子类就会出现冲突,到底用哪个方法呢.

答案是:**先继承的哪个父类的**
