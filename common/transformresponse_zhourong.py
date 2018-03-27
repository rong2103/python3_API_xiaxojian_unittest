class TransformResponse:

    def __init__(self,response,expression,logger):
        self.response = response
        self.expression = expression
        self.logger = logger
        self.logger.info("TransformResponse.............")

    #返回从响应中取到的动态变量，dict1 == {'${userid}': 2146}
    def transform(self):
        self.logger.info("提取响应的表达式为:{0}".format(self.expression))
        temp_exp = self.expression.split('=')
        #temp_exp[0]==${userid}，temp_exp[1]==data.id
        self.logger.info("提取的变量为:{0}".format(temp_exp))
        self.logger.info("提取的变量名为:{0}".format(temp_exp[0]))
        #temp_exp[1]==data.id
        keys_temp = temp_exp[1].split(".")
        #keys_temp[0]=data,keys_temp[1]=id
        data = eval(self.response)
        self.logger.info("keys_temp的长度为:{0}".format(len(keys_temp)))
        for i in range(0,len(keys_temp)):
            self.logger.info("i为:{0}".format(i))
            self.logger.info("keys_temp[i]为:{0}".format(keys_temp[i]))
            data = data[keys_temp[i]]
            self.logger.info("data为:{0}".format(data))
        # value = eval(self.response)[keys_temp[0]][keys_temp[1]]
        dict1 = {}
        dict1[temp_exp[0]] = data
        self.logger.info("提取的变量字典为:{0}".format(dict1))
        #dict1 == {'${userid}': 2146}
        return dict1
