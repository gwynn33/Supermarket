from flask import Blueprint
from sqlalchemy import select
from blueprints.database.models import Staff,User_account,User
from blueprints.database import get_session  


def StaffLogin(email,password): 
    with get_session() as session:
        query = select(Staff).where(Staff.staff_email == email)
        result = session.execute(query).scalars().first()
        if result :
            return result


def UserLogin(email,password):
    with get_session() as session:
        query = select(User_account).where(User_account.user_email == email)
        result = session.execute(query).scalars().first()
        if result:
            return result

def User_existence(email):
    with get_session() as session:
        query = select(User_account).where(User_account.user_email == email)
        result = session.execute(query).scalars().first()
        return result
        
            
def StaffIID(identifier):
    with get_session() as session:
        query = select(Staff).where(Staff.staff_id == identifier)
        result = session.execute(query).scalars().first()
        if result:
            return result

def UserID(identifier):
    with get_session() as session:
        query = select(User_account).where(User_account.user_id == identifier)
        result = session.execute(query).scalars().first()
        if result:
            return result


def parsed_gmail(text):
    text = text.split("@")
    username = text[0]
    return username

def parse_date(text):
    text = text.split("-")
    return text[0]


