import os
class Config:
    SECRET_KEY = os.urandom(32) 
    @staticmethod
    def init_app(app):
        pass
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask:123@localhost:5432/flask_project'
    UPLOADED_PHOTOS_DEST = 'app/static/'

config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}