class Person:
    def __init__(self,name,lastname,age,ci):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.ci = ci
        self.type = '  PERSON'

    def __str__(self):
        return '{4}: {3} [{2}] - {0} {1}'.format(
                self.name,self.lastname,self.age,self.ci,self.type)

