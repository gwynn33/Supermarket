from typing import Optional
from sqlalchemy import ForeignKey,String,Integer,DateTime,Boolean,Date
from sqlalchemy.orm import mapped_column,relationship,Mapped
from blueprints.database import Base
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash
import traceback

try:

    class User(Base):
        __tablename__ = "user"
        user_id : Mapped[int] = mapped_column(Integer,ForeignKey("user_account.user_id"),primary_key=True)
        user_fullname : Mapped[str] = mapped_column(String(50),nullable=False)
        user_region : Mapped[str] = mapped_column(String(50),nullable=False)
        user_phone: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
        user_sign_up_date : Mapped[Date] = mapped_column(Date,nullable=False)
        user_sexe : Mapped[str] = mapped_column(String(10),nullable=False)
        user_age : Mapped[int]  = mapped_column(Integer,nullable=False)
        user_loyality: Mapped[bool] = mapped_column(Boolean,nullable=False)
        user_ordering_count: Mapped[int] = mapped_column(Integer,nullable=True)
        
        def __repr__(self):
            return f"User: user_id : {self.user_id}"
  
    """Related to flask-login"""
    class User_account(Base,UserMixin):
        __tablename__ = "user_account"
        user_id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
        user_email: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
        user_password: Mapped[str] = mapped_column(String(256),nullable=False)
        is_user : Mapped[bool] = mapped_column(Boolean,nullable=True)
    
        def set_password(self,password):
            self.user_password = generate_password_hash(password)
        
        def check_password(self,password):
            return check_password_hash(self.user_password,password)
        
        def get_id(self):
            return str(self.user_id)
        
        def __repr__(self):
            return f"User : user_id : {self.user_id}"

    class Admin(Base,UserMixin):
        __tablename__ = "admin"
        admin_id:Mapped[int] = mapped_column(Integer,primary_key=True)
        admin_email: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
        admin_password: Mapped[str] = mapped_column(String(256),nullable=False)

        def set_password(self,password):
            self.admin_password = generate_password_hash(password)
        
        def check_password(self,password):
            return check_password_hash(self.admin_password,password)
        
        def get_id(self):
            return str(self.admin_id)

        def __repr__(self):
            return f"Admin : admin_id : {self.admin_id}"

    class Staff(Base,UserMixin):
        __tablename__ = "staff"
        staff_id: Mapped[int] = mapped_column(Integer,primary_key=True)
        staff_email: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
        staff_password: Mapped[str] = mapped_column(String(256),nullable=False)
        is_staff: Mapped[bool] = mapped_column(Boolean,nullable=True)

        def set_password(self,password):
            self.staff_password = generate_password_hash(password)
        
        def check_password(self,password):
            return check_password_hash(self.staff_password,password)

        def get_id(self):
            return str(self.staff_id)
        
        def __repr__(self):
            return f"Staff : staff_id : {self.staff_id}"
    
    """end here"""

    class Product(Base):
        __tablename__ = "product"
        product_id: Mapped[int] = mapped_column(Integer,primary_key=True)
        product_name: Mapped[str] = mapped_column(String(50),nullable=False)
        product_categorie: Mapped[str] = mapped_column(String(50),nullable=False)
        product_price: Mapped[int] = mapped_column(Integer,nullable=False)
        current_stock_quantity: Mapped[int] = mapped_column(Integer)
        product_entering_date: Mapped[Date] = mapped_column(Date,nullable=False)
        product_expiration_date: Mapped[Date] = mapped_column(Date,nullable=True)

        def __repr__(self):
            return f"Product : product_id : {self.product_id}"

    class Order(Base):
        __tablename__ = "orders"
        order_id: Mapped[int] = mapped_column(Integer,primary_key=True)
        user_id: Mapped[int] = mapped_column(Integer,ForeignKey("user_account.user_id"))
        product_id: Mapped[int] = mapped_column(ForeignKey("product.product_id"))
        order_date: Mapped[Date] = mapped_column(Date,nullable=False)
        product_quantity: Mapped[int] = mapped_column(Integer,nullable=False)
        order_total_price: Mapped[int] = mapped_column(Integer,nullable=False)

        def __repr__(self):
            return f"Order : order_id : {self.order_id}"

    class StockHistory(Base):
        __tablename__ = "stock_history"
        stock_history_id: Mapped[int] = mapped_column(Integer,primary_key=True)
        product_id: Mapped[int] = mapped_column(ForeignKey("product.product_id"))
        quantity_change: Mapped[int] = mapped_column(Integer,nullable=True)
        quantity_after: Mapped[int] = mapped_column(Integer,nullable=True)
        change_date: Mapped[Date] = mapped_column(Date,nullable=False)
        change_type: Mapped[str] = mapped_column(String(50),nullable=False)

        def __repr__(self):
            return f"StockHistory : stock_history_id : {self.stock_history_id}"

except Exception as e:
    print(f"-------Error--------\n {e}")
    print(f"==================Detailed Error================\n {traceback.print_exc}")
