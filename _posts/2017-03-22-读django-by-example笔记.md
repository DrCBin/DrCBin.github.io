---
title: 读django by example 笔记
category: django
excerpt: |
  django by example 的读书笔记
---
# 第一天
-  创建第一个站点:
`django-admin startpreject mysite`
2. 使用 manage.py 添加建立第一个应用:
`python3 manage.py startapp blog`
3. 安装创建的应用:
> 刚建立的应用需要安装，才能被系统识别，安装方式为在站点的settings.py文件中，　有个　INSTALL_APP 的列表中添加刚创建的应用．
4. 创建第一个Model:
> 创建一个应用之后，默认就有model.py模块，只需要编辑该模块，创建Model即可．书中是创建了一个 'Post' Model．如下:
```python
	from django.db import models
	class Post(models.Model):
		title = models.CharField(max_length=50)
		publish = models.Datetimefield()
		class Meta:
			ordering = ('-publish',)
		def __str__(self):
			return self.title
```
> - Post 为Model名字，是一个类．
> - title、publish等是变量，后面的CharField等叫做字段，关于字段的介绍和类型见[这里](http://single-thread.me/django/2017/03/13/django%E5%AD%97%E6%AE%B5%E7%B1%BB%E5%9E%8B%E6%80%BB%E7%BB%93/)
> - models.CharField(max_length=50),其中max_length叫做字段选项，关于字段选项的作用及类容见[这里](http://single-thread.me/django/2017/03/13/django%E5%AD%97%E6%AE%B5%E7%B1%BB%E5%9E%8B%E6%80%BB%E7%BB%93/)
> - class Meta:叫做元类，作用是为该Model定义一下不可见的功能，比如排序等，　关于元类的详细介绍在[这里]()．
> - ordering = ('-publish',):叫做元选项，关于元选项的作用及种类见[这里]()．
> def __str __:是Model的模型方法，和　python的方法作用一样.

- 生成迁移脚本:
`python3 manage.py makemigrations`
作用是将基于当前应用中的Model,生成相对应的数据库生成迁移策略文件．简单说就是根据你的Model,确定怎么生成数据库中的表．
- 执行迁移：
`python3 manage.py migrate`
作用是根据伸长的迁移策略，执行迁移，简单说就是执行在数据库中创建表．
- 创建管理员用户：
`python3 manage.py createsuperuser`
创建一个管理员用户，用于后台登陆管理员界面．
- 运行开发服务器：
dango自带了一个简单的开发服务器，运行`mython3 manage.py runserver`便可以运行．然后访问`localhost:8000/admin`，使用管理员账号便可以登陆．
- 注册Model到admin:
> 为了在admin界面管理Model,需要将Model先注册到admin站点，方法是在admin.py中注册．
```python
	from django.conrrib import admin
	from .models import Post
	admin.site.register(Post)
```
具体注册方法见[这里](http://single-thread.me/django/2017/03/12/django%E6%B3%A8%E5%86%8Cmodel%E5%88%B0adminSite%E7%9A%84%E6%96%B9%E6%B3%95/).

- 模型API的使用：介绍了API的简单使用，包括了创建，更新，查询，删除等．具体的API使用见[这里]().
- 自定义模型管理器：
> 管理器就是用来管理Model的，其提供了对模型的一些操作的接口．
models默认提供的是objects管理器，但是有时候这个管理器并不是我们期待的样子，这时候我们就可以自己写自己的管理器了．关于自定义管理器的详细，见[这里]()．
- 建立视图：
所谓试图，就是接收请求，进行业务逻辑处理并返回一个响应的东西．书中简单的使用了两个请求，一个是post列表，一个是post详情．试图的实质为一个函数．
- 建立URL路由器 urlpatterns．
上述说了，试图的作用是进行业务逻辑处理并返回一个响应，而URL路由的作用便是解析网址，并将不同的请求分配给对应的View处理，则便是URL路由的作用．具体用法见[这里]().
- URL路由使用include.
系统给我们提供的URL路由模块是  urls.py,并且只有一个，　但是如果我们将所有应用的工作都交给这个路由来做的话，　势必会造成负担，并且不好维护和管理．　因此我们可以给每个应用都配置一个属于自己的路由．使用include.具体如下：
```python
	# in blog/urls.py
	from django.conf.urls import url
	from . import views
	urlpatterns = [
		url(r'^$', views.post_list, name='post_list'),
	]
	
	# in mysite/urls.py
	from django.comf.urls import url, include
	urlpatterns = [
		url(r'^blog/', include('blog.urls', namespacs='blog', app_name='blog')),
	]
```
这样，post/urls.py文件就只管理post的url, 然后在将子url include到父url路由器统一管理．

- 规范化Model的url:
当我们想要访问一篇post 的详情的时候，　我们需要通过url访问，所以对于每一篇post,都需要一个唯一的url,所以我们需要按照一定的规范来产生每一个Model对应的url.
```python
	from django.core.urlresovers import reverse
	class Post(modes.Model):
		# ...
		return reverse('blog:post_detail',
						args = [self.publish.year,
								self.publish.strftime(%m),
								self.publish.strftime(%d),
								self.slug])
```
- 使用模板：
django在html页面可以使用模板引擎，具体使用方法见[这里]()．

- 使用分页助手：
我们在页面中显示post列表的时候，有时候数目过多，　此时可以使用分页的方法显示．具体见[这里]().
 - 使用通用视图:
 有时候我们的视图是没有进行任何的特定逻辑处理，或者某些逻辑处理是很简单且统一的，这时候我们可以将他们简化成一个模板，使用的时候只需要传递几个参数就行．比如显示列表的试图，不管是什么Model，都可以显示成列表．关于django中的通用试图，见[这里]().
 
 
--------
# 第二天,终于开始更新第二次了
- 发送邮件：
简单的讲了一下邮件的发送方式，具体见[这里](),并涉及ModelForm的使用。其中用到了两个Model，`models.ModelForm`,`models.Form`,两个的区别见[这里]().

- 启用评论功能：
此处自定义了一个Model Comment，当做是评论类，其中将Post作为Comment的外键。其他的就是一个简单的表单。接着就是简单的处理了一下有关评论的templates

- 使用文章标签:
先安装标签，pip3 install django-taggit并注册到settings.py.然后在post Model中启用标签管理
```python
from taggit.manager import TaggableManager
class Post:
	#...
	tags = TaggableManager()
```

这样post就有tag属性了, 然后在post_list.html template 中进行标签的显示处理。

- 推荐相似的Post：
由于使用了 tag标签， 则可以根据文章的标签来推荐具有相同或者相似标签的文章。在这个地方遇到了一个坑，并get了一个技能：由于对正则表达式不是熟，所以在配置url路由器的时候，正则表达式写错了，应该是```(?P<tag_slug>[-/w]+)```, 我硬是写成了`(?P<tag_slug>[-/w+])`,如此便出现了NoReverseMatch的错误。
通过找资料，get了一个技能，当在模板中需要用到` url 'url-name' arg1 arg2 %}`来获取url地址的时候， 可能会出现获取失败的情况，或者这啊那的出问题，则可以将上述需要获取的url地址通过这样设置成一个变量:` url 'url-name' arg as varname %}`, 这样在需要用到url路径的地方使用`{{ varname }}`就行了。但各有优缺点
    - 优点：保证了网站的正常行不会崩溃，导致无法访问等。
    - 缺点：在调试期间无法很好的及时发现错误。比较好的解决办法是在使用`{{ varname }}`的时候先判断试下该变量是否为空。
    
### 第二天总结
第二天完事了，这章的内容不多，主要是添加一些功能内容为主，业务逻辑偏多，新技术涉及较少。

--------

# 第三天
> 这一章的内容不是很多，因为有的用不到，现在也没必要过于深入的折腾，所以过滤了差不多一半的内容。

- 自定义模板标签：
`django.template.Library()`库提供了自定义模板标签的可能。模板标签需位于指定目录下，默认是和`tamplate`在同一个目录下，目录名字为`tamplatetags`,并且需要用`__init__.py`初始化为模块，然后建立标签文件eg:`post_tag.py`具体用法如下。
    - 导入Library()库：
```python
	# in sitename/appname/templatetags/file_name.py
	from django.template import Librarry() as register
```
编写模板标签函数：
```python
    	def total_posts():
    		return Post.published.count()
```
注册函数为模板标签：
```python
	@register.simple_tag
	def total_posts():
		return Post.published.count()
```
其中注册器分三种:

> - simple_tag:模板标签的功能只限于返回简单的字符串
> - inclusion_tag:可以返回一个`tamplate`，并且使用变量。
> - assignment_tag:可以返回一个上下文变量。

具体用法见[这里]().


- 自定义过滤器：
自定义过滤器和自定义模板标签的方法一样， 只是在注册的时候使用`register.filter`注册。
- 添加站点地图：只是大概的了解了一下什么是站点地图，只是知道作用大概是方便网站被搜索引擎检索到。
- 添加RSS订阅：恩，了解，没使用。
- 添加站内搜索:了解了一下，也没配置成功。