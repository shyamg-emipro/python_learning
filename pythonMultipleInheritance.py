class child2:
    # This class is not a parent class
    # but the class is named as per the use of the class and our convenience

    def __init__(self, fname, mname, lname):
        # Assign values to the properties
        self.c2fname = fname
        self.c2mname = mname
        self.lname = lname

    def printDetails(self):
        # print the names
        print(self.c2fname, self.c2mname, self.lname)


class child1(child2):
    # This class is level 2 class after parent class
    # But here we are using this class as per our convenience

    def __init__(self, fname, mname, lname):
        # Assign values to the properties
        # get parent(child in our logical case) first name from user
        # call super class constructor and pass parameters into it
        self.c1fname = fname
        self.c1mname = mname
        self.lname = lname
        super(child1, self).__init__(input("Enter Name of Child 2:  "), fname, lname)

    def printDetails(self):
        # print the names and name call parent class method to print it's names
        print(self.c1fname, self.c1mname, self.lname)
        super(child1, self).printDetails()


class child(child1):
    # This class is level 3 class after parent and a child class
    # But here we are using this class as per our convenience

    def __init__(self, fname, mname, lname):
        # Assign values to the properties
        # get parent(child in our logical case) first name from user
        # call super class constructor and pass parameters into it
        self.cfname = fname
        self.cmname = mname
        self.lname = lname
        super(child, self).__init__(input("Enter Name of Child 1:  "), fname, lname)

    def printDetails(self):
        # print the names and name call parent class method to print it's names
        print(self.cfname, self.cmname, self.lname)
        super(child, self).printDetails()


class parent(child):
    # This class is actually last Child class
    # but here we are using this class as per our requirement

    def __init__(self, fname, lname):
        # Assign values to the properties
        # get parent(child in our logical case) first name from user
        # call super class constructor and pass parameters into it
        self.fname = fname
        self.lname = lname
        super(parent, self).__init__(input("Enter Name of Child:  "), fname, lname)

    def printDetails(self):
        # print the names and name call parent class method to print it's names
        print(self.fname, self.lname)
        super(parent, self).printDetails()


parent("Anand", "Joshi").printDetails()
