Pretty much the same process as phase 2, except for the part of creating drawObject function, push and pop functions were used as a pair
to save and restore the drawing style settings and transformation.

def setup():
    size(1000, 1000)
    noStroke()

def drawObject(x,y,s):
    push()
    translate(x,y) #Translate function specifies an amount to displace objects within the display window.
    scale(s)
    fill(0)
    ellipse(10,30,10,10)
    ellipse(40,30,10,10)
    arc(25,40,10,10,radians(0),radians(180))    #Degrees have to be translated into radians to be able to run the function.
    pop()                                 

def draw():
    drawObject(0,0,1) #The first and second digits in the bracket mean x and y coordinate, the third controls the size of the object been drawn.
    drawObject(100,100,2)
    drawObject(300,300,3)
