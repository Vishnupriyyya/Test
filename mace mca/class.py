class Student:
    def __init__(self, name,classrm,dob,address,admsnno):
        self.name = name
        self.classrm = classrm
        self.dob = dob
        self.address = address
        self.admsnno = admsnno
        self.marksheet= {}
    def __str__(self):
        return f"Name: {self.name}\nClass: {self.classrm}\nDate of Birth: {self.dob}\nAddress: {self.address}\nAdmission Number: {self.admsnno}\nMarksheet: {self.marksheet}"

    def updateClassroom(self ,newclassrm):
        self.classrm = newclassrm

    def updateAddress(self,newAddress):
        self.address = newAddress

    def addSubject(self, subjectName, marks=0):
        self.marksheet[subjectName] = marks

   # def addSubject(self, subjectName):
        #self.marksheet[subjectName] = 0
        

    def updateScore(self, subjectName, newMarks):
        self.marksheet[subjectName] =newMarks

    '''def display_info(self):
        print(f"Name: {self.name}\nDOB: {self.dob}\nClassroom: {self.classrm}\nAddress: {self.address}\nAdmission No:{self.admsnno}")'''

s1=Student("Vish","MCA","28-11-2002","Mvpzha","M24CA035")
s1.addSubject("Biology")
s1.addSubject("Maths",200)
#print(s1.name,s1.dob,s1.marksheet)
print(s1)
