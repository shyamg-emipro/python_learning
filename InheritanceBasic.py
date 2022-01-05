# Ignore this Program
# This program is only for trial and error
class Child:
    def __init__(self, px, py, pz):
        self.cfname = px
        self.mname = py
        self.lname = pz

    def printName(self):
        print(self.cfname, self.mname, self.lname)


class Parent(Child):
    def __init__(self, childName, fname, lname):
        super(Parent, self).__init__(childName, fname, lname)
        self.fname = fname
        self.lname = lname

    def printName(self):
        super(Parent, self).printName()
        print(self.fname, self.lname)

Parent(input(),"A","B").printName()
