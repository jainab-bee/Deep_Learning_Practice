from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Annotated, Optional

class Patient(BaseModel):
    # Enforcing strict constraints and attaching metadata
    name: Annotated[str, Field(max_length=50, title="Name of the Patient")]
    email: EmailStr
    linkedin_url: Optional[AnyUrl] = None
    age: Annotated[int, Field(gt=0, le=120)]
    
    # strict=True disables Pydantic's automatic type casting (e.g., stops "75.2" -> 75.2)
    weight: Annotated[float, Field(gt=0, strict=True)]
    
    # Custom business logic for a single field
    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid corporate domain")
        return value
        
    # Data transformation
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

patient_info = {
    "name": "Nitish",
    "email": "abc@hdfc.com",
    "age": 30,
    "weight": 75.2
}

patient2 = Patient(**patient_info)
print(patient2.name) # Outputs: NITISH