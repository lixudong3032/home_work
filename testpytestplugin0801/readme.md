打包一个日志插件步骤：
1.创建一个包log_plugin，在__init__.py写下日志方法
2.在包log_plugin同级目录下创建setup.py文件，并且修改打包信息
3.打开终端打包python setup.py sdist bdist_wheel，这样多了dist目录，并且2个文件。打包依赖pip install setuptools  pip install wheel
4.进行插件安装 python setup.py install

