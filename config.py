import os

class Config:
    PIX_BASE_URL = 'https://pixabay.com/api/?key={}&category={}'
    PIX_API_KEY=os.environ.get('PIX_API_KEY')


class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG =True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
