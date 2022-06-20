# @Time : 2021/8/2 19:00
# @File : test_log.py
import logging

import pytest
from log_plugin import logger

def test_log():
    logger.info('打印INFO信息')
    logger.error('打印error信息')
    logger.error('打印error信息')


@pytest.mark.parametrize('a',['中文','测试','test'],ids=['测试1','测试2','abc'])
def test_charset(a):
    logger.info(a)

