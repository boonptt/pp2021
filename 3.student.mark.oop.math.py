import math
import numpy as np
import curses

student = []
studentid = []
course = []
courseid = []
mark = []
credit = []
GPA = []

class student:
    def __init__(self, id, name, dob):
        self.studentid = id
        self.student_name = name
        self.student_dob = dob
        student.append(self)
        studentid.append(self.studentid)

        def get_id(self):
            return self.studentid

        def get_name(self):
            return self.student_name

        def get_dob(self):
            return self.student_dob
class course:
    def __init__(self, id, name):
        self.studentid = id
        self.student_name = name
        self.credit = credit
        course.append(self)
        course.append(self.studentid)
        credit.append(self.credit)

    def get_id(self):
        return self.studentid
    def get_name(self):
        return self.student_name
    def get_credit(self):
        return self.credit

class mark:
    def __init__(self, a, b, mark):
        self.a = a
        self.b = b
        self.mark = mark
        mark.append(self)

    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_mark(self):
        return self.mark
    def get_GPA(self):
        return self.GPA
def input_information_of_student():
    def input_number_student():
        num = int(input("Enter the numbers of student:"))
        if num <= 0:
            print("There is no student")
            return 0
        else:
            return num
def get_infomation_of_student():
    print("Get infomation of student to the course:")
    info = {
        'id': '',
        'name': '',
        'dob': ''
    }
    print("Enter studentid:")
    info['id'] = id = input()
    print("Enter studentname:")
    info['name'] = input()
    print("Enter date of brith:")
    info['dob'] = input()
    student.append(info)
    studentid.append(id)


def get_infomation_of_course():
    print("Number of course")
    number_course = int(input("Enter the number of course:"))
    if (number_course <= 0):
        print("There is no course in here")
        return 0
    else:
        return number_course

def get_id_of_course():
    name = input("Enter the name of course")
    id = input("Enter the id of course")
    info = {
        'name': name,
        'id': id,
    }
    course.append(info)
    courseid.append(id)

def mark():
    def __init__(self,cid,id,mark):
        self.cid=cid
        self.id=id
        self.mark=mark
        mark.append(self)
    def describe(self):
        print(["courseid:"],self.cid, ["studentid:"],self.id, ["mark:"],self.mark)
    def inputmark():
         print("Enter course id")
         cid=input()
         if cid in courseid:
             print("Enter student id:")
             id=input()
             if id in studentid:
                 print("Enter the mark:")
                 mark=float(input())
                 if mark<0 or mark >20:
                     print("Wrong")
                     print("Enter mark again")
                     mark=float(input())
             else:
                 return 0
         else:
             return 0
         mark(cid,id,mark)
def average_GPA(self):
    print("___________")
    value=np.array([self.mark])
    cre=np.array([self.credit])
    ol=input("Enter the studentid:")
    if ol in self.id:
        for i in range (len(mark)):
            GPA=value[i]/cre[i]
            return GPA
    print("GPA")
def caculate_mark(self):
    print("GPA FIND")
    id_a=input("Enter the ID:")
    if id_a in self.studentid:
        mark=input("Enter the mark:")
    mark.append(mark)

    credit_value=[credit]
    mark_value=[mark]
    name_again=input("Enter name that you want to calculate")
    GPA=mark_value/credit_value
    return GPA

def show_student:
    print("List Student")
    for i in range(0, len(student)):
        print(f"id:{student[i]['id']} name:{student[i]['name']} DoB:{student[i]['DoB']}")
def show_course:
    print("Show lists of course:")
    for i in range(0, len(course)):
        print("[", course[i]['cID'], "]", "[", course[i]['name'], "]", )
def show_mark:
    print("Show mark of student:")
    for i in range(len(student)):
        print("[", mark[i]['courseid'], "]", "[", mark[i]['id'], "]", "[", mark[i]['mark'], "]", )

print("choose option")
print("1.y")
print("2.n")
for i in range (0,len(course)):
    ol=int(input("enter your option:"))
    if ol ==1:
        print("mark of student")
        show_mark()
        break
    else:
        break
