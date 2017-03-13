#!/usr/bin/env python3

import OpenGL

OpenGL.ERROR_ON_COPY = True

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys

from functions import *

start_time = time.time()
period = 10
angle = 0
is_rotating = False

is_torus_rotating = False

scene = 1

def display(swap = 1, clear = 1):
    if clear:
        glClearColor(0.0, 0.0, 0.0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # establish the projection matrix (perspective)

    viewInit(lookat=(20, 20, 0))

    if scene == 1: # two cone
        drawScene1()
    elif scene == 2: #rotation
        drawScene2(angle)
    elif scene == 3:
        viewInit(evepoint=(0, 0, 100), lookat=(0,0,0))
        #torus
        glPushMatrix()
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        glTranslatef(-20, 0, 0)
        glRotate(45, 1, 0, 0)

        drawTorus(5, .9999, 20, 20)

        #glutWireTorus(5, 10, 20, 20)

        glPopMatrix()

        #cylinder
        glPushMatrix()

        glTranslatef(20, 0, 0)
        glRotate(45, 1, 0, 0)

        quadratic = gluNewQuadric()
        gluQuadricDrawStyle(quadratic, GLU_LINE)
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluCylinder(quadratic, 5.0, 5.0, 20.0, 32, 32)

        glPopMatrix()
    elif scene == 4:
        viewInit(evepoint=(0, 0, 100), lookat=(0, 0, 0))
        # torus
        glPushMatrix()

        glRotate(angle, 0, 0, 1)

        glTranslatef(-20, 0, 0)
        glRotate(45, 1, 0, 0)
        glutWireTorus(5, 10, 20, 20)

        glPopMatrix()

        # cylinder
        glPushMatrix()

        glScalef(2, 2, 2)

        glTranslatef(20, 0, 0)
        glRotate(45, 1, 0, 0)

        quadratic = gluNewQuadric()
        gluQuadricDrawStyle(quadratic, GLU_LINE)
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluCylinder(quadratic, 5.0, 5.0, 20.0, 32, 32)

        glPopMatrix()


    if swap:
        glutSwapBuffers()


def idle():
    # print("idle")
    global angle
    global is_rotating
    global is_torus_rotating
    global scene

    if scene == 2:
        if is_rotating and angle < 90:
            angle = (((time.time() - start_time) % period) / period) * 360
            if angle == 90:
                is_rotating = False
    if scene == 4:
        if is_torus_rotating and angle > -45:
            angle = (((time.time() - start_time) % period) / period) * -360
            if angle == -45:
                is_torus_rotating = False

    glutPostRedisplay()


def key_pressed(*args):
    global scene
    global is_rotating
    global is_torus_rotating
    global angle
    global start_time
    # print("key pressed: ", ord(args[0]))
    # If escape is pressed, kill everything.
    if ord(args[0]) == 27:
        sys.exit()
    elif ord(args[0]) == 49:
        scene = 1
    elif ord(args[0]) == 50:
        start_time = time.time()
        angle = 0
        is_rotating = True
        scene = 2
    elif ord(args[0]) == 51:
        scene = 3
    elif ord(args[0]) == 52:
        start_time = time.time()
        angle = 0
        is_torus_rotating = True
        scene = 4
    elif ord(args[0]) == 53:
        scene = 5
    elif ord(args[0]) == 54:
        scene = 6



def main():
    import sys
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow('V33 lab1')
    glutReshapeWindow(800, 600)
    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
    glutIdleFunc(idle)
    glutMainLoop()


if __name__ == "__main__":
    main()
