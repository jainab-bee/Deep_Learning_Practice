from pydantic import BaseModel
from typing import Optional, List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = False 
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

# Raw data dictionary
patient_info = {
    "name": "Nitish",
    "age": 30,
    "weight": 75.2,
    "married": False,
    "allergies": ["pollen", "dust"],
    "contact_details": {
        "email": "abc@gmail.com",
        "phone": "1234567890"
    }
}

# Instantiating the Pydantic model (Type cohersion & validation happens here)
patient1 = Patient(**patient_info)
print(patient1)