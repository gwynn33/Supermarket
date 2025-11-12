from flask import Blueprint,render_template,jsonify,request
from flask_login import login_required,current_user
import traceback

market_bp = Blueprint("market_bp",__name__)

@market_bp.route('/Hormarket',methods=["GET","PUT"])
@login_required
def market():
    if request.method == "GET":
        print(current_user)
        return render_template("market_bp.html")
    