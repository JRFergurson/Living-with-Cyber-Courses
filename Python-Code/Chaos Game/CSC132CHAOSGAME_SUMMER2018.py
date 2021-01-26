######################################################################################################################
# Name: Jordan Fergurson
# Date: July 23, 2018
# Description: 
######################################################################################################################

from Tkinter import *
from random import *


# the 2D point class
class Point(object):

    # The constructor, intialize x and y coordinates
    def __init__(self, xcomp = 0.0, ycomp = 0.0):

        # Set points to have x and y direction
        self.xcomp = xcomp
        self.ycomp = ycomp

    # Accessors and Mutators for the instance variables
    @property
    def xcomp(self):
        return self._xcomp

    @xcomp.setter
    def xcomp(self, value):
        self._xcomp = value

    
    @property
    def ycomp(self):
        return self._ycomp

    @ycomp.setter
    def ycomp(self, value):
        self._ycomp = value

    # Assign the name pt to the class argument given,
    # then calculate the distance between the point values its
    # own class contains (self) and the point values from the input class.
    def dist(self, pt):

        # Calculate the distances in the x and y direction.
        dif_xcomp = pt.xcomp - self.xcomp
        dif_ycomp = pt.ycomp - self.ycomp

        # The distance is calculted and returned as a floating integer.
        distance = (dif_xcomp ** 2 + dif_ycomp ** 2) ** 0.5
        return distance
    
    # Assign the name pt to the class argument given,
    # then calculate the midpoint between the point values its
    # own class contains (self) and the point values from the input class.
    def midpt(self, pt):

        # Calculate the average of the x values and the y values.
        avg_xcomp = (self.xcomp + pt.xcomp) / 2
        avg_ycomp = (self.ycomp + pt.ycomp) / 2

        # Call a new object containing the averages
        return Point(avg_xcomp, avg_ycomp)
        
    # When the object is created, its values are made into floats
    # and printed in a two-dimensional coordinate form.
    def __str__(self):
        return "({},{})".format(self.xcomp*1.0, self.ycomp*1.0)


# class CoordinateSystem(Canvas): is exchanged for Chaos
class ChaosGame(Canvas):

    def __init__(self,master):
        Canvas.__init__(self,master,bg = "white")
        self.pack(fill = BOTH, expand = 1)

    def play(self,n):

        #Points representing the vertices of the triangle are created
        v1 = Point((WIDTH-1) / 2 , 10)
        v2 = Point( 2 , HEIGHT-10 )
        v3 = Point(WIDTH-7, HEIGHT-10)

        #The vertices are plotted with a larger radius and red color
        self.plot(v1.xcomp,v1.ycomp,VERTEX_RADIUS, VERTEX_COLOR)
        self.plot(v2.xcomp,v2.ycomp,VERTEX_RADIUS, VERTEX_COLOR)
        self.plot(v3.xcomp,v3.ycomp,VERTEX_RADIUS, VERTEX_COLOR)

        # vertex objects are put into a list
        # and randomly chosen from to make
        # two more points
        vertices = [v1, v2, v3]
        p1 = vertices[randint(0,2)]
        p2 = vertices[randint(0,2)]

        # the midpoint of the randomly chosen vertices is plotted
        # to get things started
        m = p1.midpt(p2)
        self.plot(m.xcomp,m.ycomp, POINT_RADIUS, POINT_COLOR)

        # For the number of points called, the vertices are
        # randomly chosen and the midpoint between the first
        # midpoint and any vertex is plotted. Then that point becomes
        # the next one to be calculated
        for i in range(n):
            v = vertices[randint(0,2)]
            m1 = m.midpt(v)
            self.plot(m1.xcomp,m1.ycomp, POINT_RADIUS, POINT_COLOR)
            m = m1
                  
    def plot(self, x, y, radius, color):
        self.create_oval(x, y, (x + 2 * radius), (y + 2 * radius)\
                         ,outline = color,fill = color)







##### Code taken from 2D Points... Plotted Assignment #####

# Set a constant Width and Height
WIDTH = 600
HEIGHT = 520

# the default vertex radius is 2 pixels and color is red
VERTEX_RADIUS = 2
VERTEX_COLOR = "red"
# the default point radius is 0 pixels and color is black
POINT_RADIUS = 0
POINT_COLOR = "black"


NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")

# create the coordinate system as a Tkinter canvas inside the window, exchange coordinate for chaos
s = ChaosGame(window)

# plot some points, at least 50,000. plotPoints is exchanged for play
s.play(NUM_POINTS)

# wait for the window to close
window.mainloop()








