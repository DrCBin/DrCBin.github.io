---
layout: post
title: "github之一台电脑添加两个账户"
categories: [Tech]
excerpt: 在同一台电脑上使用两个以上github账户的方法.
tags:
  - github
---


一个私人，一个工作,拥有两个github账号是很正常的一件事了,但是要在一台电脑上使用两个github账户怎么办？

github服务器确认你是你的两种方法:
1. 你的github账号和密码.
2. 唯一的ssh密钥对.

显然，第二种方便，一次添加，永久有效.

所以,要在一台机器上使用两个github，需要两个ssh密钥对:

```ssh
ssh-keygen -t rsa -f "path/you/want/filename" -C "your@email.com"
# 通常是 -f '~/.ssh/id_rsa_work'
```

**注意,文件名不能和已经存在的重复**


好了,现在你有假冒的自己了. 然后把假冒的自己添加到另一个github账户.过程跳过.

现在你还需要伪装一下,不然能被认出你和那个人是同一个人.

在`~/.ssh/`文件夹下新建`config`, 并添加以下内容:

```ssh

# default 真实的你自己
Host github.com
    HostName github.com
    IdentityFile ~/.ssh/id_rsa


# work 后来添加的那个假的
Host xxx.github.com   # 只是起了个假名字，假外表, 假名字你可以随便起
    HostName github.com    # 灵魂还是自己原本的
    IdentityFile ~/.ssh/id_rsa_work    # 假的你用着另一张假的身份证
```

好了，假的自己已经造好了,现在就是向公安局上提交假自己的档案了.运行命令:

```shell
ssh-add ~/.ssh/id_rsa_work
```


如果你向全世界都宣布过了你的名字了,那么你要把它撤回

```git
git config --glogal --unset user.name
git config --glogal --unset user.email


# 然后在每一个仓库单独告诉他们你想让它知道的名字

git config user.name "my-name"
git config user.email "your@email.com"
```

对了,你设置的远程仓库别忘了改

```git
git remote add origin git@xxx.github.com:AccountName/ResName.git
# git是config里面的User，xxx.github.com就是你的Host
```

ok! 开始享受两个自己吧.
