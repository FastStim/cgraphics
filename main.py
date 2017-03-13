#!/usr/bin/env python3

# This is statement is required by the build system to query build info

import OpenGL

OpenGL.ERROR_ON_COPY = True

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys

starttime = time.time()

def drawCone(position=(0, 0, 0), radius=1, height=2, slices=20, stacks=8):
    glPushMatrix()
    try:
        glTranslatef(*position)
        glRotatef(250, 1, 0, 0)
        glutWireCone(radius, height, slices, stacks)
        glColor3ub(255, 255, 0)
    finally:
        glPopMatrix()


# def coneMaterial():
#     """Setup material for cone"""
#     glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
#     glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.8, 0.8, 0.8, 1.0))
#     glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 0.0, 1.0, 1.0))
#     glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(50.0))
#
#
# def light():
#     """Setup light 0 and enable lighting"""
#     glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_4(0.0, 1.0, 0.0, 1.0))
#     glLightfv(GL_LIGHT0, GL_DIFFUSE, GLfloat_4(1.0, 1.0, 1.0, 1.0))
#     glLightfv(GL_LIGHT0, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))
#     glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(1.0, 1.0, 1.0, 0.0));
#     glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
#     glEnable(GL_LIGHTING)
#     glEnable(GL_LIGHT0)


# def depth():
#     """Setup depth testing"""
#     glDepthFunc(GL_LESS)
#     glEnable(GL_DEPTH_TEST)


def display(swap=1, clear=1):
    """Callback function for displaying the scene
    This defines a unit-square environment in which to draw,
    i.e. width is one drawing unit, as is height
    """
    if clear:
        glClearColor(0.0, 0.0, 0.0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # establish the projection matrix (perspective)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    x, y, width, height = glGetDoublev(GL_VIEWPORT)
    gluPerspective(
        45,  # field of view in degrees
        width / float(height or 1),  # aspect ratio
        .25,  # near clipping plane
        200,  # far clipping plane
    )

    # and then the model view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0, 0, 100,  # eyepoint
        0, 0, 0,  # center-of-view
        0, 1, 0,  # up-vector
    )
    # light()
    # depth()
    # coneMaterial()

    rotation()
    drawCone(radius=10, height=50)
    drawCone(radius=10, height=-25)
    if swap:
        glutSwapBuffers()


def idle():
    glutPostRedisplay()


xd = False
angle = 0


def rotation(period=10):
    global xd
    global angle
    """Do rotation of the scene at given rate"""
    angle = (((time.time() - starttime) % period) / period) * 360
    #glRotate(90, 1, 0, 0)

    # if (angle <= 90 and not xd):

    #     print(angle)
    #     if(angle == 90):
    #         xd = True

    return angle


def key_pressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == '\033':
        sys.exit()


def main():
    import sys
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow('V33')
    glutReshapeWindow(800, 600)
    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
    glutIdleFunc(display)
    # note need to do this to properly render faceted geometry
    glutMainLoop()


if __name__ == "__main__":
    main()
