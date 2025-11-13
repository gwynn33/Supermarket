from blueprints.database.models import Staff
from werkzeug.security import check_password_hash
from flask_login import login_user,logout_user
from blueprints.fn.functions import StaffLogin,UserLogin
from flask import render_template,request,Blueprint,jsonify,redirect,url_for,session
import traceback

login_bp = Blueprint('login_bp',__name__)
logout_bp = Blueprint('logout_bp',__name__)

@login_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_bp.html')
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                raise ValueError("Something Wrong With The Data!")

            email = data.get("form_email")
            password = data.get("form_password")
            Type = data.get("type")

            """Staff Login"""

            if Type == "admin":
                result = StaffLogin(email,password)

                if result and result.check_password(password):
                    session["staff_id"] = result.staff_id
                    login_user(result)
                    # return redirect(url_for('staff_bp.staff'))
                    return jsonify({"success":True,"message":"Valid Cardentials","type":"admin"})
                else:
                    return jsonify({"success":False,"error":"Invalid Cardentials"}),401
            
            """Regular User Login"""
            if Type == "user":
                result = UserLogin(email,password)
                if result and result.check_password(password):
                    login_user(result)
                    return jsonify({"success":True,"message":"Valid Cardentials","type":"user"})
                else:
                    return jsonify({"success":False,"error":"Invalid Cardentials"})
                    


        except Exception as e : 
            print("=========Error=========")
            print(str(e))
            print("==========Detailled Error=========")
            traceback.print_exc()
            return jsonify({"success":False,"error":f"Something Wrong : {e}"}),401

@logout_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.main'))
