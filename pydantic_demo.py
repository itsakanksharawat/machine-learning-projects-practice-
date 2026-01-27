from pydantic import BaseModel
class student(BaseModel):
    name:str
new_student ={'name':'aksha'}
student = student(**new_student)
print(student)