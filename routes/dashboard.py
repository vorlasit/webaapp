from flask import Blueprint, current_app, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db
import os
from werkzeug.utils import secure_filename
from . import auth_bp

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

 