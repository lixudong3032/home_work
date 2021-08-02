# @Time : 2021/8/2 18:54
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : __init__.py.py
import logging
import os
from typing import List


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]):
    '''
    修改用例使用参数化时中文的名称问题
    :param session:
    :param config:
    :param items:
    :return:
    '''
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # 用例名字
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # 用例路径


LOGGING_DEFAULT_LEVEL = logging.DEBUG  # 默认级别
LOGGING_FILE_LEVEL = logging.DEBUG  # 输出文件级别
LOGGING_CONSOLE_LEVEL = logging.DEBUG  # 输出到控制级别  ，备注：调用等级没有超过默认等级将不会有输出；而其他的调用等级超过默认等级的时候，日志记录的就是调用等级。


def plugin_logger():
    '''
    自定义日志格式写入调用项目的logs目录下
    :return:
    '''
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_DEFAULT_LEVEL)

    if not os.path.exists('./logs'):  # 判断logs文件是否存在
        os.makedirs('./logs')
    formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")  # 设置日志输出/打印格式

    file_haddler = logging.FileHandler("./logs/report.log", encoding="utf-8", mode='w')
    file_haddler.setLevel(LOGGING_FILE_LEVEL)  # 设置输出到文件最低日志级别
    file_haddler.setFormatter(formatter)
    logger.addHandler(file_haddler)

    console_haddler = logging.StreamHandler()  # 输出到控制台
    console_haddler.setLevel(LOGGING_CONSOLE_LEVEL)  # 设置输出到文件最低日志级别
    console_haddler.setFormatter(formatter)
    logger.addHandler(console_haddler)

    return logger


logger = plugin_logger()