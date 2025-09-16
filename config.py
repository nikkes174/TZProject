from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(os.getenv("DB_PASS"))

Base = automap_base()

Session = sessionmaker(bind=engine)

session = Session()


def close_session():
    session.close()