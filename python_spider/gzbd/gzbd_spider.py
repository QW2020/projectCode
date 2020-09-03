#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
冠状病毒 数据爬取
'''

import requests;
from bs4 import BeautifulSoup;
import re;

# 卫健委
__wjw_regin = "四川";
__wjw_domain = "http://wsjkw.sc.gov.cn";

# 爬取新闻列表页数据
def news_page_data(url):
    # 转载新闻数据
    news_list = [];

    # requests获取页面内容
    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    # bs4 解析页面标签
    bs = BeautifulSoup(r.text, "html.parser");
    li_list = bs.find(name="div",attrs={"class":"contMain fontSt"}).find_all(name='li');
    for li in li_list:
        child_span = li.findChildren("span", recursive=False)[0];
        child_a = li.findChildren("a", recursive=False)[0];
        new_page_url = __wjw_domain + child_a.get("href");
        new_dict = new_page_data(new_page_url);
        new_dict["日期"] = child_span.get_text();
        new_dict["地区"] = __wjw_regin;
        news_list.append(new_dict);
        # print(news_list)

    print(news_list)


# 爬取新闻数据
def new_page_data(url):
    # 转载新闻数据
    new_dict = {};

    # requests获取页面内容
    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    # bs4 解析页面标签
    bs = BeautifulSoup(r.text, "html.parser");
    span_list = bs.find_all(name="span",attrs={"style":"font-size: 12pt;"});
    line = span_list[1].get_text();

    # 正则表达式提取数据，并装到dict
    line_compile = re.compile(r'\d+例').findall(line)+re.compile(r'\d+人').findall(line);
    if len(line_compile)>0:
        new_dict["确诊数"] = (line_compile[0])[:-1];
        new_dict["境外输入数"] = (line_compile[1])[:-1];
        new_dict["治愈数"] = (line_compile[2])[:-1];
        new_dict["死亡数"] = (line_compile[3])[:-1];
        new_dict["隔离数"] = (line_compile[4])[:-1];
        if len(line_compile)>5:
            new_dict["观察数"] = (line_compile[5])[:-1];
    # print(new_dict)

    return new_dict;

if __name__ == "__main__":
    # url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/2020/9/3/fe0eb6e3101d4709a9bbd27f5a12ae78.shtml";
    url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml";
    news_page_data(url);

















