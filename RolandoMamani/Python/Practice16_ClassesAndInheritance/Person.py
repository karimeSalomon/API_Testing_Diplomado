class Person:
    def __init__(self, first, last, age, ci):
        self.firstname = first
        self.lastname = last
        self.age = age
        self.ci = ci

    def Name(self):
        return self.firstname + " " + self.lastname