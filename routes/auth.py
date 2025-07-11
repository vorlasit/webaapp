from flask import Blueprint, flash, render_template, request, redirect, session ,url_for
from flask_login import login_user, logout_user, login_required, current_user
from models import User,Group
from database import db

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        group_ids = request.form.getlist('groups')

        # เช็ค email ซ้ำ
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email นี้ถูกใช้ไปแล้ว กรุณาใช้ email อื่น", "danger")
            groups = Group.query.all()
            return render_template('register.html', groups=groups, selected_group_ids=[])

        user = User(name=username, email=email)
        user.set_password(password)

        if User.query.count() == 0:
            admin_group = Group.query.filter_by(name='Admin').first()
            if admin_group:
                user.groups.append(admin_group)
        else:
            for gid in group_ids:
                group = Group.query.get(int(gid))
                if group:
                    user.groups.append(group)

        db.session.add(user)
        db.session.commit()
        flash("สมัครสมาชิกสำเร็จ", "success")
        return redirect(url_for('auth.login'))

    groups = Group.query.all()
    return render_template('register.html', groups=groups, selected_group_ids=[])


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)  # ✅ ใช้ Flask-Login จัดการ session
            return redirect(url_for('auth.dashboard'))  

        flash("Invalid email or password", "danger")

    return render_template('login.html', user=current_user)
 

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('auth.login')) 