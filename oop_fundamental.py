# In oop everything is 'Object' so always try to make the program object oriented
# In OOP class==Design and Method==Behaviour of objects and Object== Model we create from the design or class..
# a class contains of two things 1.Attribute(Variables)  2. Methods(Functions)

class StudentsEnroll: #outer Class
    school='Jhargram K.K Institution' #This variable is called Class/Static Var.
    def __init__(self,student_name,roll):
        #print('Name','ROll No','School','Laptop Config.')
        #Variable use in __init__ is called instance variable/Attribute
        self.name=student_name
        self.roll_no=roll
#        self.lap=self.Laptop()
        

    class Laptop:   ##inner class of StudentEnroll....we have to make a object of its in the outer class to give life
        def __init__(self):
            self.cpu='i5'
            self.ram=16
            self.company='hp'
        def Details(self):
            print(self.company,self.cpu,self.ram)

    def Details(self):
        print(self.name,self.roll_no,self.school)#you cannot print laptop here


stud1=StudentsEnroll('Roni','02')
stud2=StudentsEnroll('Bobi','09')
#Students.Details(stud1)
stud1.Details()
stud2.Details()
lap1=StudentsEnroll.Laptop()    #ior lap1=stud1.Laptop()    #outer object creation
lap1.Details()
# lap2=stud2.Laptop()
# lap1.Details()


