
from OpenGL.GL import *     
from OpenGL.GLUT import *  
from OpenGL.GLU import *    
import random
# --- Global coordinates of the point ---
WINDOW_WIDTH, WINDOW_HEIGHT = 500,500
arr2 = []
speed = 0.1
stop = False ## ball is stop moving

unvisible = False ## ball will unvisible

# ===== Function to draw a single point =====
def draw_points(x, y):
    glPointSize(5)          
    glBegin(GL_POINTS)      
    glVertex2f(x, y)        
    glEnd()                



# ===== Set up 2D coordinate system =====
def setup_projection():
    glViewport(0, 0, 500, 500)     
    glMatrixMode(GL_PROJECTION)    
    glLoadIdentity()               
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)  
    glMatrixMode(GL_MODELVIEW)     


# ===== Display callback =====
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                    
    setup_projection()                                  
    for i in arr2:
        if i["Flag"]:
            glColor3f(i["Red"],i["Green"],i["Blue"])
        else:
            glColor3f(0, 0, 0)

        draw_points(i["x"], i["y"])

    glutSwapBuffers()                                  


def animate():
    """Continuously moves the ball diagonally."""

    if not stop:
        for i in arr2:
            i["x"] += i["x_change"] * speed
            i["y"] += i["y_change"] * speed

            if i["x"] >= 500 or i["x"] <= 0:
                i["x_change"] *= -1

            if i["y"] >= 500 or i["y"] <= 0:
                i["y_change"] *=-1

        if unvisible:
            for i in arr2:
                i["Flag"] =not i["Flag"]

    glutPostRedisplay()
    
def mouseListener(button, state, x, y):
    global unvisible 
    if state!=GLUT_DOWN:
        return
    y = 500 - y

    if stop:
        return

    if button == GLUT_LEFT_BUTTON :

        arr = {
            "x": x,
            "y": y,
            "x_change": random.choice([-0.5, 0.5]),
            "y_change": random.choice([-0.5, 0.5]),
            "Red": random.random(),
            "Green": random.random(),
            "Blue": random.random(),
            "Flag":True
        }

        arr2.append(arr)
        glutPostRedisplay()

    elif button == GLUT_RIGHT_BUTTON :
        unvisible = not unvisible

def specialKeyListener(key, x, y):
    global speed

    if unvisible:
        return

    if key == GLUT_KEY_UP: ## speed up
        speed += 0.1
    elif key == GLUT_KEY_DOWN: ## speed down
        speed -= 1

def keyboardListener(key, x, y): ## ball will not move(logic)
    global stop
    if key == b' ':
        stop = not stop

# ===== Main entry point =====
def main():
    glutInit()                              
    glutInitDisplayMode(GLUT_RGBA ) 
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(250, 250)            
    glutCreateWindow(b"OpenGL 2D Point")    
    glutDisplayFunc(display) 
    glutIdleFunc(animate)
    glutMouseFunc(mouseListener)
    glutSpecialFunc(specialKeyListener)
    glutKeyboardFunc(keyboardListener)                
    glutMainLoop()                           

# ===== Run the program =====
if __name__ == "__main__":
    main() 