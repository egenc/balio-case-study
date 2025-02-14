# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine, CustomField, EmailCadence
from api.mock_functions import mock_hubspot_api_call, mock_upso_api_call
from models.schemas import CustomFieldCreate, CustomFieldModify, EmailCadenceCreate, EmailCadenceModify

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Orchestra Configuration Engine API"}

@app.post("/add_custom_field/")
def add_custom_field(custom_field: CustomFieldCreate, db: Session = Depends(get_db)):
    field = CustomField(field_name=custom_field.field_name, field_type=custom_field.field_type, field_value=custom_field.field_value)
    db.add(field)
    db.commit()
    db.refresh(field)
    mock_hubspot_api_call("add", custom_field.field_name, custom_field.field_type, custom_field.field_value)
    return field

@app.put("/modify_custom_field/{field_id}")
def modify_custom_field(field_id: int, custom_field: CustomFieldModify, db: Session = Depends(get_db)):
    field = db.query(CustomField).filter(CustomField.id == field_id).first()
    if not field:
        raise HTTPException(status_code=404, detail="Field not found")
    field.field_name = custom_field.field_name
    db.commit()
    db.refresh(field)
    mock_hubspot_api_call("modify", custom_field.field_name)
    return field

@app.post("/add_email_cadence/")
def add_email_cadence(email_cadence: EmailCadenceCreate, db: Session = Depends(get_db)):
    cadence = EmailCadence(cadence_name=email_cadence.cadence_name, timing=email_cadence.timing, template=email_cadence.template)
    db.add(cadence)
    db.commit()
    db.refresh(cadence)
    mock_upso_api_call("add", email_cadence.cadence_name, email_cadence.timing, email_cadence.template)
    return cadence

@app.put("/modify_email_cadence/{cadence_id}")
def modify_email_cadence(cadence_id: int, email_cadence: EmailCadenceModify, db: Session = Depends(get_db)):
    cadence = db.query(EmailCadence).filter(EmailCadence.id == cadence_id).first()
    if not cadence:
        raise HTTPException(status_code=404, detail="Cadence not found")
    cadence.timing = email_cadence.timing
    cadence.template = email_cadence.template
    db.commit()
    db.refresh(cadence)
    mock_upso_api_call("modify", email_cadence.timing, email_cadence.template)
    return cadence
