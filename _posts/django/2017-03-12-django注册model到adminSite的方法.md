---
layout: post
title: "django中ModelAdmin.actions用法总结"
categories: [Tech]
excerpt: ModelAdmin.actions的用法总结
tags:
  - django
---


## Model的注册
如果我们在models.py中创建了模型，但是admin site并不知道我们的这个模型，所以我们需要告诉admin site ，以显示这个模型．这就是注册．
将一个model注册到admin site 提供了三种方法:
1. 直接注册:
```
admin.site.register(ModelName)
```
2. 使用ModelAdmin注册:
```
class ModelAdminNamea(dmin.ModelAdmin):
	pass
admin.site.register(ModelAdminName, modelName)
```
这中方法可以通过ModelAdminName类来添加一下对Model的约束或管理
3. 使用装饰器注册：
```
@admin.register(ModelName)
class ModelAdminName(admin.ModelAdmin):
	pass

```

## ModelAdmin的选项和用法
```class Meta```类提供了一个模型的内部的约束和行为管理，其功能只能是对具体的模型进行具体的管理，有点类似于模型的自我管理．而```class ModelAdmin```提供的是模型外部的管理，管理的是一群模型的实例．主要管理的是Model在admin site中的表现行为.

#### ModelAdmin的可用选项
` ModelAdmin.action `:其值为一个列表，列表内容是响应的函数，作用是定义在admin site中选择多个model实例是，可用的操作．通俗说就是批量处理的行为．具体见[这里](http://single-thread.me/django/2017/03/12/django%E4%B8%ADModelAdmin.action%E7%9A%84%E7%94%A8%E6%B3%95%E6%80%BB%E7%BB%93/)

` ModelAdmin.action_on_top/bottom `:值为布尔(bool),作用是控制action bar 的显示位置.

`ModelAdmin.action_selection_counter`:取值为布尔，作用是是否显示选择计数器．选择计数器，选择的时候，会在下拉响应菜单的旁边实时显示数量．

`ModelAdmin.date_hierarchy`:取值为字段类型中的DateField/DateTimeField,作用是在列表页面上方生成一个基于时间的导航．

`ModelAdmin.exclude`:．．．

`ModelAdmin.fields`:需要编辑的字段取值为元祖。点击添加的时候可以供用户编辑的字段。注意`DataTimeField`有的auto_add, auto_add_now等字段选项不能出现在这个元祖中。

`ModelAdmin.list_display`:取值为元祖，　作用是定义在Model列表中要显示的字段．

`ModelAdmin.list_filter`:取值为元祖，作用按元祖中的选项过滤Model,表现为在页面的右边显示了一系列的过滤选择．

`ModelAdmin.search_fields`:取值为元祖，　作用是提供一个搜索框，　可以搜索元祖中列举的字段．

`ModelAdmin.prepopularted_fields`:取值为字典，**键值必须在fields选项中**作用是自动根据字典中的Value生成SlugField填充Key,通常作用是将Key为SlugField,然后通过Value来自动填充，其中Value为元祖．并且Value不支持DateTimeField 和关系字段.

`ModelAdmin.raw_id_fields`:取值为一个元祖，作用是将Model中ForeignKry由默认的下拉选择框改成文本输入框，使得用户可以直接键入ForeignKey的对象ID便可以，也可以点击选择．

`ModelAdmin.ordering`:取值为一个列表，　作用是按照列表中所给的字段排序，字段为字符串，加上 '-' 为反向排序．


