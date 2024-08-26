from flask import Flask, render_template, redirect, flash, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from app.config import Config


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

from app.main import *
from app.reg_auth import *
from .models.Client import Client
from .models.Rieltor import Rieltor
