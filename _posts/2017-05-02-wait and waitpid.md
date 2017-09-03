---
title: wait 和 waitpid 的用法
category: c\c++
excerpt: |
  wait和waitpid的用法学习笔记
---

OS编写fork()代码的时候用到了wait和waitpid来保证fork()的子进程能被妥善处理，这里总结一下，供日后参考.

## wait:
- 函数原型:pid_t wait(int *status);
     - 返回值:返回所成功等到的子进程的pid 或发生错误时的-1;
     - 参数: 用来保存进程状态码的变量的指针;
     - 功能: 等待一个子进程运行结束并将该子进程彻底转变成终止状态
     - 用法示例:
     
```c
#include<stdop.h>
#include<sys/wait.h>
#include<unistd.h>
int main(){
	int status; //用来保存状态码的变量.
	if(fork() > 0){
		wait(&status);
		printf("status is:%d", status);
	}
	else{
		// do something
	}
	return 0;
}
```

可以看到，输出的值为一个256的整数倍的数.

但是我们并看不懂这个状态吗代表什么意思？没法理解它传递给我们的信息，就算可以查询，每次查询也比较麻烦.所以人们设计了一套宏来进行简单方便的解释这个。

## waitpid:
- 函数原型: pid_t waitpid(pid_t pid, int* status, int options);
    - 参数:
        - pid_t pid:
            - pid > 0:等待进程号与pid相等的子进程;
            - pid == 0:等待[进程组](http://baike.baidu.com/item/%E8%BF%9B%E7%A8%8B%E7%BB%84)与其父进程的进程组相同的任意子进程；
            - pid == -1:等待任意子进程,同wait作用一样.
            - pid < -1: 等待进程组号为 -pid 的子进程； 
        - int *status; 同wait();
        - int options:
            - WNOHANG: 如果想wait的子进程还没进入退出状态，则返回0，不再继续等待.
            - WUNTRACED: 如果子进程进入暂停执行情况则马上返回, 但结束状态不予以理会. 子进程的结束状态返回后存于status.(这个我还是没有理解啊...找了这么多都是这么说,没有完整的解释的！)
            - 0: 不使用第三个参数;
            
        - 返回值:
            - 正常返回: 子进程的pid;
            - 意外返回: -1; 错误表示存放于errno
            - 没有等待想等待的子进程结束，并且参数设置为WNOHANG: 0;
        
        - 功能:同wait();
        
列子和上面的差不多，就不写了。

**其他一些补充:**

- wait() 其实是 waitpid()的包装:

```c
// wait.c
pid_t wait(int *status){
	return waitpid(-1, status, 0);
}
```

- status码对人类还说不好读，所以人们发明了一套宏来更好的读取status码:(感觉就是函数，为啥叫宏...)

| 宏 | 作用|返回值|
| ---- | ---- |----|
| WIFEXITED(int status) | 根据给的状态码判断进程是否为正常退出 | 0:异常退出； 非0: 正常退出|
WEXITSTATUS(status)|取得子进程exit()返回的结束代码, 一般会先用WIFEXITED 来判断是否正常结束才能使用此宏.|子进程exit()返回的结束代码|
|WIFSIGNALED(status)|如果子进程是因为信号而结束则此宏值为真|0:进程不是因为信号终止, 非0：子进程因为信号而终止|
|WTERMSIG(status)|取得子进程因信号而中止的信号代码, 一般会先用WIFSIGNALED 来判断后才使用此宏.|信号代码|
|WIFSTOPPED(status)|如果子进程处于暂停执行情况则此宏值为真. 一般只有使用WUNTRACED时才会有此情况.|非0:子进程处于暂停状态|
|WSTOPSIG(status)|取得引发子进程暂停的信号代码, 一般会先用WIFSTOPPED 来判断后才使用此宏.|暂停的信号代码|

- waitpid的第三个参数可以使用组合的形式，如WIFHANG||WUNTRACED.

           
            
        
