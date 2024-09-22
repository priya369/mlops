class Config:
  DEBUG = False
  TESTING = False
  DATABASE_URI = 'sqlite:///:memory:'
  LOG_LEVEL = 'DEBUG'
  LOG_FILE_PATH = 'app.log'
  SECRET_KEY = 'mysecretkey'
  SECRET_COOKIES = 'mysecretcookies'
  API_ENDPOINT = 'https://api.example.com'

class ProductionConfig(Config):
  DATABASE_URI = 'mysql://user@localhost/foo'
  LOG_LEVEL = 'INFO'
  LOG_FILE_PATH = 'app.log'
  SECRET_KEY = 'mysecretkey-prod'
  SECRET_COOKIES = 'mysecretcookies'
  API_ENDPOINT = 'https://api.example.com'

class DevelopmentConfig(Config):
  DEBUG = True
  LOG_LEVEL = 'INFO'
  LOG_FILE_PATH = 'app.log'
  SECRET_KEY = 'mysecretkey-dev'
  SECRET_COOKIES = 'mysecretcookies'
  API_ENDPOINT = 'https://api.example.com'

class TestingConfig(Config):
  TESTING = True
  LOG_LEVEL = 'INFO'
  LOG_FILE_PATH = 'app.log'
  SECRET_KEY = 'mysecretkey-test'
  SECRET_COOKIES = 'mysecretcookies'
  API_ENDPOINT = 'https://api.example.com'