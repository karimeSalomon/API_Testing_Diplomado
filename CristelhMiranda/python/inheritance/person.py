class Person:
    def __init__(self, name, last_name, age, ci):
        self.ci = ci
        self.age = age
        self.last_name = last_name
        self.name = name

    def __str__(self):
        return f"Name: {self.name}, Last_Name: {self.last_name}" \
            f"Age: {self.age}, ci: {self.ci}"
