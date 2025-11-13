from flask import Blueprint,render_template,request,jsonify
from blueprints.database.models import User,User_account
from blueprints.fn.functions import User_existence,parse_date
from blueprints.database import get_session
import traceback
from datetime import datetime


signin_bp = Blueprint("signin_bp",__name__)

@signin_bp.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == "GET":
        return render_template("signin_bp.html")

    if request.method == "POST":
        try:
            data = request.get_json()
            if not data: 
                raise ValueError("Data Corrupted")
            
            email = data.get("email")
            fullname = data.get("full_name")
            region = data.get("city")
            phone = data.get("phone")
            birth = data.get("birth")
            gender = data.get("gender")
            password = data.get("password")

            date_obj = datetime.strptime(birth,"%Y-%m-%d")
            now = datetime.now()
            age = now.year - date_obj.year - (
            (now.month, now.day) < (date_obj.month, date_obj.day)
            )
            
            if age < 18: 
                raise ValueError("Too Young Bro!")

            sign_up_date = datetime.now().strftime("%Y-%m-%d")

            result = User_existence(email)

            if result :
                raise ValueError("This User is Already Exist!")


            with get_session() as session:
                
                user_account_data = User_account(
                    user_email = email,
                )        
                user_account_data.set_password(password)
                session.add(user_account_data)
                session.flush()
                
                user_data = User(
                    user_id = user_account_data.user_id,
                    user_fullname = fullname,
                    user_region = region,
                    user_phone = phone,
                    user_sign_up_date = sign_up_date,
                    user_sexe = gender,
                    user_age = age,
                    user_loyality = 0,
                )    
                session.add(user_data)
                session.commit()
                return jsonify({"success":True,"message":"Data commited successfully!"})

        except Exception as e:
            print("======Error======")
            print(str(e))
            print("==========Detailed Error==========")
            traceback.print_exc()
            return jsonify({"success":False,"error":f"Something Wrong {e}"}),401

