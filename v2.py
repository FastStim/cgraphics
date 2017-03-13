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
is_rotating = True

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

        glTranslatef(-20, 0, 0)
        glRotate(45, 1, 0, 0)
        glutWireTorus(5, 10, 20, 20)

        glPopMatrix()

        #cylinder
        glPushMatrix()

        glTranslatef(20, 0, 0)
        glRotate(45, 1, 0, 0)

        quadratic = gluNewQuadric()
        gluQuadricDrawStyle(quadratic, GLU_LINE)
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluCylinder(quadratic, 5.0, 5.0, 20.0, 32, 32)

        # radius = 10
        # halfLength = 10
        # slices = 20
        # for i in range(0, slices - 1):
        #     theta = 2.0 * pi * i
        #     nextTheta = 2.0 * pi * float(i + 1)
        #     glBegin(GL_TRIANGLE_STRIP)
        #     glVertex3f(0.0, halfLength, 0.0)
        #     glVertex3f(radius * cos(theta), halfLength, radius * sin(theta))
        #     glVertex3f(radius * cos(nextTheta), -halfLength, radius * sin(nextTheta))
        #     glVertex3f(0.0, -halfLength, 0.0)
        #     glEnd()

        # float
        # radius, halfLength;
        # int
        # slices;
        # for (int i=0; i < slices; i++) {
        # float theta = ((float)i) * 2.0 * M_PI;
        # float nextTheta = ((float)i+1) * 2.0 * M_PI;
        # glBegin(GL_TRIANGLE_STRIP);
        # / * vertex at middle of end * / glVertex3f(0.0, halfLength, 0.0);
        # / * vertices at edges of circle * / glVertex3f(radius * cos(theta), halfLength, radius * sin(theta));
        # glVertex3f (radius * cos(nextTheta), halfLength, radius * sin(nextTheta));
        # / * the same vertices at the bottom of the cylinder * /
        # glVertex3f (radius * cos(nextTheta), -halfLength, radius * sin(nextTheta));
        # glVertex3f(radius * cos(theta), -halfLength, radius * sin(theta));
        # glVertex3f(0.0, -halfLength, 0.0);
        # glEnd();
        # }

        glPopMatrix()

        #drawScene3(10, 1, 20, 20)


    if swap:
        glutSwapBuffers()
    # print("displaying scene: " + str(scene))


def idle():
    # print("idle")
    global angle
    global is_rotating

    if is_rotating and angle < 90:
        angle = (((time.time() - start_time) % period) / period) * 360
        if angle == 90:
            is_rotating = False
    glutPostRedisplay()


def key_pressed(*args):
    global scene
    global is_rotating
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
        scene = 4



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