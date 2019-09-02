# 配置文件
import os

users =  {'id':'root', 'username': 'root', 'password': '123456'}
urls = []

class Common():
    SECRET_KEY = 'this is a secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'img.db')
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/images'
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass