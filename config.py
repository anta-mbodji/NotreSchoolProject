import os 

class config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    database = 'schoolproject'
    user = 'root'
    password = 'postGres'
    host = 'localhost'
    port = '5432'