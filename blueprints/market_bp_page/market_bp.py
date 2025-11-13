from flask import Blueprint,render_template,jsonify,request
from blueprints.database.models import User
from sqlalchemy import select
from blueprints.fn.functions import parsed_gmail
from flask_login import login_required,current_user
from blueprints.database import get_session
import traceback

market_bp = Blueprint("market_bp",__name__)

@market_bp.route('/Hormarket',methods=["GET","PUT"])
@login_required
def market():
    user = int(current_user.get_id())
    with get_session() as session:
        query = select(User).where(User.user_id == user)
        statement = session.execute(query).scalars().first()
        username = statement.user_fullname
    username = parsed_gmail(username)

    if request.method == "GET":
        return render_template("market_bp.html",username=username)
    