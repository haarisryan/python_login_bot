class University:
    def __init__(self,name):
        self.name=name
    def show_details(self):
        print(f"name of the university is {self.name}")
   
class Course(University):
    def __init__(self,name,u_name):
        self.course_name=name
        super().__init__(u_name)
    def show_details(self):
        print(f"course:{self.course_name} univeristy name:{self.name}")
class Branch(University):
    def __init__(self,name,u_name):
        self.branch_name=name
        University.__init__(self,u_name)
    def show_details(self):
        print(f"Branch name:{self.branch_name} university:{self.name}")    
class Student(Branch,Course):
    def __init__(self,name,b_name,c_name,u_name):
        self.student_name=name
        Branch.__init__(self,b_name,u_name)
        Course.__init__(self,c_name,u_name)
    def show_details(self):
        print(f"student name:{self.student_name} branch name:{self.branch_name} course name:{self.course_name}")
class Faculty(Branch):
    def __init__(self,name,b_name,u_name):
        self.faculty_name=name
        Branch.__init__(self,b_name,u_name)
        # University.__init__(self,u_name)
    def show_details(self):
        print(f"faculty name:{self.faculty_name} branch name:{self.branch_name} univeristy name:{self.name}")
university_1=University("anna")
course_1=Course("engineering","anna")
branch_1=Branch("aerospace","anna")
student_1=Student("ryan","aerospace","engineering","anna")
faculty_1=Faculty("ww","aerospace","anna")
faculty_1.show_details()
student_1.show_details()
branch_1.show_details()
course_1.show_details()
university_1.show_details()