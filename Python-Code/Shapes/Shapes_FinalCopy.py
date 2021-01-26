######################################################################################################################
# Name: Jordan Fergurson
# Date: July 27, 2018
# Description: This program is meant to take in parameters of height and width
#              and produce four different shapes (Square, Rectangle, Triangle
#              and Parallelogram) when they are called.
######################################################################################################################



# Implement Shape class
class Shape(object):

    # The constructor to initialize the height and width of shapes
    def __init__(self, width, height):

        # Set shapes to have a height and width
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):

        # A value of zero cannot exist in this case, it must return a one
        if (value == 0):
            value = 1
        # If a user attempts to change a value to a negative number, the number will default
        # the original value already stored in memory.
        if (value < 0):
            value = self.width
    
        self._width = value # For anything other than 0 or negative numbers,
                            # use the given value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):

        # A value of zero cannot exist in this case, it must return a one
        if (value == 0):
            value = 1
        # If a user attempts to change a value to a negative number, the number will default
        # the original value already stored in memory.
        if (value < 0):
            value = self.height
            
        self._height = value  # For anything other than 0 or negative numbers,
                              # use the given value

    # All classes will refer back to this string, unless otherwise stated within the next class
    def __str__(self):
        
        for i in range(self.height):
           j = "* " * self.width
           print j

        # The return statement is taken out of the for loop and moved into the string
        # function, having it in the for loop causes it to stop after the first iteration.
        # Once return is hit, the process is over. A space is returned to complete the
        # string and avoid a TypeError.
        return " "

# The Rectangle class is implemented, inheriting all attributes from Shape class
class Rectangle(Shape):
    def __init__(self, width, height ):
        Shape.__init__(self, width, height)

# The Square class is implemented, inheriting all attributes from Shape class
class Square(Shape):
    def __init__(self, height):
        Shape.__init__(self, height, height)

# The Triangle class is implemented
class Triangle(Shape):
    def __init__(self, height):
        Shape.__init__(self, height, height)


    # This class requires its own string function, which will override
    # the string already given in the initial Shape class
    def __str__(self):

        for i in range(self.height):

            # A variable, j, is assigned to the asterisk pattern being create
            # and this is printed for each iteration in the for loop
            j = "* " * (self.height - i)
            print j

        # The return statement is taken out of the for loop and moved into the string
        # function, having it in the for loop causes it to stop after the first iteration.
        # Once return is hit, the process is over. A space is returned to complete the
        # string and avoid a TypeError.
        return " "

# The Parallelogram class is created
class Parallelogram(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, width, height)


    # This class requires its own string function, which will override
    # the string already given in the initial Shape class
    def __str__(self):
        for i in range(self.height):
            
            j = "  " * ((self.height-1)-i) + "* " * (self.width)
            print j

        # The return statement is taken out of the for loop and moved into the string
        # function, having it in the for loop causes it to stop after the first iteration.
        # Once return is hit, the process is over. A space is returned to complete the
        # string and avoid a TypeError. 
        return " "

        

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print r1
s1 = Square(6)
print s1
t1 = Triangle(7)
print t1
p1 = Parallelogram(10, 3)
print p1
r2 = Rectangle(0, 0)
print r2
p1.width = 2
p1.width = -1
p1.height = 2
print p1

