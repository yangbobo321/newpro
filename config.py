class BaseConfig(object):
    SECRET_KEY = 'HELLO'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/myblog"

class TestingConfig(BaseConfig):
    pass
class ProductionConfig(BaseConfig):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

