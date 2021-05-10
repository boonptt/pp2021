import numpy
from domains.student import *
from domains.course import *
from domains.mark import*

class outputmodule:
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