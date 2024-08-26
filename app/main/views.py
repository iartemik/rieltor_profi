from . import bp_main
from app import render_template


@bp_main.route("/", methods=["GET"])
@bp_main.route("/index")
def index():
    return render_template("index.html")
