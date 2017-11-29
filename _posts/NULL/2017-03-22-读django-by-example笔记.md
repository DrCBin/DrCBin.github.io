---
layout: post
title: "读django by example 笔记"
categories: [Tech]
excerpt: django by example 的读书笔记
tags:
    - none
    - django
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


# 第四天

- 使用内建类`User`和内建认证模块`login`来实现一个用户的登陆，官方文档说明在[这里](http://usyiyi.cn/translate/django_182/topics/auth/default.html#auth-web-requests).
- 具体的流程为:  验证请求类型(get or post), 验证标单的可用性，获取标单数据，提取标单数据，进行用户认证`login(username='xx', password='xx')`,如果认证成功， 返回用户，认证失败返回**None**。所以**一定要先判断返回值**,在进行操作。

> 在实例化一个标单的时候， 可以使用`request.POST`在作为实例化的参数，这样标单就会自动获取POST值，并赋给表单的对应项。想必这也是html中的表单不用设置action url的原因吧。

- 使用内建的登陆模块:
除了使用自定义的试图来登陆，django还提供了内置的登陆系统，`django.contrib.auth.views`:提供了`login`,`logout`,等常用认证试图。并且有一些常用参数可选择，如指定模板，指定登陆后重定向等。官方文档见[这里]().
> 超级BUG，配置 url "xxx:xxx" %} 时，引号之间的字符串就是名字，包括空格，所以不要手残加空格
 
 - 扩展了User类，给User类添加了一个Profile， 关系为和User OneToOne。
 
- 添加了用户注册的功能:
编写了一个用户注册的表单类。主要用到一个方法，就是判断两次输入的密码，这个表单类基于`model=User`, 在编辑用户注册Views的时候，有一个地没太明白：
```python
	profile_form = ProfileEditForm(instance=request.user.profile)
```
**这个参数是干嘛用的。？**大概的感觉是这个表单中的数据和这个实例关联，如果实例中有表单中某个数据的字段就将它填充上。



- 添加了用户编辑的功能:
由于Profile属性是后来添加的，所以在之前创建的User就没有这个属性，所以当尝试访问没有属性的User的profile属性时，会报`RelateObjectDoesNotExist:user has no profile`错误。**所以需要将尝试获取User的profile的代码段用try-except包起来，这是书上没有说明的**。

- 简单的提了一句自定义User类。

- 启用消息通知：
`django.contrib.message`提供了消息对象，可以返回不同类型的消息。用法：
```python
	# in views.py
	from django.contrib import messages
	def anyviews(request):
		messages.success(request, 'Message body')
```
```html
	<!-- in html-->
	{.% if messages %}
		{.% for message in messages %}
			{.{ message|safe }}
		{.% endfor %}
	{.% endif %}
```
- 添加了自定义认证系统:
自定义认证需要实现两个方法:
```python
	def authenticate(self, username=None, password=None):
		pass
	
	def get_user(self, user_id):
		pass
```
然后在settings.AUTHENTICATE_BACNEND中添加。**认证的时候会重上到下认证，如果认证成功则不再进行下一个认证.**

- 添加第三方认证登陆的功能:
这个功能没做。

- blank的作用，表示可以不填。null的作用，表示可以为Null.

**需要解决：1. 自定义认证出现了问题。2.添加第三方认证登陆**



# 第五天

终于更新到第五章了。这章开始慢慢变难了，不是说django难了，而是开始涉及到的知识面变广了，很多都是我没有接触过，甚至不知道是干啥用的。一个一个来吧。

- 今天领悟到了一个很重要的问题，django寻找东西的时候只认名字。比如`settings.STATIC_URL = 'static/'`这样的设置，django需要静态文件的时候它就只找叫做static的文件夹，找到了就停，并不会去关心是在哪儿找到的。同样的道理，在使用模板继承的时候，我们写的是`{.% extends "base.html" %}`,django只知道在templates下找这个名字，**找到就用，并不会去管在那个templates找到的**。当然，**会优先搜索同级**。然后从前到后。

- 然后是开始写Image Model了：
```python
	class Image(models.Model):
		url = models.UrlFiels()
		slug = models.SlugFields()
		image = models.ImageFields(uplode_to='images/%Y/%m/%d')
		users_like = models.ManyToManyFields(settings.AUTH_USER_MODEL,related_name='images_liked', blank=True)
		# 多对多字段，表示点赞的人和被点赞的图片之间的关系
		
		def save(self):
			if not self.slug:
				self.slug = slugify(self.title) #django.utils.text.slugify
```
注意，这里会有两个save.`Image.save()`,`Image.image.save(name,content,save=True)`.前者是Model的save,保存的是所有model的信息， 后者是Field的save,保存的仅仅是image,并且需要两个参数，name 和content,名字和对应的实例。

- 紧接着创建了一个创建Image的表单:
```python
	class CreateImageForm(forms.ModelForm):
		class Meta:
			model = Image
			fields = ('title', 'url', 'description')
			widget = {
				'url':forms.HiddenInput,
			}
```
这个表单使用的是ModelForm，特点是根据一个Model来生成表单，同时 你可以规定需要填写的字段等。

- 紧接这给这个表单添加了一个获取url数据的方法clean_url:
```python
	def clean_url(self):
		url = self.cheaned_data['url']
		extension = url.rsplit('.', 1)[1]
		if extension not in ['jpg', 'jpeg']
			raise 'url error'
		return url
```

- 然后重写了ImageCreateForm.save()方法
重写的save()方法中，直接调用了Image的save()方法，如果数据都可用的话。这样就直接通过ImageCreateForm.save()将图片保存了，省的还要通过Image来保存。


- 接下来就是添加一个基于Jquery的收集功能，大概的实现原理是
    - 添加一段自动运行的js脚本，并拖到收藏栏
    - 打开网页的时候，脚本会自动运行，并且检查网页中的网址是否为图片
    - 将检测到的图片列出来，然后点击其中一张，就会跳到创建图片的页面。
    - 填写部分信息，结合从其他网站传过来的信息，完成图片创建。
    
不会写，照着书写出来是不能跑的， 故暂时放弃。


- 接下来还使用了其他的东西，比如AJAX来异步请求等，但是都不会。所以自己用很原始的请求响应来完成了同样的功能，保证网站完整运行。



# 第六天

- create_action中限制用户重复发动态的方法没有完善，记得完善。

- 有关动态中，用户和被牵连的东西之间的关系，ContentType啥的也没有弄懂。

-  image一直不能保存， 原来是重写save()的时候，缩进弄错了导致没有执行save()
