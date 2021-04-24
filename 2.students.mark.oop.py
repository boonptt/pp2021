student = []
studentid = []
course = []
courseid = []
mark = []

class Students:
    def __init__(self, id, name, dob):
        self.studentid = id
        self.student_name = name
        self.student_dob = dob
        Student.append(self)
        StudentID.append(self.studentid)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob


class Courses:
    def __init__(self, id, name):
        self.studentid = id
        self.student_name = name
        Course.append(self)
        Course.append(self._id)

    def get_id(self):
        return self._id

    def get_name(self):
        return self.name


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



def input_information_of_student():
    def input_number_student():
        Num = int(input("Enter the numbers of student:"))
        if Num <= 0:
            print("There is no students")
            return 0
        else:
            return Num

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
    students.append(info)
    student_id.append(id)


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
    course_id.append(id)

def mark():
    def __init__(self,cid,id,marks):
        self.cid=cid
        self.id=id
        self.marks=marks
        mark.append(self)
    def describe(self):
        print(["Coursesid:"],self.cid, ["Studentid:"],self.id, ["mark:"],self.marks)
    def inputMark():
         print("Enter Courses id")
         cid=input()
         if cid in CoursesID:
             print("Enter Student ID:")
             id=input()
             if id in StudentID:
                 print("Entrer marks:")
                 marks=float(input())
                 if marks<0 or marks >20:
                     print("Error")
                     print("Enter marks again")
                     marks=float(input())
             else:
                 return 0
         else:
             return 0
         mark(cid,id,marks)


class Start:
    def show_student():
        print("List Student")
        for i in range(0, len(students)):
            print(f"id:{students[i]['id']} name:{students[i]['name']} DoB:{students[i]['DoB']}")

    def show_course():
        print("Show lists of courses:")
        for i in range(0, len(courses)):
            print("[", courses[i]['cID'], "]", "[", courses[i]['Name'], "]", )

    def show_mark():
        print("Show marks of students:")
        for i in range(len(students)):
            print("[", marks[i]['coID'], "]", "[", marks[i]['ID'], "]", "[", marks[i]['marks'], "]", )

def StudentManagement():
    print("_____")
    print("""please choose option you want:
    1.  Input  course:
    2.  Stop """)
    option = int(input("Choose:"))
    if option == 1:
        Nco = get_infomation_of_course()
        print("1.Add course:")
        print("2.Stop")
        option1 = int(input("Choose:"))
        if option1 == 1:
            for i in range(Nco):
                get_id_of_course()
                Num = input_information_of_student()
                for i in range(Num):
                    print("1. Input student:")
                    print("2.Stop:")
                    option2 = int(input("Choose:"))
                    if option2 == 1:
                        for i in range(Num):
                            get_infomation_of_student()
                            show_course()
                            show_student()
                            print("1.Add mark:")
                            print("2.Stop:")
                            option3 = int(input("Choose:"))
                            if option3 == 1:
                                mark()
                                show_course()
                                show_student()
                                show_mark()
                                break
                            else:
                                exit()
                    else:
                        exit()
        else:
            exit()
    else:
        print("Out of service:")
        exit()


Start.show_mark()
Start.StudentManagement()