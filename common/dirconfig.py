import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]

testcase_dir = cur_dir.replace("common","testdata")

html_report = cur_dir.replace("common","testreport")

logger_dir = cur_dir.replace("common","logs")