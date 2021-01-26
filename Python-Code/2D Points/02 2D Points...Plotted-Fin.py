########################################################################################################################
# Name: Jordan Fergurson
# Date: July 17, 2018
# Description: The coordinates of individual 2D points are located and plotted in an 800*800 grid, placement and color
#              random
########################################################################################################################

from Tkinter import *
from random import randint

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


# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter

class CoordinateSystem(Canvas):

    def __init__(self,master):
        Canvas.__init__(self,master,bg = "white")
        self.pack(fill = BOTH, expand = 1)

    def plotPoints(self,NUM_POINTS):
        
        for i in range(NUM_POINTS): 
            p = Point(randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
            self.plot(p.xcomp,p.ycomp)
            
    def plot(self, x, y):

        # Add color to the points being plotted
        pointcolor = COLORS[randint(0,len(COLORS)-1)]
        self.create_oval(x, y, (x + 2 * POINT_RADIUS), (y + 2 * POINT_RADIUS), outline = pointcolor)


# A point object is created
P = Point()

# The default point radius is set
POINT_RADIUS = 0

# List of colors to choose from
COLORS = ["red","blue", "green", "black", "magenta", "cyan", "yellow"]

#### Poisson Disc Method Attempt ####

# n is the appropriate number of points to be generated
#n = (WIDTH*HEIGHT)/((THRESHOLD)**2)

# t is the reasonable threshold, based on the given values of n, the width and height.
#t = ((WIDTH*HEIGHT)/n)**(0.5)



##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
