#if name is not str, we will get a validation error
#Optinal hai, but None hona chaiye value of age, if not provided
#Pydantic is intelligent, if i put age as '32' even though it is str, it will convert it to int and not give a validation error
#Field: to put constraints on the fields, like min_length, max_length, regex etc

from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'N/A' #a default value has been set
    age: Optional[int] = None #age is optional and can be None
    mail: EmailStr #email should be a valid email address
    cgpa: float = Field(gt=0, lt=10) #cgpa should be greater than 0 and less than 10

new_person={'name':'Manasvi', 'age':'19','mail':'manasvi@example.com','cgpa':12}

student = Student(**new_person)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()