from flask import Flask
from config import Config
from database import db
from routes import auth_bp
from models import User, Group 
from flask_login import LoginManager
import os
import sys

sys.path.append(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)

# ✅ Setup Database
db.init_app(app)

# ✅ Setup Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# ✅ user_loader สำหรับ Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ Register Routes
app.register_blueprint(auth_bp)

# ✅ สร้าง DB และ Group ตัวอย่าง
with app.app_context():
    # db.drop_all()
    db.create_all()
    if not Group.query.first():
        db.session.add_all([
            Group(name='Admin'),
            Group(name='Editor'),
            Group(name='Viewer')
        ])
        db.session.commit() 

# ✅ Run App
if __name__ == '__main__':
    app.run(debug=True)
