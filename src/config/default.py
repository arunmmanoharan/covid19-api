import os
import urllib

# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(str(os.getenv('SQL_AZURE_CONNSTR')))}"
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_ECHO = True if '1' == os.environ.get('SQLALCHEMY_ECHO', None) else False
SQLALCHEMY_TRACK_MODIFICATIONS = False
