#Author:Xiao Jian

import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]

testcase_dir = cur_dir.replace("Common","TestDatas")

htmlreport_dir = cur_dir.replace("Common","HtmlTestReport")

logs_dir = cur_dir.replace("Common","Logs")