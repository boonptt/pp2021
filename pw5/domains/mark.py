mark = []
credit = []
GPA = []


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
