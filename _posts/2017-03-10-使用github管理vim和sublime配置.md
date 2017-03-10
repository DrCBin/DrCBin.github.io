---
title: 使用github备份vim和sublime配置
category: github
excerpt: |
  如何使用github来管理配置文件
---

sublime使用的时间长了，渐渐的就积累了一些有用甚至离不开的插件。但是有时候系统会出点问题，或者换电脑什么的，这时候要想在找回那个曾经的sublime就不那么容易了。好在我们可以把我们的配置备份起来。需要用的时候直接下载就好。

首先，我们选择的是使用github来备份我们的sublime，我的目的是把windows下的配置备份一下，然后去linux下使用。当然，还不知道能不能直接跨到linux下使用。先备份了再说。

------
### 准备
>1.  电脑上安装好git
>2.  在[github](http://www.github.com)上注册一个账号
>3.  本机上安装个sublime(有点废话)

### 创建本地仓库
>1.  启动gitshell，并切换到sublime(vim)的配置目录
>  - 切换目录的命令是 cd 'path',比如，我要切换E盘，就输入 cd e:
>  - sublime的配置文件以及安装包存放路径，在sublime菜单项：preferences->browse pacakges.这样打开的是sublime的包目录，再往上一级就是整个sublime的配置以及包目录了。
vim的配置文件在~/.vimrc, 安装的插件等在~/.vim文件夹下．
>  - git 的仓库是一个文件夹，所以我们选择~/.vim作为仓库目录，移动~/.vimrc到~/.vim文件夹下，并且重命名为vimrc(去掉'.',git是不会添加隐藏文件的)．
>  - 在用cd 命令切换目录的时候，记得把路径用单引号引起来，因为可能路径有空格，就找不到了。
>2. 切换到配置目录以后，执行命令```git init``` 
>     -  该命令的作用是将当前文件夹初始化为仓库 
>3.  然后执行```git add .```
>  -   该命令添加所有的文件到缓存区。
>4.  然后执行```git commit -m "say something"```
>   -   该命令的作用是将缓存区的东西提交到仓库
>   -   双引号里面的内容可以随便写，一般是写一些关于这次提交的说明
### 创建远程仓库
>1. 登陆[github](http://github.com),个人主页的右上角有个"new  repository"的绿色按钮。然后点击创建一个新的repository，输入名字，确定。完成之后会创建一个空repository，很明显的地方能看到一个ssh码。格式是git@github.com:accountName/repositoryName.git，复制该ssh 码。
>  -  将上述的acountName和repositoryName对应成自己的。下同
>2.  将远程仓库和本地仓库连接。执行命令```git remote add origin git@github.com:accountName/repositoryName.git```
>  -   remote是git远程主机的操作命令，后面的add就是添加一个远程主机的意思了。
>  -  origin是一个名字，是你远程主机的名字，这个名字只是一种约定，你也可以起你自己想要的名字。
>  -   后面那一串就是之前准备的ssh码了
>3.  将本地仓库推送到远程仓库。 ```git -u push origin master```
>  -  origin是你要推到的目标主机，master是你要推送的本地分支，git默认的分支就叫master。

至此，本地的配置都备份到远程的仓库了
### 恢复配置
>1.  如果机器安装了git。
>     1.   运行gitshell，切换到sublime配置所在目录或～目录．
>     2.  执行```git clone git@github.com:accountName/repositoryName.git```
> 
> 2.  如果没有安装git，就去github上下载zip包，然后解压到sublime配置目录就行
> 3.重命名：将下载下来的文件夹重命名成sublime的文件夹 名字，就是之前我们初始化仓库的那个名字，vim 的话重命名为.vim,然后再把.vim文件夹里面的vimrc链接到～目录：
> ```link vimrc ../.vimrc```

这样，配置就回复了．往后如果有修改的配置记得备份一下就行，不怕换电脑丢了．
