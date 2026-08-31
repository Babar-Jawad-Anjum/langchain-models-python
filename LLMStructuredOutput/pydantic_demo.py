from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None

new_student = {'name': 'Josh'} # Valid
new_student = {'name': 32} # Invalid because of pydantic schema, name should be string

# ** is used in Python to unpack a dictionary into keyword arguments.
student = Student(**new_student)

print(student) # valid