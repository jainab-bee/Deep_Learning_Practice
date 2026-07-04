from pydantic import BaseModel, computed_field

# Nested Model Schema
class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address # Referencing the nested model
    weight: float
    height: float
    
    # Computes BMI dynamically from the weight and height fields
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

address_info = {
    "city": "Gurgaon",
    "state": "Haryana",
    "pincode": 122018
}

patient_info = {
    "name": "Nitish",
    "gender": "Male",
    "age": 30,
    "address": Address(**address_info),
    "weight": 75.2,
    "height": 1.72
}

patient4 = Patient(**patient_info)
print(f"Computed BMI: {patient4.bmi}")

# --- Exporting Pydantic Objects (Bonus from Video) ---
print(patient4.model_dump()) # Exports as a Python Dictionary
print(patient4.model_dump_json()) # Exports as JSON
print(patient4.model_dump(include={"name", "bmi"})) # Selective export
print(patient4.model_dump(exclude={"address"}))