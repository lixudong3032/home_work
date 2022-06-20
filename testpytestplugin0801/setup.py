# @Time : 2021/8/2 18:49
# @Author : lixudong
# @File : setup.py.py


from setuptools import setup

setup(
    name='log_plugin',
    version='1.0',
    author="李旭东",
    author_email='50348744@qq.com',
    description='自定义日志和改变编码格式',
    long_description='已定义好日志格式实例，将日志保存至项目目录下的logs',
    classifiers=[  # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.6',
    ],
    license='proprietary',
    packages=['log_plugin'],
    keywords=[
        'pytest', 'py.test', 'log_plugin','logger','log'
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            # 会自动加载这个包下的__init__.py文件
            'log_plugin = log_plugin',
        ]
    },
    # windows才需要zip_false参数
    zip_safe=False
)
