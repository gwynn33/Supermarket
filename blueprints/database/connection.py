from sqlalchemy import text
from blueprints.database import engine
from sqlalchemy import inspect

def check_connection():
    try:
        with engine.connect() as conn:
            result= conn.execute(text("SELECT VERSION()"))
            version = result.scalar()
            print("Connected to Database!")
            print(f"Version : {version}")
            return True
    except Exception as e:
        print(f"connection failed: {e}")
        return False
    
def check_tables():
    inspector = inspect(engine)

    tables = inspector.get_table_names()

    if tables:
        print(f"Existing tables : {tables}")
    else:
        print("no tables found in the database")
    
    return tables

if __name__== "__main__":
    check_connection()
    check_tables()
