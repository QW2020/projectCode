#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
数据库工具类
'''

import pymysql;

def get_connect_cursor():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8');
    return conn,conn.cursor();

def execute_insert_update_delete(cursor,sql):
    result = cursor.execute(sql);
    return result;

def execute_query(cursor,sql):
    cursor.execute(sql);
    return cursor.fetchall();

def execute_commit(conn):
    conn.commit();

def close_connect_cursor(connection,cursor):
    connection.close();
    cursor.close();