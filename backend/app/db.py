from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# We connect to the docker container database using the following structure:
# postgresql://{user}:{password}@{ip:port}/{database}
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/user_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

