from pydantic import BaseModel, model_validator
from typing import Dict

class Patient(BaseModel):
    name: str
    age: int
    contact_details: Dict[str, str]
    
    # mode='after' runs the check AFTER Pydantic performs initial type casting
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        # Accessing object properties directly to cross-verify
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return self

patient_info = {
    "name": "Nitish",
    "age": 65,
    "contact_details": {
        "emergency": "9876543210" # Validation passes because emergency key exists
    }
}

patient3 = Patient(**patient_info)
print(patient3)