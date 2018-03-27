'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
import requests

class MyRequests:
    def __init__(self,logger):
        self.logger = logger

    def myrequest(self,url,method,request_data):
        # 判断如果请求数据不为空就将请求数据转换成字典类型，如果请求数据为空就直接传数据None
        if request_data is not None:
            request_data = eval(request_data)
            self.logger.info("转换为字典后的请求数据为{0}".format(request_data))
            self.logger.info("转换为字典后的请求数据类型为{0}".format(type(request_data)))
        if method == "get":
            res = requests.get(url, request_data)
        elif method == "post":
            res = requests.post(url, request_data)
        else:
            self.logger.info("请求方法没有找到")
            res = None
        return res


# def myRequests(url,method,request_data):
#
#     #判断如果请求数据不为空就将请求数据转换成字典类型，如果请求数据为空就直接传数据None
#     if request_data is not None:
#         request_data = eval(request_data)
#     if method == "get":
#         res = requests.get(url,request_data)
#     elif method == "post":
#         res = requests.post(url,request_data)
#     else:
#         print("请求方法没有找到")
#         res = None
#     return res
