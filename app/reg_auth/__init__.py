from flask import Blueprint

bp_login = Blueprint("auth", __name__)
from .views import load_user, login, logout
