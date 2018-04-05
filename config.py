# http://flask-docs-kr.readthedocs.io/ko/latest/config.html

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500

    # Cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    SWAGGER_UI_JSONEDITOR = True

    PHASE = "alpha"
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = False
    TESTING = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 10

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    SAMPLE_DATA_PATH="sample_data"


class TestConfig(Config):
    DEBUG = True
    TESTING = False
    DATABASE_URI = ""
    CPU_COUNT = 4


class DevConfig(Config):
    DEBUG = True
    DATABASE_URI = ""
    CPU_COUNT = 4


class AlphaConfig(Config):
    PHASE = "alpha"
    DATABASE_URI = ""
    CPU_COUNT = 2


class RealConfig(Config):
    PHASE = "real"
    DATABASE_URI = ""
    CPU_COUNT = 8
