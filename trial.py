class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def studentName(self):
        # return {"Hello your name is ${}.format(name)"}
        return f"Hello your name is {self.name}"

    def studentAge(self):
        return f"Hello your age is  {self.age}"

