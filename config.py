import psycopg2
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://doyo:doyo123@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='1234'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://uvwvmkiqhgfubf:abe513190f4f7f07835a812186460cc53c065e6e4ace40ddaf28182a21fc02af@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d7i76dml2jcpeh'
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

    
config_options = {
'development':DevConfig,
'production':ProdConfig
}