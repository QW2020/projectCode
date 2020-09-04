#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
冠状病毒 数据存储
'''

import mysql_utils, excel_utils, gzbd_spider;
# 获取所有数据
gzbd_all_data = gzbd_spider.gzbd_all_data();

def storage_mysql():

    for item in gzbd_all_data:
        # build sql 语句：根据时间查询、插入语句
        epidemic_date = item["日期"];
        query_sql = "select * from  gzbd_epidemic where date = '%s'" %(epidemic_date);
        insert_sql = "insert into gzbd_epidemic (region, date, diagnosis, overseas_import, cure" \
                     ",death, therapy, observation) values ('%s' ,'%s' ,%s ,%s ,%s ,%s ,%s ,%s)"%\
                     (item["地区"],item["日期"],item.get("确诊数",None),item.get("境外输入数",None),
                      item.get("治愈数",None),item.get("死亡数",None),item.get("隔离数",None),item.get("观察数",None));
        insert_sql = insert_sql.replace("None", "Null");

        # 查询数据，以此判断是否需要插入
        result = mysql_utils.execute_all(query_sql);
        if len(result) == 0:
            # 插入数据
            result = mysql_utils.execute_all(insert_sql);
            if result > 0:
                print("ok");
            else:
                print("error");

def storage_excel():
    header = ["地区", "日期", "确诊数", "境外输入数", "治愈数", "死亡数", "隔离数", "观察数"];
    body = list();
    for item in gzbd_all_data:
        line = [];
        line.append(item["地区"]);
        line.append(item["日期"]);
        line.append(item.get("确诊数", None));
        line.append(item.get("境外输入数", None));
        line.append(item.get("治愈数", None));
        line.append(item.get("死亡数", None));
        line.append(item.get("隔离数", None));
        line.append(item.get("观察数", None));
        body.append(line);

    file_path = "/python视频/temp/gzbd_data.xlsx"
    excel_utils.create_excel(header, body, file_path);

if __name__ == "__main__":
    # storage_mysql();
    # storage_excel();
    pass;