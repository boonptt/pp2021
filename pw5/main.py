import input as inp
import output

student = []
studentsmark = []
course = []

def menu():
    option = "-1";
    while (option != "0"):
        print("""
                   MENU
            1. Add student
            2. Add course
            3. Add mark
            4. Show student list
            5. Show course list
            6. Show mark list
            7. Calculate average score
            8. Calculate weighted sum
            9. Sort student list
            0. Exit
            """)
        option = input("Your option: ")
        if (option == "1"):
            inp.InputStudent(student)
        elif (option == "2"):
            inp.InputCourse(course)
        elif (option == "3"):
            inp.inputMark(course, student, studentsmark)
        elif (option == "4"):
            inp.showlistStudent(student)
        elif (option == "5"):
            inp.ShowlistCourses(course)
        elif (option == "6"):
            inp.ShowMarks(studentsmark)
        elif (option == "7"):
            inp.showAvarage(student)
        elif (option == "8"):
            inp.showWeightedSum(course, studentsmark);
        elif (option == "9"):
            inp.sortAvg(student);

menu()