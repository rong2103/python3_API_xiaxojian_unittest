from common.excel_operation import ExcelOperation
from common import myrequest
import os

filename = os.getcwd().replace("testcase","testdata")+"/api.xlsx"
sheetname = "Sheet1"
ex = ExcelOperation(filename,sheetname)
maxrow = ex.getmaxrows()
maxcol = ex.getmaxcols()
for i in range(2,ex.getmaxrows()+1):
    url = ex.readexcel(i,3)
    print(url)
    method = ex.readexcel(i,4)
    print(method)
    data = ex.readexcel(i,5)
    print(data)
    res = myrequest.myRequests(url,method,eval(data))
    print(res.status_code)
    assert res.text == eval(ex.readexcel(i,6))
    #如果让断言失败不影响用例继续运行
    #如何实现手机注册号码自动变化



    #eval