# models/schemas.py
from pydantic import BaseModel

class CustomFieldCreate(BaseModel):
    field_name: str
    field_type: str
    field_value: str

class CustomFieldModify(BaseModel):
    field_name: str

class EmailCadenceCreate(BaseModel):
    cadence_name: str
    timing: str
    template: str

class EmailCadenceModify(BaseModel):
    timing: str
    template: str
