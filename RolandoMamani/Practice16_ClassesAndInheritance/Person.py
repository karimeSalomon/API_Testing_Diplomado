class Person:
    first_name = None
    last_name = None
    age = None
    ci = None

    def __init__(self, name, last_name, age, ci):
        self.first_name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def name(self):
        return self.first_name + " " + self.last_name
