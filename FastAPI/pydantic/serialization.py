from pydantic import BaseModel
from typing import Optional

# Define the Nested Model
class Address(BaseModel):
    city: str
    state: str
    pin: str

# Define the Main Model
class Patient(BaseModel):
    name: str
    # Giving a default value to demonstrate exclude_unset later
    gender: Optional[str] = "Male" 
    age: int
    address: Address

# 1. Create the objects
address_obj = Address(city="Gurgaon", state="Haryana", pin="122018")
# Notice we are not explicitly passing 'gender', so it defaults to "Male"
patient_obj = Patient(name="Nitish", age=30, address=address_obj)

# ==========================================
# 2. BASIC SERIALIZATION
# ==========================================

print("--- model_dump() (Python Dictionary) ---")
patient_dict = patient_obj.model_dump()
print(patient_dict)
print(type(patient_dict)) # <class 'dict'>

print("\n--- model_dump_json() (JSON String) ---")
patient_json = patient_obj.model_dump_json()
print(patient_json)
print(type(patient_json)) # <class 'str'>


# ==========================================
# 3. ADVANCED SERIALIZATION (Modifiers)
# ==========================================

print("\n--- Include: Only export 'name' ---")
print(patient_obj.model_dump(include={"name"}))

print("\n--- Exclude: Remove 'age' and 'gender' ---")
print(patient_obj.model_dump(exclude={"age", "gender"}))

print("\n--- Nested Exclude: Remove 'state' from the nested Address ---")
print(patient_obj.model_dump(exclude={"address": {"state"}}))

# ==========================================
# 4. EXCLUDE UNSET
# ==========================================
# Because we didn't explicitly set 'gender' when instantiating patient_obj,
# exclude_unset=True will strip it out of the exported dictionary.
print("\n--- Exclude Unset ---")
print(patient_obj.model_dump(exclude_unset=True))