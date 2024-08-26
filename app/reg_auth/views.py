from app import *
from . import bp_login


@login_manager.user_loader
def load_user(user_id):
    user = Client.query.get(int(user_id))
    if user is None:
        user = Rieltor.query.get(int(user_id))
    return user


@bp_login.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Client.query.filter_by(username=username).first()
        if user is None:
            user = Rieltor.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("dashboard"))
    return render_template("login.html")


@bp_login.route("/login", methods=["POST"])
def register():
    return redirect(url_for("auth.login"))


@bp_login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
