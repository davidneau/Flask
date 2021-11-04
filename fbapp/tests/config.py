import os
SECRET_KEY = 'votre_nouvelle_cle_secrete'

# Remplacez par l'id de l'app TEST que vous avez créée précédemment.
FB_APP_ID = 12345678901234567890

basedir = os.path.abspath(os.path.dirname(__file__))

# Nouvelle base de données pour les tests.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

# Facebook test user
FB_USER_NAME = "Test user"
FB_USER_PW = "Duragon-49"
FB_USER_EMAIL = "test_schlcyw_user@tfbnw.net"
FB_USER_ID = 111205844698279
FB_USER_GENDER = 'male'
