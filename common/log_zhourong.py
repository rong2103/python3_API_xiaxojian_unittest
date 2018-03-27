import logging

class Log:
    def __init__(self,log_name,file_name):
        #日志收集器的名字
        self.log_name = log_name
        #日志文件的名字
        self.file_name = file_name

    def logger(self,level,msg):
    # def logger(self):
        #日志收集器
        mylog = logging.getLogger(self.log_name)
        mylog.setLevel("DEBUG")
        #日志过滤器
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        fh = logging.FileHandler(self.file_name,encoding='utf-8')
        fh.setFormatter(formatter)
        fh.setLevel("DEBUG")

        mylog.addHandler(fh)
        if level.upper()=="DEBUG":
            mylog.debug(msg)
        elif level.upper()=="INFO":
            mylog.info(msg)
        elif level.upper()=="WARNING":
            mylog.warning(msg)
        elif level.upper()=="ERROR":
            mylog.error(msg)
        elif level.upper()=="CRITICAL":
            mylog.critical(msg)
        else:
            mylog.exception(msg)

        mylog.removeHandler(fh)


    # 定义各种日志级别的方法
    def debug(self, msg):
        self.logger("debug", msg)

    def info(self, msg):
        self.logger("info", msg)

    def error(self, msg):
        self.logger("error", msg)

    def warning(self, msg):
        self.logger("warning", msg)

    def critical(self, msg):
        self.logger("critical", msg)

    def exception(self,msg):
        self.logger("exception", msg)