from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random


camerapos = (0,400,800)

fovY = 150 
GRID_LENGTH = 1000  
randvar = 423

firstperson=False
camfacingangle=0

nahian=[0,0,0]
amrghura=0
amrspeed=10
rotatespeed=5



weapon=[]
weaponspeed=5
MAX_BULLET_DISTANCE=1800

danobcount=5
danobspeed=0.1
danobdie=110
gulihitradius=100
danobs=[]


cheatmode=False
automatic=False
cheatfirecooldown=190
CHEAT_FIRE_DELAY=190
losconedeg=6






life=5
score=0
gulimiss=0
gameover=False


danobpump=0.005


def distance2d(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def drawtext(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,0.8,0)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    
    gluOrtho2D(0, 1000, 0, 800)  ### left, right, bottom, top

    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    
    glRasterPos2f(x, y)
    for ch in text:
      glutBitmapCharacter(font, ord(ch))
    
  
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def spawndanob():
    while True:
        x=random.uniform(-GRID_LENGTH+100,GRID_LENGTH-100)
        y=random.uniform(-GRID_LENGTH+100,GRID_LENGTH-100)
        if distance2d(x,y,nahian[0],nahian[1])>400:
            return {'x': x,'y': y,'z':60,'phase':random.uniform(0,2*math.pi),'scale':1.0}

def resetdanobs():
    global danobs
    danobs=[]
    for i in range(5):
        danobs.append(spawndanob())


def resetgame():
    global nahian,amrghura,life,score,gulimiss,gameover,weapon,danobs,cheatmode,automatic,cheatfirecooldown,camorbitangle,camheight

    nahian=[0,0,0]
    amrghura=0
    life=5
    score=0
    gulimiss=0
    gameover=False
    weapon=[]
    cheatmode=False
    automatic=False
    cheatfirecooldown=0
    camorbitangle=0
    camheight=400

    resetdanobs()



def fireguli():
    if gameover:
        return
    fx,fy=playerforward()
    bx=nahian[0]+fx*60
    by=nahian[1]+fy*60
    bz=nahian[2]+120

    weapon.append({'x':bx,'y':by,'z':bz,'angle':amrghura,'distance':0})








def drawgulis():
    glColor3f(0,0,0)
    for b in weapon:
        glPushMatrix()
        glTranslatef(b['x'],b['y'],b['z'])
        glutSolidCube(30)
        glPopMatrix()



def drawshapes():
    drawplayer()
    drawdanobs()

def drawplayer():

    glPushMatrix()
    glTranslatef(nahian[0],nahian[1],nahian[2])
    #glScalef(Scale,scale,scale)

    if gameover:
        glRotatef(90,0,1,0)
        
    



    glRotatef(amrghura,0,0,1)



## Leg 1
    glPushMatrix()

    glColor3f(0, 0, 1)
    glScalef(2, 2, 2)
  
    glRotatef(90, 0, 1, 0)
    glRotatef(90, 0, 1, 0)
    glTranslatef(-50, 1, 0)
    gluCylinder(gluNewQuadric(), 40, 20, 250, 10, 10) ### parameters are: quadric, base radius, top radius, height, slices, stacks


## Leg 2
    glPopMatrix()
    glPushMatrix()
    glColor3f(0, 0, 1)
    glScalef(2, 2, 2)
  
    
    glRotatef(90, 0, 1, 0)

    glRotatef(90, 0, 1, 0)
    glTranslatef(50, 1, 0)
    gluCylinder(gluNewQuadric(), 40, 20, 250, 10, 10)

## body

    glPopMatrix()
    glPushMatrix()
    glColor3f(0, 0.5, 0)
    glTranslatef(0, 0, 250)
    glutSolidCube(150)

## head
    glPopMatrix()
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslatef(0, 0, 400)
    gluSphere(gluNewQuadric(), 50, 10, 10)# parameters are: quadric, radius, slices, stacks

## weapon
    glPopMatrix()
    glPushMatrix() 

    glColor3f(0.5, 0.5, 0.5)
    glScalef(2, 2, 2)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glTranslatef(0, 10, -100)
    gluCylinder(gluNewQuadric(), 20, 0,200 , 10, 10) # parameters are: quadric, base radius, top radius, height, slices, stacks

### hand 1

    glPopMatrix()
    glPushMatrix() 
    glColor3f(0.8, 0.8, 0.8)
    glScalef(2, 2, 2)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glTranslatef(40, 15, -100)
    gluCylinder(gluNewQuadric(), 20, 10,150 , 10, 10)

### hand 2
    glPopMatrix()
    glPushMatrix() 
    glColor3f(0.8, 0.8, 0.8)
    glScalef(2, 2, 2)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glRotatef(90, 1, 0, 0)
    glTranslatef(-40, 15, -100)
    gluCylinder(gluNewQuadric(), 20, 10,150 , 10, 10)


    glPopMatrix()
    glPopMatrix()





 
def drawdanobs():

    for danob in danobs:
        glPushMatrix()
        glTranslatef(danob['x'],danob['y'],danob['z'])
        scale=1.0+0.2*math.sin(danob['phase'])
        glScalef(scale,scale,scale)
        glPushMatrix()


        glColor3f(1,0,0)
        glutSolidSphere(120,20,20)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0,0,0)
        glTranslatef(0,0,130)
        glutSolidSphere(50,20,20)


        glPopMatrix()
        glPopMatrix()










def playerforward():
    rad=math.radians(amrghura)
    return math.sin(rad),-math.cos(rad)




def moveplayer(amount):
    if gameover:
        return
    fx,fy=playerforward()
    newx=nahian[0]+fx*amount
    newy=nahian[1]+fy*amount

   


    nahian[0]=max(-GRID_LENGTH+80,min(GRID_LENGTH-80,newx))
    nahian[1]=max(-GRID_LENGTH+80,min(GRID_LENGTH-80,newy))
    
   


def normalizeangle(angle):
    while angle>180:
        angle-=360
    while angle<-180:
        angle+=360
    return angle











def findlineofsightdanob():
    bestdanob=None
    bestdistance=float('inf')

    for danob in danobs:
        dx=danob['x']-nahian[0]
        dy=danob['y']-nahian[1]

        targetangle=math.degrees(math.atan2(dx,-dy))
        difference=abs(normalizeangle(targetangle-amrghura))
        dist=math.hypot(dx,dy)

        if difference<=losconedeg and dist<bestdistance:
            bestdistance=dist
            bestdanob=danob
    return bestdanob


def updatecheatmode():
    global amrghura,cheatfirecooldown

    if not cheatmode or gameover:
        return
    
    amrghura=(amrghura+2)%360
    target=findlineofsightdanob()

    if target :
        dx=target['x']-nahian[0]
        dy=target['y']-nahian[1]

        targetangle=math.degrees(math.atan2(dx,-dy))
        difference=normalizeangle(targetangle-amrghura)

        if difference>0:
            amrghura+=min(2,difference)
           
        else:
            amrghura-=min(2,-difference)
            

        amrghura%=360

        if cheatfirecooldown<=0 and abs(difference)<=losconedeg:
            fireguli()
            cheatfirecooldown=CHEAT_FIRE_DELAY

def updateautocamera():
    global camorbitangle

    if cheatmode and automatic :
        camorbitangle=amrghura


def updategulis():
    global gulimiss,score 
    remaining=[]

    for b in weapon:
        rad=math.radians(b['angle'])

        b['x']+=math.sin(rad)*weaponspeed
        b['y']+=-math.cos(rad)*weaponspeed
        b['distance']+=weaponspeed

        hit=False

        for danob in danobs:
            d=distance2d(b['x'],b['y'],danob['x'],danob['y'])

            if d<=gulihitradius:
                score+=1
                newdanob=spawndanob()
                danob.update(newdanob)

                hit=True
                break
        if hit:
            continue

        if b['distance']>MAX_BULLET_DISTANCE:
            gulimiss+=1
            if gulimiss>=10:
                endgame()
            continue
        remaining.append(b)
    
    weapon[:]=remaining



def updatedanobs():
    global life

    if gameover:
        return
    for danob in danobs:
        dx=nahian[0]-danob['x']
        dy=nahian[1]-danob['y']
        dist=math.hypot(dx,dy)

        if dist>0:
            danob['x']+=(dx/dist)*danobspeed
            danob['y']+=(dy/dist)*danobspeed
        danob['phase']+=danobpump

        if dist<=danobdie:
            life-=1

            newdanob=spawndanob()
            danob.update(newdanob)

            if life<=0:
               endgame()






def endgame():
    global gameover,weapon
    gameover=True
    weapon=[]







def keyboardListener(key, x, y):
    """
    Handles keyboard inputs for player movement, gun rotation, camera updates, and cheat mode toggles.
    """
    global nahian,amrghura,cheatmode,automatic
    
    
    # # Move forward (W key)
    if key == b'w':
        moveplayer(+amrspeed)




    # # Move backward (S key)
    elif key == b's':
        moveplayer(-amrspeed)


    # # Rotate gun left (A key)
    if key == b'a':
        amrghura=(amrghura+rotatespeed)%360

    # # Rotate gun right (D key)
    if key == b'd':
        amrghura=(amrghura-rotatespeed)%360


    # #  cheat mode (C key)
    if key == b'c':
        cheatmode=not cheatmode


    # #  cheat vision (V key)
    if key == b'v':
        
        automatic=not automatic
        
    # # Reset the game ((R key)
    if key == b'r':
        resetgame()
        return
    if gameover:
        return



def specialKeyListener(key, x, y):
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """
    global camerapos
    x, y, z = camerapos
    # Move camera up (UP arrow key)
    if key == GLUT_KEY_UP:
        z+=5
        y-=5

    # # Move camera down (DOWN arrow key)
    if key == GLUT_KEY_DOWN:
        if z!=10:
            z-=5
            y+=5
            

    # moving camera left (LEFT arrow key)
    if key == GLUT_KEY_LEFT:
        x -= 1  

    # moving camera right (RIGHT arrow key)
    if key == GLUT_KEY_RIGHT:
        x += 1  

    camerapos = (x, y, z)


def mouseListener(button, state, x, y):
    """
    Handles mouse inputs for firing bullets (left click) and toggling camera mode (right click).
    """
    global firstperson
        # # Left mouse button fires a bullet
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if not gameover:
            fireguli()
            

        # # Right mouse button  camera tracking mode
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        firstperson= not firstperson


def setupCamera():
    """
    Configures the camera's projection and view settings.
    Uses a perspective projection and positions the camera to look at the target.
    """
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()  
    
    gluPerspective(fovY, 1.25, 0.1, 3000) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()  


    if firstperson:
        fx,fy=playerforward()

        camx=nahian[0]+fx*10
        camy=nahian[1]+fy*10
        camz=nahian[2]+160

        lookx=camx+fx*500
        looky=camy+fy*500
        lookz=camz


        gluLookAt(camx, camy, camz, 
                  lookx, looky, lookz, 
                  0, 0, 1)

    else:
        if cheatmode and automatic:
            rad=math.radians(camorbitangle)
            fx,fy=math.sin(rad),-math.cos(rad)
            camdist=900
            x=nahian[0]-fx*camdist
            y=nahian[1]-fy*camdist
            z=camheight
            gluLookAt(x, y, z,
                      nahian[0], nahian[1], nahian[2],
                      0, 0, 1)
        else:
            x,y,z=camerapos
            gluLookAt(x,y, z,
                      0, 0, 0,
                      0, 0, 1)
            


      

def idle():
    global cheatfirecooldown
    """
    Idle function that runs continuously:
    - Triggers screen redraw for real-time updates.
    """

    if cheatfirecooldown>0:
        cheatfirecooldown-=1
    if not gameover:
        updatedanobs()
        updategulis()
        updatecheatmode()
        updateautocamera()
        
        
    glutPostRedisplay()

    


    
    glutPostRedisplay()


def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  
    glViewport(0, 0, 1000, 800)  

    setupCamera()  

    


    drawshapes()
    drawgulis()




    drawtext(10,770,f"life Remaining:{life}")
    drawtext(10,740,f"Score:{score}")
    drawtext(10,710,f"Bullets Missed::{gulimiss}/10")

    if cheatmode:
        drawtext(10,680,"CHEAT MODE:ON")
    if automatic and cheatmode:
        drawtext(10,650,"AUTO TRACK:ON")
    if firstperson:
        drawtext(10,620,"FIRST PERSON")
    else:
        drawtext(10,620,"THIRD PERSON")

    if gameover:
        drawtext(390,430,"GAME OVER")
        drawtext(390,400,"Press R to Restart")


    
    glBegin(GL_QUADS)


## Row 1  ##

    glColor3f(1, 1, 1)
    glVertex3f(-1800, 0, 0)
    glVertex3f(-1800, -300, 0)
    glVertex3f(-1500, -300, 0)
    glVertex3f(-1500, 0, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1500, 0, 0)
    glVertex3f(-1500, -300, 0)
    glVertex3f(-1200, -300, 0)
    glVertex3f(-1200, 0, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1200, 0, 0)
    glVertex3f(-1200, -300, 0)
    glVertex3f(-900, -300, 0)
    glVertex3f(-900, 0, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-900, 0, 0)
    glVertex3f(-900, -300, 0)
    glVertex3f(-600, -300, 0)
    glVertex3f(-600, 0, 0)


    glColor3f(1, 1, 1)
    glVertex3f(-600, 0, 0)
    glVertex3f(-600, -300, 0)
    glVertex3f(-300, -300, 0)
    glVertex3f(-300, 0, 0)


    
    glColor3f(1, 1, 1)
    glVertex3f(-300, 300, 0)
    glVertex3f(0, 300, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(-300, 0, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-300, 0, 0)
    glVertex3f(-300, -300, 0)
    glVertex3f(0, -300, 0)
    glVertex3f(0, 0, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(300, 0, 0)
    glVertex3f(300, -300, 0)
    glVertex3f(600, -300, 0)
    glVertex3f(600, 0, 0)


    glColor3f(1, 1, 1)
    glVertex3f(600, 0, 0)
    glVertex3f(600, -300, 0)
    glVertex3f(900, -300, 0)
    glVertex3f(900, 0, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(900, 0, 0)
    glVertex3f(900, -300, 0)
    glVertex3f(1200, -300, 0)
    glVertex3f(1200, 0, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1200, 0, 0)
    glVertex3f(1200, -300, 0)
    glVertex3f(1500, -300, 0)
    glVertex3f(1500, 0, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1500, 0, 0)
    glVertex3f(1500, -300, 0)
    glVertex3f(1800, -300, 0)
    glVertex3f(1800, 0, 0)






## Row 2 ##


    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1800, 300, 0)
    glVertex3f(-1800, 0, 0)
    glVertex3f(-1500, 0, 0)
    glVertex3f(-1500, 300, 0)


    glColor3f(1, 1, 1)
    glVertex3f(-1500, 300, 0)
    glVertex3f(-1500, 0, 0)
    glVertex3f(-1200, 0, 0)
    glVertex3f(-1200, 300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1200, 300, 0)
    glVertex3f(-1200, 0, 0)
    glVertex3f(-900, 0, 0)
    glVertex3f(-900, 300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-900, 300, 0)
    glVertex3f(-900, 0, 0)
    glVertex3f(-600, 0, 0)
    glVertex3f(-600, 300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-600, 300, 0)
    glVertex3f(-600, 0, 0)
    glVertex3f(-300, 0, 0)
    glVertex3f(-300, 300, 0)



    glColor3f(1, 1, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, -300, 0)
    glVertex3f(300, -300, 0)
    glVertex3f(300, 0, 0)


    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(0, 300, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(300, 0, 0)
    glVertex3f(300, 300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(300, 300, 0)
    glVertex3f(300, 0, 0)
    glVertex3f(600, 0, 0)
    glVertex3f(600, 300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(600, 300, 0)
    glVertex3f(600, 0, 0)
    glVertex3f(900, 0, 0)
    glVertex3f(900, 300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(900, 300, 0)
    glVertex3f(900, 0, 0)
    glVertex3f(1200, 0, 0)
    glVertex3f(1200, 300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1200, 300, 0)
    glVertex3f(1200, 0, 0)
    glVertex3f(1500, 0, 0)
    glVertex3f(1500, 300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1500, 300, 0)
    glVertex3f(1500, 0, 0)
    glVertex3f(1800, 0, 0)
    glVertex3f(1800, 300, 0)



## Row 3 ###

    glColor3f(1, 1, 1)
    glVertex3f(-1800, 600, 0)
    glVertex3f(-1800, 300, 0)
    glVertex3f(-1500, 300, 0)
    glVertex3f(-1500, 600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1500, 600, 0)
    glVertex3f(-1500, 300, 0)
    glVertex3f(-1200, 300, 0)
    glVertex3f(-1200, 600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1200, 600, 0)
    glVertex3f(-1200, 300, 0)
    glVertex3f(-900, 300, 0)
    glVertex3f(-900, 600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-900, 600, 0)
    glVertex3f(-900, 300, 0)
    glVertex3f(-600, 300, 0)
    glVertex3f(-600, 600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-600, 600, 0)
    glVertex3f(-600, 300, 0)
    glVertex3f(-300, 300, 0)
    glVertex3f(-300, 600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-300, 600, 0)
    glVertex3f(-300, 300, 0)
    glVertex3f(0, 300, 0)
    glVertex3f(0, 600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(0, 600, 0)
    glVertex3f(0, 300, 0)
    glVertex3f(300, 300, 0)
    glVertex3f(300, 600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(300, 600, 0)
    glVertex3f(300, 300, 0)
    glVertex3f(600, 300, 0)
    glVertex3f(600, 600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(600, 600, 0)
    glVertex3f(600, 300, 0)
    glVertex3f(900, 300, 0)
    glVertex3f(900, 600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(900, 600, 0)
    glVertex3f(900, 300, 0)
    glVertex3f(1200, 300, 0)
    glVertex3f(1200, 600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1200, 600, 0)
    glVertex3f(1200, 300, 0)
    glVertex3f(1500, 300, 0)
    glVertex3f(1500, 600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1500, 600, 0)
    glVertex3f(1500, 300, 0)
    glVertex3f(1800, 300, 0)
    glVertex3f(1800, 600, 0)


## Row 4 ####

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1800, 900, 0)
    glVertex3f(-1800, 600, 0)
    glVertex3f(-1500, 600, 0)
    glVertex3f(-1500, 900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1500, 900, 0)
    glVertex3f(-1500, 600, 0)
    glVertex3f(-1200, 600, 0)
    glVertex3f(-1200, 900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1200, 900, 0)
    glVertex3f(-1200, 600, 0)
    glVertex3f(-900, 600, 0)
    glVertex3f(-900, 900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-900, 900, 0)
    glVertex3f(-900, 600, 0)
    glVertex3f(-600, 600, 0)
    glVertex3f(-600, 900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-600, 900, 0)
    glVertex3f(-600, 600, 0)
    glVertex3f(-300, 600, 0)
    glVertex3f(-300, 900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-300, 900, 0)
    glVertex3f(-300, 600, 0)
    glVertex3f(0, 600, 0)
    glVertex3f(0, 900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(0, 900, 0)
    glVertex3f(0, 600, 0)
    glVertex3f(300, 600, 0)
    glVertex3f(300, 900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(300, 900, 0)
    glVertex3f(300, 600, 0)
    glVertex3f(600, 600, 0)
    glVertex3f(600, 900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(600, 900, 0)
    glVertex3f(600, 600, 0)
    glVertex3f(900, 600, 0)
    glVertex3f(900, 900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(900, 900, 0)
    glVertex3f(900, 600, 0)
    glVertex3f(1200, 600, 0)
    glVertex3f(1200, 900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1200, 900, 0)
    glVertex3f(1200, 600, 0)
    glVertex3f(1500, 600, 0)
    glVertex3f(1500, 900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1500, 900, 0)
    glVertex3f(1500, 600, 0)
    glVertex3f(1800, 600, 0)
    glVertex3f(1800, 900, 0)


## Row 5 ##

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1800, -300, 0)
    glVertex3f(-1800, -600, 0)
    glVertex3f(-1500, -600, 0)
    glVertex3f(-1500, -300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1500, -300, 0)
    glVertex3f(-1500, -600, 0)
    glVertex3f(-1200, -600, 0)
    glVertex3f(-1200, -300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1200, -300, 0)
    glVertex3f(-1200, -600, 0)
    glVertex3f(-900, -600, 0)
    glVertex3f(-900, -300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-900, -300, 0)
    glVertex3f(-900, -600, 0)
    glVertex3f(-600, -600, 0)
    glVertex3f(-600, -300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-600, -300, 0)
    glVertex3f(-600, -600, 0)
    glVertex3f(-300, -600, 0)
    glVertex3f(-300, -300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-300, -300, 0)
    glVertex3f(-300, -600, 0)
    glVertex3f(0, -600, 0)
    glVertex3f(0, -300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(0, -300, 0)
    glVertex3f(0, -600, 0)
    glVertex3f(300, -600, 0)
    glVertex3f(300, -300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(300, -300, 0)
    glVertex3f(300, -600, 0)
    glVertex3f(600, -600, 0)
    glVertex3f(600, -300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(600, -300, 0)
    glVertex3f(600, -600, 0)
    glVertex3f(900, -600, 0)
    glVertex3f(900, -300, 0)

    glColor3f(1, 1, 1)
    glVertex3f(900, -300, 0)
    glVertex3f(900, -600, 0)
    glVertex3f(1200, -600, 0)
    glVertex3f(1200, -300, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1200, -300, 0)
    glVertex3f(1200, -600, 0)
    glVertex3f(1500, -600, 0)
    glVertex3f(1500, -300, 0)


    glColor3f(1, 1, 1)
    glVertex3f(1500, -300, 0)
    glVertex3f(1500, -600, 0)
    glVertex3f(1800, -600, 0)
    glVertex3f(1800, -300, 0)

### row 6 ##

    glColor3f(1, 1, 1)
    glVertex3f(-1800, -600, 0)
    glVertex3f(-1800, -900, 0)
    glVertex3f(-1500, -900, 0)
    glVertex3f(-1500, -600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1500, -600, 0)
    glVertex3f(-1500, -900, 0)
    glVertex3f(-1200, -900, 0)
    glVertex3f(-1200, -600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1200, -600, 0)
    glVertex3f(-1200, -900, 0)
    glVertex3f(-900, -900, 0)
    glVertex3f(-900, -600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-900, -600, 0)
    glVertex3f(-900, -900, 0)
    glVertex3f(-600, -900, 0)
    glVertex3f(-600, -600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-600, -600, 0)
    glVertex3f(-600, -900, 0)
    glVertex3f(-300, -900, 0)
    glVertex3f(-300, -600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-300, -600, 0)
    glVertex3f(-300, -900, 0)
    glVertex3f(0, -900, 0)
    glVertex3f(0, -600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(0, -600, 0)
    glVertex3f(0, -900, 0)
    glVertex3f(300, -900, 0)
    glVertex3f(300, -600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(300, -600, 0)
    glVertex3f(300, -900, 0)
    glVertex3f(600, -900, 0)
    glVertex3f(600, -600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(600, -600, 0)
    glVertex3f(600, -900, 0)
    glVertex3f(900, -900, 0)
    glVertex3f(900, -600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(900, -600, 0)
    glVertex3f(900, -900, 0)
    glVertex3f(1200, -900, 0)
    glVertex3f(1200, -600, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1200, -600, 0)
    glVertex3f(1200, -900, 0)
    glVertex3f(1500, -900, 0)
    glVertex3f(1500, -600, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1500, -600, 0)
    glVertex3f(1500, -900, 0)
    glVertex3f(1800, -900, 0)
    glVertex3f(1800, -600, 0)

    

## row 7 ##

    glColor3f(1, 1, 1)
    glVertex3f(-1800, 1200, 0)
    glVertex3f(-1800, 900, 0)
    glVertex3f(-1500, 900, 0)
    glVertex3f(-1500, 1200, 0)


    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1500, 1200, 0)
    glVertex3f(-1500, 900, 0)
    glVertex3f(-1200, 900, 0)
    glVertex3f(-1200, 1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1200, 1200, 0)
    glVertex3f(-1200, 900, 0)
    glVertex3f(-900, 900, 0)
    glVertex3f(-900, 1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-900, 1200, 0)
    glVertex3f(-900, 900, 0)
    glVertex3f(-600, 900, 0)
    glVertex3f(-600, 1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-600, 1200, 0)
    glVertex3f(-600, 900, 0)
    glVertex3f(-300, 900, 0)
    glVertex3f(-300, 1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-300, 1200, 0)
    glVertex3f(-300, 900, 0)
    glVertex3f(0, 900, 0)
    glVertex3f(0, 1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(0, 1200, 0)
    glVertex3f(0, 900, 0)
    glVertex3f(300, 900, 0)
    glVertex3f(300, 1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(300, 1200, 0)
    glVertex3f(300, 900, 0)
    glVertex3f(600, 900, 0)
    glVertex3f(600, 1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(600, 1200, 0)
    glVertex3f(600, 900, 0)
    glVertex3f(900, 900, 0)
    glVertex3f(900, 1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(900, 1200, 0)
    glVertex3f(900, 900, 0)
    glVertex3f(1200, 900, 0)
    glVertex3f(1200, 1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1200, 1200, 0)
    glVertex3f(1200, 900, 0)
    glVertex3f(1500, 900, 0)
    glVertex3f(1500, 1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1500, 1200, 0)
    glVertex3f(1500, 900, 0)
    glVertex3f(1800, 900, 0)
    glVertex3f(1800, 1200, 0)
 

## row 8 ##

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1800, -900, 0)
    glVertex3f(-1800, -1200, 0)
    glVertex3f(-1500, -1200, 0)
    glVertex3f(-1500, -900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1500, -900, 0)
    glVertex3f(-1500, -1200, 0)
    glVertex3f(-1200, -1200, 0)
    glVertex3f(-1200, -900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1200, -900, 0)
    glVertex3f(-1200, -1200, 0)
    glVertex3f(-900, -1200, 0)
    glVertex3f(-900, -900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-900, -900, 0)
    glVertex3f(-900, -1200, 0)
    glVertex3f(-600, -1200, 0)
    glVertex3f(-600, -900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-600, -900, 0)
    glVertex3f(-600, -1200, 0)
    glVertex3f(-300, -1200, 0)
    glVertex3f(-300, -900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-300, -900, 0)
    glVertex3f(-300, -1200, 0)
    glVertex3f(0, -1200, 0)
    glVertex3f(0, -900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(0, -900, 0)
    glVertex3f(0, -1200, 0)
    glVertex3f(300, -1200, 0)
    glVertex3f(300, -900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(300, -900, 0)
    glVertex3f(300, -1200, 0)
    glVertex3f(600, -1200, 0)
    glVertex3f(600, -900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(600, -900, 0)
    glVertex3f(600, -1200, 0)
    glVertex3f(900, -1200, 0)
    glVertex3f(900, -900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(900, -900, 0)
    glVertex3f(900, -1200, 0)
    glVertex3f(1200, -1200, 0)
    glVertex3f(1200, -900, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1200, -900, 0)
    glVertex3f(1200, -1200, 0)
    glVertex3f(1500, -1200, 0)
    glVertex3f(1500, -900, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1500, -900, 0)
    glVertex3f(1500, -1200, 0)
    glVertex3f(1800, -1200, 0)
    glVertex3f(1800, -900, 0)


    ## row 9 ##

    glColor3f(1, 1, 1)
    glVertex3f(-1800, -1200, 0)
    glVertex3f(-1800, -1500, 0)
    glVertex3f(-1500, -1500, 0)
    glVertex3f(-1500, -1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-1500, -1200, 0)
    glVertex3f(-1500, -1500, 0)
    glVertex3f(-1200, -1500, 0)
    glVertex3f(-1200, -1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-1200, -1200, 0)
    glVertex3f(-1200, -1500, 0)
    glVertex3f(-900, -1500, 0)
    glVertex3f(-900, -1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-900, -1200, 0)
    glVertex3f(-900, -1500, 0)
    glVertex3f(-600, -1500, 0)
    glVertex3f(-600, -1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(-600, -1200, 0)
    glVertex3f(-600, -1500, 0)
    glVertex3f(-300, -1500, 0)
    glVertex3f(-300, -1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(-300, -1200, 0)
    glVertex3f(-300, -1500, 0)
    glVertex3f(0, -1500, 0)
    glVertex3f(0, -1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(0, -1200, 0)
    glVertex3f(0, -1500, 0)
    glVertex3f(300, -1500, 0)
    glVertex3f(300, -1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(300, -1200, 0)
    glVertex3f(300, -1500, 0)
    glVertex3f(600, -1500, 0)
    glVertex3f(600, -1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(600, -1200, 0)
    glVertex3f(600, -1500, 0)
    glVertex3f(900, -1500, 0)
    glVertex3f(900, -1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(900, -1200, 0)
    glVertex3f(900, -1500, 0)
    glVertex3f(1200, -1500, 0)
    glVertex3f(1200, -1200, 0)


    glColor3f(1, 1, 1)
    glVertex3f(1200, -1200, 0)
    glVertex3f(1200, -1500, 0)
    glVertex3f(1500, -1500, 0)
    glVertex3f(1500, -1200, 0)

    glColor3f(0.7, 0.5, 0.9)
    glVertex3f(1500, -1200, 0)
    glVertex3f(1500, -1500, 0)
    glVertex3f(1800, -1500, 0)
    glVertex3f(1800, -1200, 0)

##  Boundary ##

    glColor3f(0, 1, 0)
    glVertex3f(-1800, 1200, 0)
    glVertex3f(-1800, 1200, 100)
    glVertex3f(-1800, -1500, 100)
    glVertex3f(-1800, -1500, 0)

    glColor3f(0.5, 0.5, 1)
    glVertex3f(-1800, -1500, 0)
    glVertex3f(-1800, -1500, 100)
    glVertex3f(1800, -1500, 100)
    glVertex3f(1800, -1500, 0)


    glColor3f(0, 0, 1)
    glVertex3f(1800, -1500, 0)
    glVertex3f(1800, -1500, 100)
    glVertex3f(1800, 1200, 100)
    glVertex3f(1800, 1200, 0)

    glColor3f(1, 1, 1)
    glVertex3f(1800, 1200, 0)
    glVertex3f(1800, 1200, 100)
    glVertex3f(-1800, 1200, 100)
    glVertex3f(-1800, 1200, 0)

   
    glEnd()

   
    glutSwapBuffers()



def main():


    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  
    glutInitWindowSize(1000, 800) 
    glutInitWindowPosition(100, 100)  
    glutCreateWindow(b"3D OpenGL Intro")  
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(showScreen)  
    glutKeyboardFunc(keyboardListener)  
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  
    resetgame()


    glutMainLoop()  

    

if __name__ == "__main__":
    main()