class ParseResponse:

    def __init__(self):
        pass

    def get_related_data(self,responsedata,exep):
        if responsedata is None or responsedata =='':
            return
        temp = exep.split("=")
        #temp[0]为提取响应表达式中的变量名
        #返回中需要定位值的key的层级list
        keys_list = temp[1].split(".")
        #将返回响应转换成字典类型
        data = eval(responsedata)
        # data[keys_list[0]][keys_list[1]]
        res = self.get_data(data,keys_list)
        return res

    def get_data(self,dictobj,keys_list):
        value = dictobj[keys_list[0]]
        if len(keys_list)>1:
            keys_list = keys_list[1:]
            res = self.get_data(value,keys_list)
            return res
        return value