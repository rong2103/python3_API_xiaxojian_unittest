import unittest
from Common.DoExcel import DoExcel
import os
from Common import myRequest
import ddt
from Common import dir_config
from Common import myLogger2
import logging
import re

#实例 化日志对象
#logger = MyLogger()
# 获取所有的测试数据
excelfile = dir_config.testcase_dir + "/api_info_1.xlsx"
de = DoExcel(excelfile)
all_case_datas = de.get_caseDatas_all()
print("所有的测试数据", all_case_datas)

global_vars = {}

@ddt.ddt
class Test_Api(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        de.update_init_data()
        de.save_excelFile(excelfile)

    @ddt.data(*all_case_datas)
    def test_api(self,case_data):
        global global_vars
        # 使用for循环，读取每行测试数据，然后发送http请求。获取响应结果
        logging.info("==============开始执行一个接口测试用例，请求数据如下===============")
        logging.info("接口请求地址：%s" % case_data["url"])
        logging.info("接口请求类型：{0}".format(case_data["method"]))
        logging.info("接口请求数据为：{0}".format(case_data["request_data"]))

        #动态替换了 - 判断请求数据当中，是否要替换全局变量的值、全局变量是否存在。
        if len(global_vars)>0 and case_data["request_data"] is not None:
            for key,value in global_vars.items():
                if case_data["request_data"].find(key) != -1:
                    case_data["request_data"] = case_data["request_data"].replace(key,value)
            logging.info("动态更新之后的请求数据为：\n{0}".format(case_data["request_data"]))

        res = myRequest.myRequest(case_data["url"], case_data["method"], case_data["request_data"])

        logging.info("本次接口请求的状态码为：%d" % res.status_code)
        logging.info("接口请求的返回数据为：")
        logging.info(res.text)
        #先要判断测试数据当中，是否有关联字段。。如果有，则需要提取出来。按表达式提取，并且赋给指定变量。
        if "related_exp" in case_data.keys():
            logging.info("需要从响应结果中提取数据：")
            #related_data = parse_response.get_relatedData_from_response(res.text,case_data["related_exp"])
            temp = case_data["related_exp"].split("=")
            res_id = re.findall(temp[1],res.text)
            #动态获取了，成为全局变量。
            global_vars[temp[0]] = res_id[0]

        logging.info("接口请求的期望数据为：")
        logging.info(case_data["expected_data"])
        logging.info("期望结果与实际结果的比对方式为：")

        if int(case_data["compare_type"]) == 0:
            logging.info("全值匹配模式。")
            try:
                self.assertEqual(res.text,case_data["expected_data"])
                logging.info("结果比对成功，测试用例通过")
            except AssertionError:
                logging.exception("结果比对失败：")
                raise AssertionError
        else:
            logging.info("正则表达式匹配模式。")
            re_obj = re.match(case_data["expected_data"],res.text)
            self.assertIsNotNone(re_obj, "正则表达式匹配失败！")
        logging.info("========================结束一个接口测试用例==========================")
