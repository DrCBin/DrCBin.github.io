---
title: django注册models到admin site的方法总结
category: django
excerpt: |
  介绍了model注册的用法，中介ModelAdmin的选项及作用
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
** ModelAdmin.action **:其值为一个列表，列表内容是响应的函数，作用是定义在admin site中选择多个model实例是，可用的操作．通俗说就是批量处理的行为．
** ModelAdmin.action_on_top/bottom **:值为布尔(bool),作用是控制action bar 的显示位置.

