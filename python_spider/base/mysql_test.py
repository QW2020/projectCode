#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
mysql test
'''

import mysql_utils;

def insert_resource():
    conn, cur = mysql_utils.get_connect_cursor();
    sql = "insert into resource (resource_uri,resource_name,permission) values ('a','a','a')";
    mysql_utils.execute_insert_update_delete(cur, sql);
    mysql_utils.execute_commit(conn);
    mysql_utils.close_connect_cursor(conn,cur);

def select_resource():
    connection, cursor = mysql_utils.get_connect_cursor();
    sql = "select * from resource"
    results = mysql_utils.execute_query(cursor, sql);
    mysql_utils.close_connect_cursor(connection, cursor);
    return results;

if __name__ == "__main__":
    # select_resource();
    insert_resource();
