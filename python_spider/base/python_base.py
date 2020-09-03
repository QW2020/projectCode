#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
基础
'''

import re,math;

# === 输入输出 ===
# a = input();
# print(a);
a = 11;
b = "qw";
print(a);
print("hello world");
print("hello", "world", "haha");
print("hello %s" % a);
print("hello %s" % (a));
print("hello %s %s" % (a, b));

# === 数据类型 ===
a = 11;
print("a = %s,数据类型: %s" % (a, type(a)));
a = 11.11;
print("a = %s,数据类型: %s" % (a, type(a)));
a = "abcdefg";
print("a = %s,数据类型: %s" % (a, type(a)));
# NoneType 相当于null
a = None;
print("a = %s,数据类型: %s" % (a, type(a)));
# bool
a = True or False;
print("a = %s,数据类型: %s" % (a, type(a)));
# list
a = ['aaa', 123, 12.3];
print("a = %s,数据类型: %s" % (a, type(a)));
# tuple类型，初始化之后元素不能变
a = ('aaa', 123, 12.3);
print("a = %s,数据类型: %s" % (a, type(a)));
# dict类型，键值对存储
a = {"name": "qw", "age": 66};
print("a = %s,数据类型: %s" % (a, type(a)));

# === 运算符 ===
print((2 + 45 / 12) * 2);  # 11.5
print(15 // 2);  # 地板除，取整 7
print(12 % 5);  # 2
print(2 ** 3);  # 乘方 8

# === ASCII 转换 ===
print("98-->%s;a-->%s" % (chr(98), ord('a')))  # 98-->b;a-->97

# ---- encode && decode ----
print("asd".encode("ascii"));  # b'asd'
print(b"asd".decode("ascii"));  # asd 解码
print("中文".encode("utf-8"));  # b'\xe4\xb8\xad\xe6\x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"));  # 中文

# === 前缀字符串 ===
print(u'中文');  # 后面字符串是以Unicode编码 中文
print(r'dddd');  # 普通字符串 dddd
print(b'qwqw');  # 后面是bytes  b'qwqw'

# === len ===
print(len("aaa"));  # 3, 对于str计算字符数
print(len("中文"));  # 2, 对于str计算字符数
print(len("aaa".encode("utf-8")));  # 3, 对于bytes计算字节数
print(len("中文".encode("utf-8")));  # 6, 对于bytes计算字节数 --- utf8中一个中文占3个字节

# === replace ===
a = "cdcassqwsdfrfqwsdfdf";
print(a.replace("qw", "==="));  # cdcass===sdfrf===sdfdf
print(a);

# === find ===
print("abcdefgce".find("c"));  # 2, 字符第一次出现的下标
print("abcdefgce".rfind("c"));  # 7， 字符最后一次出现的下标

# === isspace ===
print("   ".isspace());  # true, 判断字符串是否为空格

# === 字符串格式化 ===
print("%d----%2d----%03d" % (2, 3, 4));  # 2---- 3----004, 2d(不足两位左边补空格)、02d（不足3位，左边补0）
print("%f----%.2f" % (2.22, 3.333));  # 2.222000----3.33， .2f(保留2位小数，四舍五入)、float保留六位小数
print("%x" % 333);  # 14d， 格式化为16进制
print("%s %% %s" % ("3", "2"));  # 3 % 2
print(list("%s" % x for x in range(2, 10)));  # ['2', '3', '4', '5', '6', '7', '8', '9']， 将2 - 10生成器，转化成字符串list
print("Hi {0}, 成绩提高了{1:.1f}%".format("小名", 1.234));  # Hi 小名, 成绩提高了1.2%
print("Hi {0}, 成绩提高了{1}%".format("小名", 1.234));  # Hi 小名, 成绩提高了1.234%
print("Hi {0}, 成绩提高了{1}%".format("小名", "%.1f" % 1.234));  # Hi 小名, 成绩提高了1.2%
print("-".join(["a", "b", "c"]));  # a-b-c, 字符串拼接

# === 正则表达式 ===
# === 匹配字符串 ===
email_re = "^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$";
# 如果匹配成功，将返回一个Math对象，失败则返回None
if re.match(email_re, "2421109032@qq.com"):
    print("ok");
else:
    print("error");

# === 切分字符串 ===
print("a b  c".split(" "));  # ['a', 'b', '', 'c']
print(re.split(r"\s+", "a b c"));  # ['a', 'b', 'c']
print(re.split(r"[\s\,\;]+", "a,b;; c   d"));  # ['a', 'b', 'c', 'd']

# === 分组 ===
# 分组提取电话号码
math = re.match(r"^(\d{3})-(\d{3,8})$", "010-12345");
print(math.group());  # 010-12345
print(math.group(0));  # 010-12345
print(math.group(1));  # 010
print(math.group(2));  # 12345
# 分组提起时间
math = re.match(r"^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:"
                r"(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:"
                r"(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$", "19:05:30");
print(math.groups());  # ('19', '05', '30')
# 分组提取数字
new_line = r'截至9月2日0时，全省累计报告新型冠状病毒肺炎确诊病例653例(其中境外输入112例），' \
           r'累计治愈出院626例，死亡3例，目前在院隔离治疗24例，964人尚在接受医学观察';
new_line_re = r'^截至9月2日0时，全省累计报告新型冠状病毒肺炎确诊病例(\d+)例\(其中境外输入(\d+)例\），' \
              r'累计治愈出院(\d+)例，死亡(\d+)例，目前在院隔离治疗(\d+)例，(\d+)人尚在接受医学观察$';
new_line_math = re.match(new_line_re, new_line);
print(new_line_math.group(0));
print(new_line_math.group(1));  # 653
print(new_line_math.group(2));  # 112
print(new_line_math.group(3));  # 626
print(new_line_math.group(4));  # 3
print(new_line_math.group(5));  # 24
print(new_line_math.group(6));  # 964
new_line_compile = re.compile(new_line_re);
print(re.search(new_line_compile, new_line).group(1));  # 653
print(re.search(new_line_compile, new_line).group(2));  # 112
print(re.search(new_line_compile, new_line).group(3));  # 626
print(re.search(new_line_compile, new_line).group(4));  # 3
print(re.search(new_line_compile, new_line).group(5));  # 24
print(re.search(new_line_compile, new_line).group(6));  # 964
# 贪婪匹配
print(re.match(r"^(\d+)(0*)$", "102300").groups());  # ('102300', '')
print(re.match(r"^(\d+?)(0*)$", "102300").groups());  # ('1023', '00')

# === list ===
l = ["cas", 123, True, "cdasas"];
# 从前取值，index从0开始往后；从后取值，index从-1开始往前
print(l[0] + "-----" + l[-1]);  # cas-----cdasas
# 集合尾部添加元素
l.append("qwqw")
print(l);
l.insert(2, "cccc");
print(l);
# 删除集合最后一个元素
l.pop();
# l += 12;
l[0] = "aaaa";
print(l);
l = list(range(1, 10));
t = ("aaa", 12, 12.2, True, None, l);
l[1] = 11;
print(t);
print("list: %s, length: %s" % (l, len(l)));  # list: [1, 11, 3, 4, 5, 6, 7, 8, 9], length: 9

# ==== tuple ====
t = tuple(range(10));
print(t);
t = ("aads", 123, True, None, 12.3);
print(t);
# 定义只有一个元素的元祖，元素后追加“,”，以免误解成数学计算意义上的括号
t = ("cdsa",);
print(t);
# 集合作为元祖的元素，我们可以修改集合的元素
t = ("vsv", ["aaa", "sss"]);
print(t);  # ('vsv', ['aaa', 'sss'])
t[1][1] = "bbbb";
print(t);  # ('vsv', ['aaa', 'bbbb'])
print("tuple: %s, length: %s" % (t, len(t)));  # tuple: ('vsv', ['aaa', 'bbbb']), length: 2
t2 = tuple(range(1, 10));
print(t2);
print((1));
print((1,));  # 代表元祖对象

# ---- dict  ----
# 全称dictionary，使用key-value存储
d = {"name": "qw", "age": 22};
print(d.get("name1", "aaaaa"));  # aaaaa
print(d.get("name"));  # qw
d["name"] = "hyman";
d["aaa"] = "111dasa";
print(d);  # {'name': 'hyman', 'age': 22, 'aaa': '111dasa'}
d.pop("aaa");
print(d);
print(len(d));

# ---- set  ----
# 存储的是一组key集合，不存储value 无序
s = set(["cds", True, None, 212, 22.3]);
s2 = {"cds", 212, 22.22, "cdsacdasd"};
s.add("hyman");
print(s);
# s.pop();
print(s);
s.remove("cds");  # 移除
print(s);
# 交集、合集
print(s & s2);  # {212}
print(s | s2);

# ==== 判断语句 ====
a = 10;
if a <= 10:
    print("aaa");
elif 10 <= a <= 20:
    print("bbb");
else:
    print("ccc");
# 三目运算符
a, b, c = 1, 2, 3
print(a if (b > c) else c);  # 3


# ==== 循环语句 ====
# l = list(range(1, 10));
# for i in l:
#     print(i);
# i = 0;
# while (i<10):
#     print(i);
#     i += 1;
#     print(i);

# ==== 函数 ====
def test(a):
    a += 3;
    return a;


print(test(8));
f = test(8);  # 11
print(f);  # 11


# 位置参数
def test_2(x, y="qw"):
    print(x, y);


# 可变参数
def test_3(*num):
    count = 0;
    for i in num:
        count += i;
    return count;


# 可变关键字参数
def test_4(name, **kv):
    if "city" in kv:
        print("name:%s, city:%s" % (name, kv.get("city")));
    else:
        print("name:%s, city:%s" % (name, "sichuan"));


# 命名关键字参数
def test_5(name, *, city):
    if not isinstance(name, (str,)):
        raise TypeError("Type error");
    print("name:%s, city:%s" % (name, city));


if __name__ == "__main__":  # 相当于main方法
    print(test(8));  # 11
    test_2("hello", "hyman");  # hello hyman
    test_2("hello");  # hello qw
    print(test_3());  # 0
    print(test_3(*list(range(1, 9))));  # 36
    print(test_3(1, 2, 3, 4, 5));  # 15
    test_4("qw", **{"age": 33});  # name:qw, city:sichuan
    test_4("qw", **{"age": 33, "city": "cd"});  # name:qw, city:cd
    test_5("qw", city="cd");  # name:qw, city:cd

# === 内置函数 ===
print(int("22"));  # 数据类型转换函数，注意，如果定义变量名和函数名一样，则不会调用该函数，会报错
print(float("22.2"));
print(str(22));
print(abs(-111));  # abs函数，求绝对值
print(max(12, 34, 123.4));  # max函数，求最大值
print(min(-21, -11, 0, 22.3));  # min函数，求最小值
print(" aa bb  cc  ".strip());  # 字符串去前后空格
print("['6K-8K']".strip('[\'\']'));  # 6K-8K 移除字符串头尾指定的字符
print(hex(12));  # hex函数，将十进制数转十六进制
print(math.sqrt(3));  # 求平方根
print(sum(range(1, 101)));  # 求和
print(sum(list(range(101))));
print("cdaDcdsa".capitalize());  # 将字符串第一个字符变成大写，其他小写
