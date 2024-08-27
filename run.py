# Разработать платформу "Риелтор-Профи". Она должна включать следующие компоненты:
# 1. Система регистрации и аутентификации для клиентов и риелторов.
# 2. Возможность выбора риелтора клиентом.
# 3. Реализовать чат для общения в реальном времени.
# 4. Личные кабинеты для клиентов и риелторов.
# 5. Возможность размещения объявлений риелторами.
# 6. Система отзывов и рейтингов.
from app import *


def create_app(config):
    app = Flask(
        __name__, template_folder="./app/templates", static_folder="./app/static"
    )
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(bp_main)  # регистрация маршрутной области
    app.register_blueprint(bp_login)
    login_manager.init_app(app)
    return app


app = create_app(Config)
if __name__ == "__main__":
    app.run(debug=True)
