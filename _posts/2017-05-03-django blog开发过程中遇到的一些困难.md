---
layout: post
title: "django博客开发过程中遇到的一些困难"
categories: [Tech]
excerpt: 记录下我在开发博客过程中的一些困难
tags:
  - django
  - 总结
---

- 将页面解析成markdown:
    - 通过模板过滤器实现
    - 通过js解析前端实现

- 在template中使用下标访问一个list:
    - arrayName.index: {{ posts.0 }}

- 将某一个变量设置为全局模板变量，每一个页面都能访问:
    - 自己重写render方法，把传进来的名字加上全局名字再返回
    `def my_render(request, template, dirc):return render(request, template, dirc.update({'name':value}))`
    - 这是教程中提的第二种方法，没看明白,[教程](http://blog.csdn.net/shanliangliuxing/article/details/7595344)
    - 在settings.py中注册模板变量:[这里](http://blog.csdn.net/hengrjgc/article/details/50349698)

- gunicorn 不会使用，找到了官方的文档: [这里](http://docs.gunicorn.org/en/latest/signals.html)

- 使用gunicorn启动服务之后，找不到静态文件，原因是urls.py中要加上staticfiles_urlpattern

- 当时不是很理解STATIC_ROOT 和STATIC_URL 和STATICFILES_DIR 的区别和作用：
    - STATIC_URL: 是指django映射时候找找的文静目录，比如`STATIC_URL = '/static/'`, 那么django会自动将静态文件映射到所有名为static的文件夹上。
    - STATIC_ROOT:存放静态文件的目录，主要是部署服务器用的。部署服务器的时候需要给静态文件映射一个路径给服务器，由于我们之前的开发都是将静态文件分布在每个app的目录下，这样一个一个的去映射势必会造成一定的不便。这时候我们只需要设置一下STATIA_ROOT， 如`STATIC_ROOT = 'statics'`,这时候运行一下`pytnon manager.py collectstatic`,这样就会自动的把分布于每个app下的静态文件全部集中到statics了，然后再将这个路径映射给服务器就好了。
    - STATICFILES_DIR:告诉django有那些文件夹是静态文件，然后在urls.py里面加上staticfiles_pattern，就能直接输入静态文件的网址访问静态文件了.


- 表单重复提交的问题:如果一个页面需要提交表单数据，并且请求url也是本页面，即'.', 那么如果刷新页面，将会导致表单重复提交,博客中的评论。 解决方法是将处理表单的视图返回一个重定向.
