'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
import os
from common.myexcel_zhourong import MyExcel
from common import myrequests_zhourong

filename = os.path.abspath('..')+"/testdata/apitest.xlsx"
sheetname = "Sheet1"

#获取所有的测试数据，并发送请求
obj = MyExcel(filename,sheetname)
all_test_data = obj.getallrow()
print(all_test_data)
for testdata in all_test_data:
    print(testdata)
    res = myrequests_zhourong.myRequests(testdata["url"], testdata["http_method"], testdata["request_data"])
    # print(testdata[0]["url"])
    # print(testdata[0]["http_method"])
    # print(testdata[0]["request_data"])

    print(res.json())