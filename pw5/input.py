from domains import student, course, mark
import math

def InputStudent(students):
    id = input("Enter Id Student: ")
    name = input("Enter name of student: ")
    dob = input("Enter dob of student: ")
    student = student.Student(id, name, dob)
    students.append(student)

 f = open('Students.txt','a')
        f.write("StudnetID: " + id + "\n" + "StudentName: " + name + "\n" + "SudentDoB: " + DoB)
        f.close()
def InputCourse(courses):
    id = input("Enter Id: ")
    name = input("Enter name: ")
    credit = input("Enter credit: ")
    course = course.Course(id, name, credit)
    courses.append(course)

    f = open('Courses.txt', 'a')
    f.write("CourseID: " + id + "\n" + "CourseName: " + name + "\n" + "Course_credit: " + str(credit))
    f.close()
def inputMark(courses, students, studentMark):
    courseName = input("Enter name of course to get the mark: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMark.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))

        f = open('Marks.txt', 'a')
        f.write("CourseID: " + c_id + "\n" + "StudentID: " + s_id + "\n" + "Mark_detail: " + str(mark))
        f.close()
