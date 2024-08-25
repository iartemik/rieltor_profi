from app import *



def create_app(config):
    app = Flask(__name__,template_folder='./app/templates',static_folder='./app/static')
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_login)#регистрация марушрутной области
    login_manager.init_app(app)
    with app.app_context():
           db.create_all()
    return app 


app=create_app(Config)
if __name__ == '__main__':
          app.run(debug=True)
         
     
