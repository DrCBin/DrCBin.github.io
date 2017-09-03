---
title: c++中char*和string的相互转换
category: c\c++
excerpt: |
  有时候需要将char*和string进行相互转换 .
---

#### char*转成string

```c++
char* s;
string newS(s);
string newS1 = s;
//string 可以使用一个char*来构造
//string也有对char*的拷贝构造函数.
```

#### string转char*

```c++
string s = "abc";
const char* const_c_s = s.c_str();
//只能转换成const的char*

char* c_s = (char*)malloc(1000);//足够大，也可以通过精确的计算，得到合适的.
strcpy(c_s, s.c_str());// 会产生中间垃圾


strcpy(c_s, const_c_s);
delete const_c_s;    //没有中间垃圾

```
