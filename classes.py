class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display_info(self):
        print(f'{self.name}{self.rollno}')
student1=Student('john',9)
student2=Student('mery',5)
student1.display_info()
student2.display_info()