---
layout: post
title: 配置java运行环境和开发环境的配置(Windiws&Linux)
categories: [Tech]
excerpt: java运行环境的配置教程，包括了windous和linux平台．
tags:
  - NULL
---

本学期开了java课，要运行java程序，或者进行java开发，需要将电脑上的java环境配一下．

#### JRE:
jre(java runtime environment),java运行环境，包含了<strong>java</strong>程序运行所需的套件和环境，是java程序能正常运行的必要条件．
#### JDK:
jdk(java development kit),java开发套件，包含了<strong>jre</strong>,java<strong>编译调试程序</strong>和其他一些类库等.

## 下载:
甲骨文官网下载:[http://www.oracle.com/technetwork/java/javase/downloads/index.html](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
**注意选择jkd或jre,只有jre不能进行java的编译**
## 安装(JDK)
#### 1.java
- 解压下载好的文件到任何你想要安装的目录，此处假设该目录为JAVA_HOME
- 进入JAVA_HOME/bin下，可以看到一个可执行文件java.
- 在该目录打开控制台(windows下按住shift，然后单击右键，可以看到弹出的菜单中会有＇在此处打开命令窗口＇的选项)，然后输入java,便可看到java弹出的帮助．
#### 2.javac
- windows下进入JAVA_HOME/lib，可以看到该目录下有个javac的可执行文件，如果这个目录没有，便在JAVA_HOME/bin目录下
- linux下进入JAVA_HOME/bin,也就是和java在用一个目录，可以看到javac可执行文件.
- 在此目录打开控制台，输入javac，可以看到弹出的帮助信息．
如果上述两个命令都能弹出帮助，则<strong>说明JDK安装完成</strong>．
> 错误帮助:如果提示找不到命令，请检查两个地方:
> 
> - 上述目录下是否有java和javac的可执行文件．
> 
> - 控制台所在目录是否和上述文件是同一个目录(控制台光标前面的路径就是当前所在目录)
## 配置
上面已经安装好了JDK,也就是我们的电脑可以编译和运行java代码了，但是我们需要到java和javac的目录下才能运行，这样势必会造成一定的不方便，所以我们需要进行一定的配置，使得在任何目录都能正常执行java和javac.这个过程叫做<strong>java环境变量的配置</strong>.
#### linux:
编辑/etc/profile,在最末尾添加如下代码:
```
export JAVA_HOME=xxx/xxx/xxx
# JAVA_HOME为你的jdk安装目录
export PATH=$PATH:$JAVA_HOME/bin
# bin目录是编译，执行等程序的所在目录
export CLASSPATH=.:$JAVA_HOME/lib
# lib目录是java自带类库等所在目录
```
保存后执行下述命令,是配置生效:
```
sudo source /etc/profile
```
然后在任何地方运行java和javac,都能正常弹出帮助了，说名配置完成．
#### Windows:
参考图文教程,[点这里](http://jingyan.baidu.com/article/925f8cb836b26ac0dde0569e.html)！
配置完成之后也可以在任何地方打开控制台（之前打开的记得<strong>重启一下控制台</strong>），都能正常识别命令，说明环境配置完成．


