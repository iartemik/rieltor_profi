from flask import Blueprint

bp_main = Blueprint("main", __name__)
from .views import index
