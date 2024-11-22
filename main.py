class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def set_details(self,name,gender,age):
        self.name=name
        self.age=age
        self.gender=gender
    def get_details(self):
        print(f"Name:[{self.name}],Age:[{self.age}],Gender:[{self.gender}]")

class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.student_id=""
        self.course=""
        self.grades=[]
    def set_student_details(self,student_id,course):
        self.student_id=student_id
        self.course=course
    def add_grade(self,grade):
        self.grades.append(grade)
    def calculate_average_grade(self):
        if len(self.grades)>1:
            self.avg_grade=sum(self.grades)/len(self.grades)
            return self.avg_grade
        else:
            return 0
    def get_student_summary(self):
        print(Student)

class Professor(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.staff_id=""
        self.salary=""
        self.department=""
    def set_proffessor_details(self,staff_id,salary,department):
        self.staff_id=staff_id
        self.salary=salary
        self.department=department
    def give_feedback(self,Student,feedback):
        self.student=Student
        self.feedback=feedback
        print