
# 📘 Pydantic Notes (FastAPI)

This folder contains my **Pydantic learning notes** while learning **FastAPI for Machine Learning**.

The notebooks are written in a simple and beginner-friendly way with explanations, examples, and practice code.

---

# 📂 Contents

### 📄 Part 1 - Introduction to Pydantic

Topics Covered

- What is Pydantic?
- Why do we need Pydantic?
- Data Validation
- Type Validation
- BaseModel
- Required vs Optional Fields
- List
- Dictionary
- Type Coercion
- Creating the First Pydantic Model

---

### 📄 Part 2 - Field(), Annotated & Built-in Types

Topics Covered

- EmailStr
- AnyUrl
- Field()
- Annotated
- Field Constraints
- Metadata
- strict=True
- Validation Examples

---

### 📄 Part 3 - Validators

Topics Covered

- field_validator
- model_validator
- Custom Validation
- Data Transformation
- Business Rules
- ValidationError

---

### 📄 Part 4 - Advanced Features

Topics Covered

- Computed Fields
- Nested Models
- model_dump()
- model_dump_json()
- include
- exclude
- Exporting Data
- Complete Example

---

# 📚 Learning Outcomes

After completing these notebooks, you will be able to:

- Create Pydantic Models
- Validate User Input
- Use Required and Optional Fields
- Work with Lists and Dictionaries
- Validate Emails and URLs
- Apply Constraints using Field()
- Use Annotated for Clean Code
- Create Custom Validators
- Validate Multiple Fields Together
- Create Computed Fields
- Build Nested Models
- Export Models as Dictionary or JSON
- Use Pydantic effectively with FastAPI

---

# 🛠 Requirements

Install Pydantic Version 2

```bash
pip install pydantic
```

For Email Validation

```bash
pip install pydantic[email]
```

