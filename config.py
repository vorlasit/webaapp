

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://myapp_user:myapp_pass@localhost/myapp_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
