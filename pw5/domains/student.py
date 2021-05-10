student = []
studentid = []


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