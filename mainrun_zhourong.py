'''
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-
import unittest
import time
import HTMLTestRunnerNew
from testcase.test_api_unittest_zhourong import TestAPI
from common import dirconfig_zhourong

suite = unittest.TestSuite()
ts = unittest.TestLoader()
suite.addTest(ts.loadTestsFromTestCase(TestAPI))

#生成测试报告
now = time.strftime('%Y-%m-%d_%H_%M_%S')
filepath = dirconfig_zhourong.html_report + "/PyResult" + now + ".html"
fp = open(filepath,"wb")

runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title="单元测试",verbosity=2)
runner.run(suite)

fp.close()