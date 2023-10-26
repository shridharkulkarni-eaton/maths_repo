class mathss:
    pi = 3.142
    e = 2.37

    def __init__(self, pi):
        self.pi = pi

    def sum(a, b):
        c = a + b
        print("Good you have added the two given numbers !")
        print("Sum of {} and {} is {} .".format(a, b, c))
        return c

    def sub(a, b):
        c = a - b
        print("Good you have subtracted the two given numbers !")
        print("Difference of {} and {} is {} .".format(a, b, c))
        return c

    def mult_pi(self, a):
        print("Good you have multiplied the two given numbers !")
        print("Pi times {} is {}".format(a, self.pi * a))
        return self.pi * a  ## Using class objects in methods

    def natural_power(a):
        return mathss.e ^ a
