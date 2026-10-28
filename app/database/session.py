from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL="sqlite:///./test.db"

engine = create_engine(
    SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_session():
    with SessionLocal() as session:
        try:
            yield session
        finally: 
            session.close()