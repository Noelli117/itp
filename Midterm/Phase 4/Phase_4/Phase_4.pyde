def setup():
    size(1000, 1000) 
    noStroke() 


def draw():
    for x in range (100):
        for y in range(100):
            drawObject(x*100,y*100,1)

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) 
    ellipse(10,30,10,10)
    ellipse(40,30,10,10)
    arc(25,40,10,10,radians(0),radians(180))
    pop()



    
