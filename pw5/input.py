import math

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

    f = open('student.txt', 'a')
    f.write("studentid: " + id + "\n" + "studentn_name: " + name + "\n" + "SudentDoB: " + dob)
    f.close()
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

    f = open('course.txt', 'a')
    f.write("courseid: " + id + "\n" + "coursename: " + name + "\n" + "credit: " + credit)
    f.close()

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

    f = open('Students.txt', 'a')
    f.write("mark: " + mark + "\n"  + "GPA: " + GPA)
    f.close()
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



