#!/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "HymanQin";

'''
results
'''

class Result(object):
    def __init__(self,status,message):
        self.message =message;
        self.status = status;

    def result(self):
        return {"status":self.status,"message":self.message};