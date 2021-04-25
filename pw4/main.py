import curses
from output import OutputModule
from input import InputModule
from domains.student import *
from domains.course import *
from domains.mark import *

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
