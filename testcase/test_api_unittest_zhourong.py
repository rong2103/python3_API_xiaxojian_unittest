import unittest
from common import dirconfig_zhourong
from common.log_zhourong import Log
from common.myexcel_zhourong import MyExcel
from common.myrequests_zhourong import MyRequests
from common.transformresponse_zhourong import TransformResponse
import ddt
import time
import re

#new logger
now = time.strftime('%Y-%m-%d_%H_%M_%S')
logger = Log("zhourong", dirconfig_zhourong.logger_dir + "/log" + now + ".txt")
#从testdata文件中读取测试用例作为测试用例的传入参数
filename = dirconfig_zhourong.testcase_dir + "/api.xlsx"
sheetname1 = "Sheet1"
sheetname2 = "variables"
fileobj = MyExcel(filename,logger)
init_variables = fileobj.get_init_variables(sheetname2)
testdatas = fileobj.getallrow(sheetname1)
request = MyRequests(logger)
dynamic_varis_dict = {}

@ddt.ddt
class TestAPI(unittest.TestCase):
    #tearDown与tearDownClass的区别：
    # 前者每个用例前后都要执行（有多少个测试用例就执行多少次）；
    # 后者在测试类中所有用例执行前后执行一次（只执行一次）

    @classmethod
    def tearDownClass(cls):
        #更新注册的电话号码变量
        fileobj.update_init_data(sheetname2,2,2)
        fileobj.savefile(filename)

    #@ddt.data(*testdatas)中参数不能用self.testdatas的形式，所以将testdatas的数据放在类外面
    #有ddt之后就不用for循环了
    @ddt.data(*testdatas)
    def test_api(self,testdata):
        global dynamic_varis_dict
        logger.info("=====================接口测试开始=====================")
        logger.info("现在执行的测试用例数据为：{0}".format(testdata))
        logger.info("请求url为：{0}".format(testdata["url"]))
        logger.info("请求http_method为：{0}".format(testdata["http_method"]))
        logger.info("请求request_data为：{0}".format(testdata["request_data"]))
        logger.info("请求request_data类型为：{0}".format(type(testdata["request_data"])))
        logger.info("请求related_expression为：{0}".format(testdata["related_expression"]))
        logger.info("请求related_expression类型为：{0}".format(type(testdata["related_expression"])))
        ################################
        # # if testdata["request_data"].find()
        #判断请求是否需要替换
        logger.info("dynamic_varis_dict:{0}".format(dynamic_varis_dict))
        dynamic_varis_len = len(dynamic_varis_dict)
        logger.info("动态变量的长度为：{0}".format(dynamic_varis_len))
        if len(dynamic_varis_dict) == 0:
            pass
        else:
            for key,value in dynamic_varis_dict.items():
                logger.info("动态变量的key为：{0}".format(key))
                if testdata["request_data"].find(key)!= -1:
                     logger.info("请求中包含key")
                     testdata["request_data"] = testdata["request_data"].replace(key, str(value))
        res = request.myrequest(testdata["url"], testdata["http_method"],testdata["request_data"])
        logger.info("返回的响应数据为：{0}".format(res.text))
        logger.info("期望结果为为：{0}".format(testdata["expected_data"]))
        # 判断该用例是否要做响应数据提取
        if testdata["related_expression"] =="None":
            logger.info("不需要做响应提取")
        else:
            # testdata["related_expression"] is not None:
            logger.info("需要做响应提取")
            # # print("is not none")
            # # 调用响应数据提取的函数，提取需要的变量的值并写入excel的变量sheetname中,保存
            # #new TransformResponse
            # trans = TransformResponse(res.text, testdata["related_expression"], logger)
            # vari_dict = trans.transform()
            # #vari_dict == {'${userid}': 2146}
            # logger.info("动态提取的变量字典vari_dict为：{0}".format(vari_dict))
            # #update动态变量字典
            # dynamic_varis_dict.update(vari_dict)
            # logger.info("动态提取的所有变量字典dynamic_varis_dict为：{0}".format(dynamic_varis_dict))
            # #################################################################################################
            # # #如何替换呢
            # # 再接下来的用例数据中继续判断测试请求中是否包含动态变量的key；如果包含则替换；
            # ##########  要在请求之前替换
            temp = testdata["related_expression"].split("=")
            # .*"id":(\d*).*
            #['2211']
            res_id = re.findall(temp[1],res.text)[0]
            logger.info("res_id".format(res_id))
            #{"$user_id":"2211"}
            dynamic_varis_dict[temp[0]] = res_id
        if int(testdata["compare_type"]) == 0:
            logger.info("全值匹配断言")
            assert res.text == testdata["expected_data"]
        elif int(testdata["compare_type"]) == 1:
            logger.info("部分匹配断言")
            # 可用正则表达式，更灵活
            self.assertIn(testdata["expected_data"],res.text)
        logger.info("=====================接口测试结束=====================")













