class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLALCHEMY_DATABASE_URI = 'mariadb+pymysql://root:root@localhost/test1?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:dbpass@127.0.0.1:5432/test1'
