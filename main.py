from flask import Flask,session
from blueprints.main_bp_page.main_bp import main_bp
from blueprints.login_bp_page.login_bp import login_bp
from blueprints.signin_bp_page.signin_bp import signin_bp
from blueprints.cli_commands.recreate_all import recreate_bp
from blueprints.cli_commands.crud_operations import crud_bp
from blueprints.staff_bp_page.staff_bp import staff_bp
from blueprints.market_bp_page.market_bp import market_bp
# from blueprints.login_bp_page.logout_bp import logout_bp
from flask_login import LoginManager
from blueprints.database.models import User_account,Staff
from blueprints.fn.functions import StaffIID,UserID

def create_app():
    
    app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')
    app.secret_key = "gwynn-super-key"
    
    """Blueprints Registration For Routes"""
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(signin_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(market_bp)

    """Blueprints Registration For Cli Commands"""
    app.register_blueprint(recreate_bp)
    app.register_blueprint(crud_bp)

    """flask-login & connecting it with Flask"""
    #Creating the LoginManager instance
    login_manager = LoginManager()
    #connecting it with Our app
    login_manager.init_app(app)


    """This Part is to be used by @login_required ("decorator")"""
    @login_manager.user_loader
    def user_load(user_id):
        user_id = int(user_id)

        staff = StaffIID(user_id)
        if staff:
            return staff
        
        user = UserID(user_id)
        if user:
            return user


    return app

#initializing the application
app = create_app()


#for debugging and tracking the HTTP requests
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5555',debug=True)

