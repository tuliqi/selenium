import logging

LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] \
    %(levelname)s %(message)s'


class feixueLogging:
    def __init__(self,
                 level=logging.DEBUG,  # 日志级别
                 format=LOGGING_FORMAT,  # 日志格式
                 datefmt='%a, %d %b %Y %H:%M:%S',  # 日期格式
                 filename='log.log',  # 日志文件名
                 filemode='w'  # 文件打开模式
                 ):
        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode = filemode

        # 初始化日志同时输出到console和日志文件
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode)

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，
        # 并将其添加到当前的日志处理对象
        console = logging.FileHandler("log.log","w")
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s \
            %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('feixueLogging').addHandler(console)
        self.log = logging.getLogger("feixueLogging")

        # 日志输出

    def logPrint(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
            logging.debug(msg)
        elif level == logging.INFO:
            # 一般的信息
            logging.info(msg)
        elif level == logging.WARNING:
            # 警告信息
            logging.warning(msg)
        elif level == logging.ERROR:
            # 错误信息
            logging.error(msg)
        else:
            # 尼玛
            logging.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.set_level(level)
