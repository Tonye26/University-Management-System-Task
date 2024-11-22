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
            print(f"The average grade for {student.name} is {self.avg_grade}")
            return self.avg_grade
        else:
            return 0
    def get_student_summary(self):
        print(student.name,student.grades,student.age,student.gender)

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
        print(f"Feedback for,{Student.name}:{self.feedback}")
    def increase_salary(self,percentage):
        percentage=percentage/100
        percentage=percentage+1
        self.salary=self.salary*percentage
    def get_Professor_summary(self):
        print(professor.name,professor.age,professor.gender,professor.salary,professor.department,professor.staff_id)

class Administrator(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.admin_id=""
        self.office=""
        self.years_of_service=0
    def set_admin_details(self,admin_id,office,years_of_service):
        self.admin_id=admin_id
        self.years_of_service=years_of_service
        self.office=office
    def increment_service_years(self):
        self.years_of_service=self.years_of_service+1
    def get_admin_summary(self):
        print(self.age,self.admin_id,self.gender)

professor=Professor("Arun Raghav-Sankar",65,"Male")
professor.set_proffessor_details("A426",65000,"Biology")
student=Student("Krystian Wilk",21,"Male")
student.set_student_details("K401","Maths")
adminstrator=Administrator("Adnan",32,"Male")
adminstrator.set_admin_details("N946","H92",3)
student.add_grade(9)
student.add_grade(8)
student.calculate_average_grade()
professor.increase_salary(50)
adminstrator.increment_service_years()
professor.give_feedback(student,"Amazing work! Keep it up")
student.get_student_summary()
professor.get_Professor_summary()
adminstrator.get_admin_summary()


