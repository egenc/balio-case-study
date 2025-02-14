# config/database.py
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./data/test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CustomField(Base):
    __tablename__ = "custom_fields"
    id = Column(Integer, primary_key=True, index=True)
    field_name = Column(String, index=True)
    field_type = Column(String)
    field_value = Column(Text)

class EmailCadence(Base):
    __tablename__ = "email_cadences"
    id = Column(Integer, primary_key=True, index=True)
    cadence_name = Column(String, index=True)
    timing = Column(String)
    template = Column(Text)

Base.metadata.create_all(bind=engine)
