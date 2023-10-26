class mathss:
    """A class of methods for mathemaitcl functions"""

    pi = 3.142
    e = 2.37

    def __init__(self, pi):
        self.pi = pi

    def sum(self, a, b):
        """method for addtion"""
        c = a + b
        print("Good you have added the two given numbers !")
        print("Sum of {a} and {b} is {c} .")
        return c

    def sub(self, a, b):
        """method for subtraction"""
        c = a - b
        print("Good you have subtracted the two given numbers !")
        print("Difference of {a} and {b} is {c} .")
        return c

    def mult_pi(self, a):
        """method for multiplication"""
        print("Good you have multiplied the two given numbers !")
        print("Pi times {} is {}".format(a, self.pi * a))
        return self.pi * a  ## Using class objects in methods

    def natural_power(self, a):
        """method for natural power"""
        return mathss.e ^ a
