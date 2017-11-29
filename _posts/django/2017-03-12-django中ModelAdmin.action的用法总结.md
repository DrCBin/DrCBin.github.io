---
layout: post
title: "django中ModelAdmin.actions用法总结"
categories: [Tech]
excerpt: ModelAdmin.actions的用法总结
tags:
  - django
---

[参考文档:django documentation](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/actions/)</br>
`ModelAdmin.actions`的作用是提供一系列对Model实例批量处理的可用操作．举个简单例子，当要删除某个Model实例时，先选择实例，然后删除，当要删除一堆实例的时候，就会多选，然后删除．`ModelAdmin.actions`做的就是提供一系列类似于*删除*的方法．

#### 用法：

``` python
	# 编写处理的方法
	def do_something_for_seleted_items(self, request, queryset):
		pass	
	# 设置对外描述
	do_something_for_seleted_items.short_description = "do something"
	
	@site.register(ModelName)
	class ModelAdminName(admin.ModelAdmin):
		# 添加处理的方法
		actions = [do_something_for_seleted_items,]
```

这样，在admin site页面，批量选择实例后，就可以批量对这些实例进行操作．
我们还可以把处理的方法放到`class ModelAdminName`中，是的处理的方法看起来更有针对性，像这样:
``` python
	# 编写处理的方法
	def do_something_for_seleted_items(self, request, queryset):
		pass	
	# 设置对外描述
	do_something_for_seleted_items.short_description = "do something"
	
	@site.register(ModelName)
	class ModelAdminName(admin.ModelAdmin):
		# 添加处理的方法
		actions = [do_something_for_seleted_items,]
	
		# 编写处理的方法
		def do_something_for_seleted_items(self, request, queryset):
			pass	
		# 设置对外描述
		do_something_for_seleted_items.short_description = "do something"
	
```


还可以改进，当处理完操作之后，向用户显示一个通知，告知用户处理的结果,可以使用`ModelAdmin.message_user()`来提供通知：
``` python
# 编写处理的方法
	def do_something_for_seleted_items(self, request, queryset):
		pass
		self.message_user(request, 'something done,or some notice')
```


或者当操作完成之后，返回给用户一个重定向或者响应:
``` python
# 编写处理的方法
	def do_something_for_seleted_items(self, request, queryset):
		pass
		return response/HttpResponseRedirect
```


#### 对所有的Model实例都启用同一个响应
如果你写的某一个方法对所有的Model都适用，那么可以把他添加到全局的响应里面，比如说统计选择条数的函数，对全局都通用．
``` python
	def count(self, request, queryset):
		num = queryset.count()
		self.message_user(request, '选择了{}条．'.format(num))
	count.short_description = '选择了多少条'
	admin.site.add_action(count)
```

这样，无论你操作那个Model的实例，都会有count的响应可选择.

`admin.site.add_action`可以选择第二个参数，第二个参数的作用是给这个响应命名，这样以后可以方便的操作这个响应．

`admin.site.add_action(count, 'show item num')`这样就把*count*这个响应命名为*show item num*了．

#### 对某个站点禁用全局响应
适用`admin.site.disable_adtion`来禁用某个响应，参数为响应的名字．eg:

``` python
	admin.site.disable('show item num')
```

#### 对某个Model禁用所有操作
``` python
	class ModelAdminName(admin.ModelAdmin):
		actions = None
```
这样，该模型就被禁用了所有的批量操作，包括自带的删除操作

#### 按需选择操作
我们可以通过复写`ModelAdmin.get_adtions`来获取可用响应
``` python
	class ModelAdminName(admin.ModelAdmin):
		...
		def get_actions(self, request):
			# 获取所有操作
			actions = super(ModelAdminName, self).get_actions()
			if ...:
				# 如果满足一定条件，则删除某个响应或者添加某个响应
				del actions['action name']
				actions.add('another action')
			# 返回经过处理的actions
			return actions
```
