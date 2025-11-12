from flask import Blueprint,request,render_template
from flask_login import login_required,current_user
from sqlalchemy import select
from blueprints.fn.functions import parsed_gmail
from blueprints.database.models import Staff
from blueprints.database import get_session
import traceback

staff_bp = Blueprint("staff_bp",__name__)

@staff_bp.route('/staff_page',methods = ['GET','POST'])
@login_required
def staff():
    if request.method == 'GET':
        user = int(current_user.get_id())
        with get_session() as session:
            query = select(Staff).where(Staff.staff_id == user)
            statement = session.execute(query).scalars().first()
            username =  statement.staff_email

        username = parsed_gmail(username)
        return render_template("staff_bp.html",username = username)
        