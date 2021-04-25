student = []
studentid = []
course = []
courseid = []
mark = []

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
        course.append(self)
        course.append(self.studentid)

    def get_id(self):
        return self.studentid

    def get_name(self):
        return self.student_name


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
    def inputMark():
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


class Start:
    def student:
        print("List Student")
        for i in range(0, len(student)):
            print(f"id:{student[i]['id']} name:{student[i]['name']} DoB:{student[i]['DoB']}")

    def course:
        print("Show lists of course:")
        for i in range(0, len(course)):
            print("[", course[i]['cID'], "]", "[", course[i]['name'], "]", )

    def mark:
        print("Show mark of student:")
        for i in range(len(student)):
            print("[", mark[i]['courseid'], "]", "[", mark[i]['id'], "]", "[", mark[i]['mark'], "]", )

def student_management():
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
                            course()
                            student()
                            print("1.Add mark:")
                            print("2.Stop:")
                            option3 = int(input("Choose:"))
                            if option3 == 1:
                                mark()
                                course()
                                student()
                                mark()
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


Start.mark()
Start.student_management()
