
def setup():
    size(1000, 1000) 
    noStroke() 

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) 
    ellipse(10,30,10,10)
    ellipse(40,30,10,10)
    arc(25,40,10,10,radians(0),radians(180))
    pop()

def draw():
    drawObject(0,0,1)
    drawObject(100,100,2)
    drawObject(300,300,3)
