---
title: Django学习之进阶--使用自定义表管理ManyToMany关系
category: django
excerpt: |
  django学习系列笔记
---


django中,当我们定义`ManyToMany`关系的时候,会自动创建一张表来管理这个关系,但是自动创建的表非常简单,就只有`id`, `from`,`to`三个字段，更多时候,我们需要更加具体更多的取管理这个关系,就得自定义表.

想想公司和员工之间的关系,一家公司有多个员工,一个员工也可能同时为好几家公司工作.这便是典型的`ManyToMany`关系. 

但是通过上述信息,我们仅仅能知道这个员工在哪几家公司,或者哪家公司有哪些员工.

如果我想问:a员工在A公司的薪水是多少?是啥时候入职的?是什么职务?等等..这些信息.应该定义在哪儿？公司？还是员工？

显然都不是.现实生活中是使用另一个东西来记录的--档案.档案,链接这员工和公司,记录这他们的相关信息.

而这个档案,就是我们需要自定义的表

```python
class Comp(models.Model):
    pass

class Staff(models.Model):
    comp = models.ManyToManyField(Comp, related_name=u'staffs', through='CompStaff', through_fields=('staff','comp')) 
    # 通过through指定关联表
    # through_fields的作用是指定哪两个字段进行关联,如果中介表中只有两个外键,可以不写


class CompStaff(models.Model):
    '''
    用于关联Comp和Staff的表
    '''
    staff = models.ForeignKey(Staff)

    # 注意,下面有两个指向Comp,django不知道选那个作为关联,需要在在ManyToMany关系创建处指定
    last_comp = models.ForeignKey(Comp)
    comp = models.ForeignKey(Comp)

    date_join = models.DateTime()
```
