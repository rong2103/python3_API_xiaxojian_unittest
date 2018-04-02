from Common.DoExcel import DoExcel
from Common import myRequest
import os


#获取所有的测试数据
de = DoExcel(os.getcwd().replace("TestCases","TestDatas") + "/api_info.xlsx")
all_case_datas = de.get_caseDatas_all()

print("所有的测试数据",all_case_datas)
#使用for循环，读取每行测试数据，然后发送http请求。获取响应结果
for case_data in all_case_datas:
    print("请求数据：")
    print(case_data)
    res = myRequest.myRequest(case_data["url"],case_data["method"],eval(case_data["request_data"]))
    print("响应结果：")
    print(res.status_code)
    print(res.text)
    assert res.text == case_data["expected_data"]

#比对响应结果和期望结果

