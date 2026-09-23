from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
import random
import time


WINDOW_W=800
WINDOW_H=600

BUTTON_Y=WINDOW_H-35
BUTTON_SIZE=26

BUTTON_RESTART_X=60
BUTTON_PLAYPAUSE_X=WINDOW_W/2
BUTTON_CLOSE_X=WINDOW_W-60

WORLD_LEFT=0
WORLD_RIGHT=WINDOW_W
WORLD_BOTTOM =0
WORLD_TOP=WINDOW_H

CATCHER_TOP_HALF_W=45
CATCHER_BOTTOM_HALF_W=30
CATCHER_HEIGHT=22
CATCHER_Y=40
CATCHER_SPEED=380.0


DIAMOND_HALF_W=12
DIAMOND_HALF_H=16
DIAMOND_BASE_SPEED=90.0
DIAMOND_ACCEL=6.0
DIAMOND_MAX_SPEED=420.0


COLOR_TEAL=(0.0,0.85,0.80)
COLOR_AMBER=(1.0,0.75,0.0)
COLOR_RED=(1.0,0.15,0.15)
COLOR_WHITE=(1.0,1.0,1.0)


def draw_points(points):
    glBegin(GL_POINTS)
    for x,y in points:
        glVertex2i(x,y)
    glEnd()


def draw_midpoint_lines(x1,y1,x2,y2):
    points=midpoint_line(x1,y1,x2,y2)
    draw_points(points)

def draw_polyline_loop(vertices):
    total=len(vertices)
    for i in range(total):
        x1,y1=vertices[i]
        x2,y2=vertices[(i+1)%total]
        draw_midpoint_lines(x1,y1,x2,y2)


def diamond_vertices(cx,cy,half_w,half_h):
    top=(cx,cy+half_h)
    right=(cx+half_w,cy)
    bottom=(cx,cy-half_h)
    left=(cx-half_w,cy)
    return [top,right,bottom,left]

def draw_diamond(cx,cy,half_w,half_h,color):
    r=color[0]
    g=color[1]
    b=color[2]

    glColor3f(r,g,b)
    draw_polyline_loop(diamond_vertices(cx,cy,half_w,half_h))


def diamond_aabb(cx,cy,half_w,half_h):
    return (
        cx-half_w,
        cy-half_h,
        2*half_w,
        2*half_h
    )


def catcher_vertices(cx,cy,top_half_w,bottom_half_w,height):
    top_y=cy+height
    bottom_y=cy
    top_left=(cx-top_half_w,top_y)
    top_right=(cx+top_half_w,top_y)
    bottom_right=(cx+bottom_half_w,bottom_y)
    bottom_left=(cx-bottom_half_w,bottom_y)
    return[top_left,top_right,bottom_right,bottom_left]


def draw_catcher(cx,cy,top_half_w,bottom_half_w,height,color):
    glColor3f(color[0],color[1],color[2])

    look=catcher_vertices(cx,cy,top_half_w,bottom_half_w,height)
    draw_polyline_loop(look)

def catcher_aabb(cx,cy,top_half_w,bottom_half_w,height):
    half_width=max(top_half_w,bottom_half_w)
    return (cx-half_width,cy,2*half_width,height)


def draw_restart_button(cx,cy,size):
    glColor3f(*COLOR_TEAL)
    hal=size/2.0
    tip=(cx-hal,cy)
    top=(cx+hal,cy+hal)
    mid=(cx+hal,cy)
    bottom=(cx+hal,cy-hal)
    draw_polyline_loop([tip,top,mid,bottom])


def draw_play_icon(cx,cy,size):
    glColor3f(*COLOR_AMBER)
    hel=size/2.0
    pain1=(cx-hel,cy+hel)
    pain2=(cx-hel,cy-hel)
    pain3=(cx+hel,cy)
    draw_midpoint_lines(*pain1,*pain2)
    draw_midpoint_lines(*pain2,*pain3)
    draw_midpoint_lines(*pain3,*pain1)

def draw_pause_icon(cx,cy,size):
    glColor3f(*COLOR_AMBER)
    hal=size/2.0
    gap=size*0.35
    draw_midpoint_lines(cx-gap,cy-hal,cx-gap,cy+hal) 

    draw_midpoint_lines(cx+gap,cy-hal,cx+gap,cy+hal)  

def draw_close_button(cx,cy,size):
    glColor3f(*COLOR_RED)
    hal=size/2.0
    draw_midpoint_lines(cx-hal,cy-hal,cx+hal,cy+hal)
    draw_midpoint_lines(cx-hal,cy-hal+1,cx+hal,cy+hal+1)
    draw_midpoint_lines(cx-hal,cy+hal,cx+hal,cy-hal)
    draw_midpoint_lines(cx-hal,cy+hal+1,cx+hal,cy-hal-1)

def button_aabb(cx,cy,size):
    high=size/2.0
    return (cx-high,cy-high,size,size)



def draw_buttons():
    draw_restart_button(BUTTON_RESTART_X,BUTTON_Y,BUTTON_SIZE)
    if b.playing:
        draw_pause_icon(BUTTON_PLAYPAUSE_X,BUTTON_Y,BUTTON_SIZE)
    else:
        draw_play_icon(BUTTON_PLAYPAUSE_X,BUTTON_Y,BUTTON_SIZE)
    draw_close_button(BUTTON_CLOSE_X,BUTTON_Y,BUTTON_SIZE)


def has_collided(box1,box2):
    x1,y1,w1,h1=box1
    x2,y2,w2,h2=box2
    if (x1<x2+w2 and x1+w1>x2 and y1<y2+h2 and y1+h1>y2):
        return True
    return False

def clamp_catcher():
    min_x=CATCHER_TOP_HALF_W
    max_x=WINDOW_W-CATCHER_TOP_HALF_W
    if b.catcher_x<min_x:
        b.catcher_x=min_x
    elif b.catcher_x>max_x:
        b.catcher_x=max_x


def animate():
    present=time.time()
    dt=present-b._last_time
    b._last_time=present
    if b.playing and not b.game_over:
        if b.cheat_mode:
            fall_y=CATCHER_Y+CATCHER_HEIGHT
            d_y=b.diamond_y-fall_y
            time_left=max(d_y,1.0)/max(b.diamond_speed,1.0)
            dis=abs(b.diamond_x-b.catcher_x)
            requ=(dis/time_left)

            if b.catcher_x<b.diamond_x:
                b.catcher_x+=requ*dt
            elif b.catcher_x>b.diamond_x:
                b.catcher_x-=requ*dt
            clamp_catcher()
        else:
            if keys["left"]:
                b.catcher_x-=CATCHER_SPEED*dt
            if keys["right"]:
                b.catcher_x+=CATCHER_SPEED*dt
            clamp_catcher()

        b.diamond_speed=min(b.diamond_speed+DIAMOND_ACCEL*dt,DIAMOND_MAX_SPEED)
        b.diamond_y-=b.diamond_speed*dt
        dia_box=diamond_aabb(b.diamond_x,b.diamond_y,DIAMOND_HALF_W,DIAMOND_HALF_H)
        cia_box=catcher_aabb(b.catcher_x,CATCHER_Y,CATCHER_TOP_HALF_W,CATCHER_BOTTOM_HALF_W,CATCHER_HEIGHT)
        if has_collided(dia_box,cia_box):
            b.score+=1
            print("Score:",b.score)
            b.spawn_diamond()
        elif b.diamond_y-DIAMOND_HALF_H<=0:
            b.game_over=True
            b.playing=False
            print("Game Over! Score:", b.score)

    glutPostRedisplay()


class GameState:
    def __init__(a):
        a.reset(full=True)

    def reset(a,full=True):
        a.score=0
        a.catcher_x=WINDOW_W/2.0
        a.game_over=False
        a.playing=True
        a.cheat_mode=False
        a.diamond_speed=DIAMOND_BASE_SPEED
        a.spawn_diamond()
        a._last_time=time.time()

    def spawn_diamond(a):
        margin=DIAMOND_HALF_W+5
        a.diamond_x=random.uniform(WORLD_LEFT +margin, WORLD_RIGHT-margin)
        a.diamond_y=WINDOW_H-40
        a.diamond_color=(random.random(),random.random(),random.random())

b=GameState()

def display():
    glClearColor(0.05,0.05,0.1,1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    if b.game_over:
        catcher_color=COLOR_RED
    else :
        catcher_color=COLOR_WHITE

    draw_catcher(
        b.catcher_x,CATCHER_Y,
        CATCHER_TOP_HALF_W,CATCHER_BOTTOM_HALF_W, CATCHER_HEIGHT,catcher_color)

    if not b.game_over:
        draw_diamond(
            b.diamond_x,b.diamond_y,DIAMOND_HALF_W,DIAMOND_HALF_H,
            b.diamond_color)

    draw_buttons()

    glutSwapBuffers()


def keyboard(key,x,y):
    if key==b'c':
        b.cheat_mode=not b.cheat_mode
        print("Cheat Mode:", b.cheat_mode)

    if key==b' ':
        if not b.game_over:
            b.playing=not b.playing


keys={"left":False,"right":False}

def special_down(key,x,y):
    if key==GLUT_KEY_LEFT:
        keys["left"]=True
    elif key==GLUT_KEY_RIGHT:
        keys["right"]=True

def special_up(key,x,y):
    if key==GLUT_KEY_LEFT:
        keys["left"]=False
    elif key==GLUT_KEY_RIGHT:
        keys["right"]=False




####  midpoint line drawing Algo

def find_zone( x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dx>=0 and dy>=0:
        if abs(dx)>=abs(dy):
            return 0
        else:
            return 1
    if dx<0 and dy>=0:
        if abs(dx)>=abs(dy):
            return 3
        else:
            return 2
    if dx<0 and dy<0:
        if abs(dx)>=abs(dy):
            return 4
        else:
            return 5
    if abs(dx)>=abs(dy):
        return 7
    else:
        return 6


def to_zone0(x,y,zone):
    if zone==0:
        return x,y
    elif zone==1:
        return y,x
    elif zone==2:
        return y,-x
    elif zone==3:
        return -x,y
    elif zone==4:
        return -x,-y
    elif zone==5:
        return -y,-x
    elif zone==6:
        return -y,x
    elif zone==7:
        return x,-y


def from_zone0(x,y,zone):

    if zone==0:
        return x,y
    elif zone==1:
        return y,x
    elif zone==2:
        return -y,x
    elif zone==3:
        return -x,y
    elif zone==4:
        return -x,-y
    elif zone==5:
        return -y,-x
    elif zone==6:
        return y,-x
    elif zone==7:
        return x,-y


def midpoint_zone0(x1,y1,x2,y2):
    points=[]
    dx=x2-x1
    dy=y2-y1

    if dx==0:
        return [(x1,y1)]
    d=2*dy-dx
    ince=2*dy
    incne=2*(dy-dx)

    x,y=x1,y1
    points.append((x,y))

    while x<x2:
        if d>0:
            d+=incne
            y+=1
        else:
            d+=ince
        x+=1
        points.append((x,y))
    return points

def midpoint_line(x1,y1,x2,y2):
    x1,y1,x2,y2=int(round(x1)),int (round(y1)),int (round(x2)),int (round(y2))
    if x1==x2 and y1==y2:
        return [(x1,y1)]

    zone=find_zone(x1,y1,x2,y2)
    fx1,fy1=to_zone0(x1,y1,zone)
    fx2,fy2=to_zone0(x2,y2,zone)

    if fx1>fx2:
        fx1,fy1,fx2,fy2=fx2,fy2,fx1,fy1
    zone0_points=midpoint_zone0(fx1,fy1,fx2,fy2)
    result=[]
    for(px,py) in zone0_points:
        result.append(from_zone0(px,py,zone))
    return result



####  ==========######



def init_gl():
    glClearColor(0.05,0.05,0.1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,WINDOW_W,0,WINDOW_H)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPointSize(2)




def point_in_button(px,py,cx,cy,size):
    h=BUTTON_SIZE/2
    if(cx-h<=px<=cx+h):
        if(cy-h<=py<=cy+h):
            return True
    return False


def mouse(button,click,x,y):
    
    if button !=GLUT_LEFT_BUTTON :
        return
    if click!=GLUT_DOWN:
        return

    
    y=WINDOW_H-y

    if point_in_button(x,y,BUTTON_RESTART_X,BUTTON_Y,BUTTON_SIZE):
        print("Starting Over")
        b.reset()
    elif point_in_button(x,y,BUTTON_PLAYPAUSE_X,BUTTON_Y,BUTTON_SIZE):
        if not b.game_over:
            b.playing=not b.playing

    elif point_in_button(x,y,BUTTON_CLOSE_X,BUTTON_Y,BUTTON_SIZE):
        print("Goodbye! Score:",b.score)
        glutLeaveMainLoop()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_W, WINDOW_H)
    glutCreateWindow(b"Catch the Diamonds!")
    init_gl()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(animate)
    glutSpecialFunc(special_down)
    glutSpecialUpFunc(special_up)
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ =="__main__":
    main()