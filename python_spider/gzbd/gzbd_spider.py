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
__wjw_base_url = "/scwsjkw/gzbd01/ztwzlmgl.shtml";
__wjw_page_count = 10;

# 获取冠状病毒所有数据
def gzbd_all_data():
    all_data = [];

    # 创建新闻列表页 url && 获取列表页的数据
    news_page_url = __wjw_domain;
    for i in range(1,__wjw_page_count+1):
        if i == 1:
            news_page_url += __wjw_base_url;
        else:
            l = __wjw_base_url.split(".");
            l.insert(1,"_%d."%i);
            news_page_url += "".join(l);

        news_list = news_page_data(news_page_url);
        all_data += news_list;

        news_page_url = __wjw_domain;

    # print(all_data);
    return all_data;

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

    return news_list;


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
    if len(span_list) > 0:
        line = span_list[1].get_text();
    # elif len(span_list) == 3:
    #     line = span_list[0].get_text().split("。")[1];
        # print(line)
    # 正则表达式提取数据，并装到dict
    line_compile = re.compile(r'\d+例').findall(line)+re.compile(r'\d+人').findall(line);
    if len(line_compile)>0:
        new_dict["确诊数"] = (line_compile[0])[:-1];
        if len(line_compile) > 1:
            new_dict["境外输入数"] = (line_compile[1])[:-1];
            if len(line_compile) > 2:
                new_dict["治愈数"] = (line_compile[2])[:-1];
                if len(line_compile) > 3:
                    new_dict["死亡数"] = (line_compile[3])[:-1];
                    if len(line_compile) > 4:
                        new_dict["隔离数"] = (line_compile[4])[:-1];
                        if len(line_compile) > 5:
                            new_dict["观察数"] = (line_compile[5])[:-1];
    # print(new_dict)

    return new_dict;

if __name__ == "__main__":
    url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/2020/9/2/02e7dbad55354b1abbbce7871acea7d7.shtml";
    # url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml";
    # new_page_data(url);
    # gzbd_all_data();















