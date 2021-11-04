import os

FB_APP_ID = 2786053421693847

SECRET_KEY = "I-9ygE]fhs_hGa1_bRn6g->8"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
