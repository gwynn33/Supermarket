from blueprints.database.models import Staff,User
from blueprints.database import get_session
from flask import Blueprint
import traceback
import click
import datetime

crud_bp = Blueprint('crud_bp',__name__)


""" This command to add staff members """
@crud_bp.cli.command('add_staff')
@click.argument('staff_identifier',type=int,required=True)
@click.argument('staff_email',required=True)
@click.argument('staff_password',required=True)
def add_staff(staff_identifier,staff_email,staff_password):
    try:
        #in this line we will call the session to let us interact with our tables
        session = get_session()
        
        
        #adding data to the table
        staff = Staff(
            staff_id = staff_identifier,
            staff_email = staff_email.strip()
        )

        #hashing the password
        staff.set_password(staff_password.strip())

        session.add(staff)
        session.commit()
        click.echo("Done!")

    except Exception as e: 
        session.rollback()
        click.echo(f"==============Error==============")
        click.echo(str(e))
        click.echo(f"==============Detailled Error==============")
        traceback.print_exc()

"""This command to add a costumer informations """
@crud_bp.cli.command('add_user_info')
@click.argument('user_identifier',type=int,required=True)
@click.argument('firstname',required=True)
@click.argument('lastname',required=True)
@click.argument('region',required=True)
@click.argument('phone',required=True)
@click.argument('signup_date',required=True,type=click.DateTime(formats=["%Y-%m-%d"]))
@click.argument('sexe',required=True)
@click.argument('age',required=True)
@click.argument('loyality',required=True,default=0)
def add_user_info(user_identifier,firstname,lastname,region,phone,signup_date,sexe,age,loyality):
    try:
        #in this line we will call the session to let us interact with our tables
        session = get_session()

        fullname = firstname + lastname
        user = User(
            user_id = user_identifier,
            user_fullname = fullname.strip(),
            user_region = region.strip(),
            user_phone = phone.strip(),
            user_sign_up_date = signup_date,
            user_sexe = sexe.strip(),
            user_age = age.strip(),
            user_loyality = loyality
        )

        session.add(user)
        session.commit()
        click.echo("Done!")

    except Exception as e :
        session.rollback()
        click.echo(f"==============Error==============")
        click.echo(str(e))
        click.echo(f"==============Detailled Error==============")
        traceback.print_exc()



