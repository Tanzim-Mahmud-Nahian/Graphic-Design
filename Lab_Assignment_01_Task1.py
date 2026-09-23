#### Task 1
# ===========================================

from OpenGL.GL import *     
from OpenGL.GLUT import *    
from OpenGL.GLU import *     
import math
import random
# ===== Global Variables =====
WINDOW_WIDTH, WINDOW_HEIGHT = 1550,1000
## point 1
x1, y1 = 250,random.randint(-250,250)     
         
            
           
## point 2
x2, y2 = 230,random.randint(-250,250)   


##point 3
x3, y3 = 210,random.randint(-250,250)


##point 4
x4, y4 = 190,random.randint(-250,250)   



##point 5
x5, y5 = 170,random.randint(-250,250) 

##point 6
x6, y6 = 150,random.randint(-250,250)

##point 7
x7, y7 = 130,random.randint(-250,250) 

##point 8
x8, y8 = 110,random.randint(-250,250) 

##point 9
x9, y9 = 90,random.randint(-250,250) 

##point 10
x10, y10 = 70,random.randint(-250,250) 

##point 11
x11, y11 = 50,random.randint(-250,250) 

##point 12
x12, y12 = 30,random.randint(-250,250) 

##point 13
x13, y13 = 10,random.randint(-250,250)

##point 14
x14, y14 = -10,random.randint(-250,250) 

##point 15
x15, y15 = -30,random.randint(-250,250) 

##point 16
x16, y16 = -50,random.randint(-250,250) 

##point 17
x17, y17 = -70,random.randint(-250,250)

##point 18
x18, y18 = -90,random.randint(-250,250) 

##point 19
x19, y19 = -110,random.randint(-250,250) 

##point 20
x20, y20 = -130,random.randint(-250,250) 

##point 21
x21, y21 = -150,random.randint(-250,250) 

##point 22
x22, y22 = -170,random.randint(-250,250) 

##point 23
x23, y23 = -190,random.randint(-250,250) 

##point 24
x24, y24 = -210,random.randint(-250,250) 

##point 25
x25, y25 = -230,random.randint(-250,250)

##point 26
x26, y26 = -250,random.randint(-250,250)



speed = 0.5 
extra=0
ball_size = 4               
new_point = False 
rain_state=0 
sky=0
sky_speed=0
rain_direction=0

# ===== Coordinate Conversion =====
def convert_coordinate(x, y):
    """
    Converts mouse (screen) coordinates to OpenGL (Cartesian) coordinates.
    Top-left of the window is (0,0) in screen space,
    but OpenGL center is (0,0).
    """
    a = x 
    b =  y
    return a, b


# ===== Draw Functions =====
def draw_point(x, y, size):
    global rain_state
    """Draws a single point at (x, y) with given size."""
    glPointSize(size)
    glLineWidth(0.5)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    if rain_state ==0:
        glVertex2f(x, y+20)
    elif rain_state ==1:
        glVertex2f(x+20, y+20)
    else:
        glVertex2f(x-20, y+20)
    glEnd()


def draw_axes():
    """Draws X and Y axes centered at origin."""
    

    


def draw_shapes():
    """Draws a triangle and a square with color gradients."""
    

    ## Soil


    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.35, 0.05)
    glVertex2d(250, 50)
    glColor3f(0.5, 0.35, 0.05)
    glVertex2d(-250, 50)
    glColor3f(0.5, 0.35, 0.05)
    glVertex2d(-250, -250)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.35, 0.05)
    glVertex2d(250, 50)
    glColor3f(0.5, 0.35, 0.05)
    glVertex2d(-250, -250)
    glColor3f(0.5, 0.35, 0.05)
    glVertex2d(250, -250)
    glEnd()

    ## Trees : 1

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-250, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-235, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-220, 0)
    glEnd()

    ## Trees : 2

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-220, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-205, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-190, 0)
    glEnd()

    ## Trees : 3

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-190, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-175, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-160, 0)
    glEnd()

     ## Trees : 4

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-160, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-145, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-130, 0)
    glEnd()

       ## Trees : 5

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-130, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-115, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-100, 0)
    glEnd()

        ## Trees : 6

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-100, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-85, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-70, 0)
    glEnd()

     ## Trees : 7

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-70, 0)
    glColor3f(0, 1, 0)
    glVertex2d(-55, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-40, 0)
    glEnd()

    ## Trees : 8

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-40, 0)
    glColor3f(0, 1, 0)
    glVertex2f(-27.5, 50)
    glColor3f(0, 1, 0)
    glVertex2d(-15, 0)
    glEnd()

        ## Trees : 9

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(-15, 0)
    glColor3f(0, 1, 0)
    glVertex2f(-2.5, 50)
    glColor3f(0, 1, 0)
    glVertex2d(10, 0)
    glEnd()

     ## Trees : 10

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(10, 0)
    glColor3f(0, 1, 0)
    glVertex2d(25, 50)
    glColor3f(0, 1, 0)
    glVertex2d(40, 0)
    glEnd()

    ## Trees : 11

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(40, 0)
    glColor3f(0, 1, 0)
    glVertex2d(55, 50)
    glColor3f(0, 1, 0)
    glVertex2d(70, 0)
    glEnd()

     ## Trees : 12

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(70, 0)
    glColor3f(0, 1, 0)
    glVertex2d(85, 50)
    glColor3f(0, 1, 0)
    glVertex2d(100, 0)
    glEnd()

    ## Trees : 13

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(100, 0)
    glColor3f(0, 1, 0)
    glVertex2d(115, 50)
    glColor3f(0, 1, 0)
    glVertex2d(130, 0)
    glEnd()

    ## Trees : 14

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(130, 0)
    glColor3f(0, 1, 0)
    glVertex2d(145, 50)
    glColor3f(0, 1, 0)
    glVertex2d(160, 0)
    glEnd()

     ## Trees : 15

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(160, 0)
    glColor3f(0, 1, 0)
    glVertex2d(175, 50)
    glColor3f(0, 1, 0)
    glVertex2d(190, 0)
    glEnd()

     ## Trees : 16

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(190, 0)
    glColor3f(0, 1, 0)
    glVertex2d(205, 50)
    glColor3f(0, 1, 0)
    glVertex2d(220, 0)
    glEnd()

    ## Trees : 17

    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2d(220, 0)
    glColor3f(0, 1, 0)
    glVertex2d(235, 50)
    glColor3f(0, 1, 0)
    glVertex2d(250, 0)
    glEnd()

    ## Roof

    glBegin(GL_TRIANGLES)
    glColor3f(0.45, 0, 1)
    glVertex2d(-110, 10)
    glColor3f(0.45, 0, 1)
    glVertex2f(0, 70)
    glColor3f(0.45, 0, 1)
    glVertex2d(110, 10)
    glEnd()


    ## Wall


    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2d(-90, 10)
    glColor3f(1, 1, 1)
    glVertex2d(90, 10)
    glColor3f(1, 1, 1)
    glVertex2d(90, -150)
    
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2d(-90, 10)
    glColor3f(1, 1, 1)
    glVertex2d(90, -150)
    glColor3f(1, 1, 1)
    glVertex2d(-90, -150)
    
    glEnd()

    ## Window 1

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0.5, 1)
    glVertex2d(-70, 0)
    glColor3f(0, 0.5, 1)
    glVertex2d(-70, -60)
    glColor3f(0, 0.5, 1)
    glVertex2d(-10, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0.5, 1)
    glVertex2d(-10, 0)
    glColor3f(0, 0.5, 1)
    glVertex2d(-70, -60)
    glColor3f(0, 0.5, 1)
    glVertex2d(-10, -60)
    glEnd()


     ## Window 2

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0.5, 2)
    glVertex2d(10, 0)
    glColor3f(0, 0.5, 1)
    glVertex2d(10, -60)
    glColor3f(0, 0.5, 1)
    glVertex2d(70, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0.5, 1)
    glVertex2d(70, 0)
    glColor3f(0, 0.5, 1)
    glVertex2d(10, -60)
    glColor3f(0, 0.5, 1)
    glVertex2d(70, -60)
    glEnd()



    ## Window 1 lines


    glLineWidth(1)
    glBegin(GL_LINES)
    ## x-axis
    glColor3f(0, 0, 0)
    glVertex2f(-70, -30)
    glVertex2f(-10, -30)

    ## y-axis
    glColor3f(0, 0, 0)
    glVertex2f(-40, 0)
    glVertex2f(-40, -60)
    glEnd()


    ## windom 2 lines

    glBegin(GL_LINES)
    ## x-axis
    glColor3f(0, 0, 0)
    glVertex2f(10, -30)
    glVertex2f(70, -30)

    ## y-axis
    glColor3f(0, 0, 0)
    glVertex2f(40, 0)
    glVertex2f(40, -60)
    glEnd()

    ## Door

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0.5, 1)
    glVertex2d(20, -80)
    glColor3f(0, 0.5, 1)
    glVertex2d(-20, -80)
    glColor3f(0, 0.5, 1)
    glVertex2d(-20, -150)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0.5, 1)
    glVertex2d(20, -80)
    glColor3f(0, 0.5, 1)
    glVertex2d(-20, -150)
    glColor3f(0, 0.5, 1)
    glVertex2d(20, -150)
    glEnd()


    ## Door lock

    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(10, -115)
    glEnd()








# ===== Keyboard & Mouse Interaction =====
def keyboard_listener(key, x, y):
    """Handles normal keyboard inputs."""
    global rain_state ,sky_speed 
    if key== b'w':
        rain_state=(rain_state+1)%3

    elif key == b'x':  #white
        
         sky_speed =0.0004
        
    elif key == b'y':  #black
        sky_speed-=0.0004

    glutPostRedisplay()


def special_key_listener(key, x, y):
    """Handles special keys (arrows, F-keys, etc.)."""
    global rain_state
    if key == GLUT_KEY_LEFT:
        rain_state=1
    elif key == GLUT_KEY_RIGHT:
        rain_state=2
    glutPostRedisplay()


def mouse_listener(button, state, x, y):
    """
    Handles mouse clicks.
    Left-click: Move ball.
    Right-click: Create a new point.
    """
    global rain_state
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        
        rain_state=1

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        
        rain_state=2



def setup_projection():
    """Defines a 2D orthographic coordinate system."""
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 0, 1)
    glMatrixMode(GL_MODELVIEW)



def display():
    """Main display callback for rendering each frame."""
    glClearColor(sky,sky,sky,1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()

    draw_axes()
    draw_shapes()
    glColor3f(1,1,1)
    draw_point(x1, y1, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x2, y2, ball_size)

    glColor3f(1,1,1)
    draw_point(x3, y3, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x4, y4, ball_size)

    glColor3f(1,1,1)
    draw_point(x5, y5, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x6, y6, ball_size)

    glColor3f(1,1,1)
    draw_point(x7, y7, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x8, y8, ball_size)

    glColor3f(1,1,1)
    draw_point(x9, y9, ball_size)
    
    glColor3f(0.5,0.5,1)
    draw_point(x10, y10, ball_size)

    glColor3f(1,1,1)
    draw_point(x11, y11, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x12, y12, ball_size)

    glColor3f(1,1,1)
    draw_point(x13, y13, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x14, y14, ball_size)

    glColor3f(1,1,1)
    draw_point(x15, y15, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x16, y16, ball_size)

    glColor3f(1,1,1)
    draw_point(x17, y17, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x18, y18, ball_size)

    glColor3f(1,1,1)
    draw_point(x19, y19, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x20, y20, ball_size)

    glColor3f(1,1,1)
    draw_point(x21, y21, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x22, y22, ball_size)

    glColor3f(1,1,1)
    draw_point(x23, y23, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x24, y24, ball_size)

    glColor3f(1,1,1)
    draw_point(x25, y25, ball_size)

    glColor3f(0.5,0.5,1)
    draw_point(x26, y26, ball_size)


    
    if new_point:
        px, py = new_point
        glColor3f(1, 1, 1)
        draw_point(px, py, 6)

    glutSwapBuffers()


def animate():
    """Continuously moves the ball diagonally."""
    global x1, y1,rain_state,sky,sky_speed, speed,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16,x17,y17,x18,y18,x19,y19,x20,y20,x21,y21,x22,y22,x23,y23,x24,y24,x25,y25,x26,y26,extra
    
    sky+=sky_speed
    if sky>=1.0:
       
       sky=1.0
       sky_speed=0

    if sky<=0.0:
       sky=0.0
       sky_speed=0
       
       
    
    if rain_state==1:
       x1 -=0.54
    elif rain_state==2:
       x1 +=0.54
    y1 -=0.57
    if   y1<-250:
        x1=random.randint(-250,250)
        y1=random.randint(-250,250)

    if rain_state==1:
       x2 -=0.59
    elif rain_state==2:
       x2 +=0.59
    y2 -=0.59
    if   y2<-250:
        x2=random.randint(-250,250)
        y2=random.randint(-250,250)

    if rain_state==1:
       x3 -=0.53
    elif rain_state==2:
       x3 +=0.53 
    y3 -=0.57
    if  y3<-250:
        x3=random.randint(-250,250)
        y3=random.randint(-250,250)
    
    if rain_state==1:
       x4 -=0.54
    elif rain_state==2:
       x4 +=0.54
    y4 -=0.58
    if  y4<-250:
        x4=random.randint(-250,250)
        y4=random.randint(-250,250)
    
    if rain_state==1:
       x5 -=0.57
    elif rain_state==2:
       x5 +=0.57
    y5 -=0.56
    if  y5<-250:
        x5=random.randint(-250,250)
        y5=random.randint(-250,250)

    if rain_state==1:
       x6 -=0.50
    elif rain_state==2:
       x6 +=0.50 
    y6 -=0.52
    if  y6<-250:
        x6=random.randint(-250,250)
        y6=random.randint(-250,250)

    if rain_state==1:
       x7 -=0.58
    elif rain_state==2:
       x7 +=0.58
    y7 -=0.51
    if  y7<-250:
        x7=random.randint(-250,250)
        y7=random.randint(-250,250)

    if rain_state==1:
       x8 -=0.54
    elif rain_state==2:
       x8 +=0.54 
    y8 -=0.59
    if  y8<-250:
        x8=random.randint(-250,250)
        y8=random.randint(-250,250)

    if rain_state==1:
       x9 -=0.51
    elif rain_state==2:
       x9 +=0.51 
    y9 -=0.55
    if  y9<-250:
        x9=random.randint(-250,250)
        y9=random.randint(-250,250)

    if rain_state==1:
       x10 -=0.54
    elif rain_state==2:
       x10 +=0.54 
    y10 -=0.58
    if  y10<-250:
        x10=random.randint(-250,250)
        y10=random.randint(-250,250)
    
    if rain_state==1:
       x11 -=0.51
    elif rain_state==2:
       x11 +=0.51
    y11 -=0.56
    if  y11<-250:
        x11=random.randint(-250,250)
        y11=random.randint(-250,250)

    if rain_state==1:
       x12 -=0.59
    elif rain_state==2:
       x12 +=0.59 
    y12 -=0.53
    if  y12<-250:
        x12=random.randint(-250,250)
        y12=random.randint(-250,250)

    if rain_state==1:
       x13 -=0.55
    elif rain_state==2:
       x13 +=0.55 
    y13 -=0.56
    if  y13<-250:
        x13=random.randint(-250,250)
        y13=random.randint(-250,250)

    if rain_state==1:
       x14 -=0.50
    elif rain_state==2:
       x14 +=0.50
    y14 -=0.55
    if  y14<-250:
        x14=random.randint(-250,250)
        y14=random.randint(-250,250)

    if rain_state==1:
       x15 -=0.54
    elif rain_state==2:
       x15 +=0.54 
    y15 -=0.54
    if  y15<-250:
        x15=random.randint(-250,250)
        y15=random.randint(-250,250)

    if rain_state==1:
       x16 -=0.50
    elif rain_state==2:
       x16 +=0.50 
    y16 -=0.54
    if  y16<-250:
        x16=random.randint(-250,250)
        y16=random.randint(-250,250)

    if rain_state==1:
       x17 -=0.50
    elif rain_state==2:
       x17 +=0.50
    y17 -=0.58
    if  y17<-250:
        x17=random.randint(-250,250)
        y17=random.randint(-250,250)

    

    if rain_state==1:
       x18 -=0.56
    elif rain_state==2:
       x18 +=0.56
    y18 -=0.54
    if  y18<-250:
        x18=random.randint(-250,250)
        y18=random.randint(-250,250)

    if rain_state==1:
       x19 -=0.58
    elif rain_state==2:
       x19 +=0.58
    y19 -=0.58
    if  y19<-250:
        x19=random.randint(-250,250)
        y19=random.randint(-250,250)

    if rain_state==1:
       x20 -=0.53
    elif rain_state==2:
       x20 +=0.53 
    y20 -=0.59
    if  y20<-250:
        x20=random.randint(-250,250)
        y20=random.randint(-250,250)

    if rain_state==1:
       x21 -=0.59
    elif rain_state==2:
       x21 +=0.59
    y21 -=0.57
    if  y21<-250:
        x21=random.randint(-250,250)
        y21=random.randint(-250,250)

    if rain_state==1:
       x22 -=0.59
    elif rain_state==2:
       x22 +=0.59 
    y22 -=0.59
    if  y22<-250:
        x22=random.randint(-250,250)
        y22=random.randint(-250,250)

    if rain_state==1:
       x23 -=0.57
    elif rain_state==2:
       x23 +=0.57
    y23 -=0.55
    if  y23<-250:
        x23=random.randint(-250,250)
        y23=random.randint(-250,250)

    if rain_state==1:
       x24 -=0.55
    elif rain_state==2:
       x24 +=0.55
    y24 -=0.55
    if  y24<-250:
        x24=random.randint(-250,250)
        y24=random.randint(-250,250)
    
    if rain_state==1:
       x25 -=0.56
    elif rain_state==2:
       x25 +=0.56
    y25 -=0.58
    if  y25<-250:
        x25=random.randint(-250,250)
        y25=random.randint(-250,250)

    if rain_state==1:
       x26 -=0.50
    elif rain_state==2:
       x26 +=0.50
    y26 -=0.53
    if  y26<-250:
        x26=random.randint(-250,250)
        y26=random.randint(-250,250)



    glutPostRedisplay()




def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Interactive Animation")

    # Register callback functions
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)

    glutMainLoop()



if __name__ == "__main__":
    main()







