class BasecConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcdef123456'
    DEBUG = False
    TESTING= False

class DEVCONFIG(BasecConfig):
    DEBUG = True
    TESTING = True

class TestingConfig():
    DEBUG = False
    TESTING = True

    