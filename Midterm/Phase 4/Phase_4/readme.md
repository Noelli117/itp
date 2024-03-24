#This is the initial codes I had, and it could not run as y was not defined.
def setup():
    size(1000, 1000)
    noStroke()

def draw():
    drawObject(x,y,s)

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    ellipse(10,30,10,10)
    ellipse(40,30,10,10)
    arc(25,40,10,10,radians(0),radians(180))
    pop()


for x in range(100):
    for drawObject in range (1,1000):
        draw()

#And I tried several other ways to solve the problem, I realized that I did not use the nested for loop, instead I used a single for loop that does not contain any defination of y.

def setup():
    size(1000, 1000)
    noStroke()


def draw():
    for x in range (100):
        for y in range(100):
            drawObject(x*100 , y*100,1)

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    ellipse(10,30,10,10)
    ellipse(40,30,10,10)
    arc(25,40,10,10,radians(0),radians(180))
    pop()

#So I put a nested for loop in the draw function, and put the y loop inside the for x loop as a inner loop which solved the problem.
