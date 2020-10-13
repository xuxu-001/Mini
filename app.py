import logging.handlers, os


# 初始化日志配置
def log_config():
    # 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建处理器(控制台处理器、文件处理器)
    sh = logging.StreamHandler()

    # 日志文件目录
    logpath = "./log"
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logpath + os.sep + "mini.log", when="midnight",
                                                     interval=1, backupCount=15, encoding="UTF-8")
    # file_path = BASE_DIR + "/log/ihrm.log"
    # trfh = logging.handlers.TimedRotatingFileHandler(file_path, when="midnight",
    #                                               interval=1, backupCount=15, encoding="UTF-8")

    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"
# 微信code
<<<<<<< HEAD
code = "081uT2ll2wTFM54eamml2KN4tp1uT2ld"
=======
code = "001Qoe100Nz9rK1JVx0002rBol2Qoe14"
>>>>>>> c96be8805a26476689d67208bb8a5cfe4dcbef77
# 请求头
headers = {
    "Content-Type": "application/json",
    "token": '1577d7e7c5a507f699bb77398081735d'

}
