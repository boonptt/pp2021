course = []
courseid = []
credit = []

class Courses:
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
