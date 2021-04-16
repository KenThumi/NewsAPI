import os

class Config:

    MOVIE_API_BASE_URL ='https://newsapi.org/v2/everything?domains={}&language=en&apiKey={}'
    # MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    MOVIE_API_KEY = '67c96776ccc842ccb9801da1ee781ca4'
    SECRET_KEY = 'ec31c80971d3d27c0f7803135c057c84'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}