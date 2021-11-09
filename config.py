import os


class DevConfig(object):
    '''项目配置文件'''
    # 数据库链接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/qa_flask'
    # flask\wtf
    SECRET_KEY = '12345'
    # 文件上传
    UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'upload_path')
    # 去除警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True