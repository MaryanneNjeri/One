import os

class Config:
    PIX_BASE_URL = 'https://pixabay.com/api/?key={}&category={}&image_type=photo'
    PIX_API_KEY=os.environ.get('PIX_API_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maryanne:mustu.cat@localhost/onepitch'

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG =True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
