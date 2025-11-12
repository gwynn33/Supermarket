from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import traceback

try:
    DATABASE_URL = "mysql+pymysql://gwynn:gwynnistrash12%40%40@localhost:3306/hormarket"

    engine = create_engine(
        DATABASE_URL,
        echo=True,
        pool_pre_ping=True
    )

    SessionLocal = sessionmaker(bind=engine)

    class Base(DeclarativeBase):
        pass

    def get_session():
        return SessionLocal()

except Exception as e:
    print(f"-------Error--------\n {e}")
    print(f"==================Detailed Error================\n {traceback.print_exc}")