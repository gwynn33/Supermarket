from blueprints.database import engine,Base

from blueprints.database.models import User,Admin,User_account,Product,Staff,StockHistory,Order
from blueprints.database.connection import check_tables

def create_all_tables():
    Base.metadata.create_all(engine)
    print("Tables created successfully")

def drop_all_tables():
    Base.metadata.drop_all(engine)
    print("Tables dropped successfully")

def recreate_tables():
    drop_all_tables()
    create_all_tables()

if __name__ == "__main__":
    create_all_tables()
    check_tables()
