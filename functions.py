import OpenGL

OpenGL.ERROR_ON_COPY = True

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys
from math import *


def viewInit(evepoint = (0, 0, 100), lookat = (0, 0, 0)):
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
        evepoint[0], evepoint[1], evepoint[2],  # eyepoint
        lookat[0], lookat[1], lookat[2],  # center-of-view
        0, 1, 0,  # up-vector
    )


def drawScene1():
    glPushMatrix()
    try:
        glTranslatef(20, 20, 0)
        glRotatef(250, 1, 0, 0)
        glutWireCone(10, 50, 20, 10)
        glutWireCone(10, -25, 20, 10)
        glColor3ub(255, 255, 0)
    finally:
        glPopMatrix()


def drawScene2(angle):
    glPushMatrix()
    try:
        glRotate(angle, 1, 0, 0)

        glTranslatef(20, 20, 0)
        glRotatef(250, 1, 0, 0)
        glutWireCone(10, 50, 20, 10)
        glutWireCone(10, -25, 20, 10)
        glColor3ub(255, 255, 0)
    finally:
        glPopMatrix()


def drawTorus(size, sp_to, numc, numt):
    glPushMatrix()

    glRotate(90, 1, 0, 0)

    torus = gluNewQuadric()
    gluQuadricDrawStyle(torus, GLU_LINE)

    s = 0.
    t = 0.
    x = 0.
    y = 0.
    z = 0.
    u = 0.
    v = 0.

    twopi = pi * 2

    for i in range(0, numc):
        glBegin(GL_QUAD_STRIP)
        for j in range(0, numt):
            for k in range(1, 0, -1):
                s = (i + k) % numc + 0.5
                t = j % numt

                x = (sp_to + .1 * size * cos(s * twopi / numc)) * cos(t * twopi / numt)
                y = (sp_to + .1 * size * cos(s * twopi / numc)) * sin(t * twopi / numt)
                z = .1 * size * sin(s * twopi / numc)

                u = 2 * (i + k) / numc
                v = 4 * j / numt

                glTexCoord2f(u, v)
                glVertex3f(x * size, y * size, z * size)
        glEnd()



    glPopMatrix()

#float pi = 3.14159265358979323846;
#    	double s, t, x, y, z, twopi;
#    	float u = 0., v= 0.;
#
# 	twopi = 2 * pi;
#
# 	for (int i = 0; i < numc; i++){
# 		glBegin(GL_QUAD_STRIP);
# 	    	for (int j = 0; j <= numt; j++){
# 	    		for (int k = 1; k >= 0; k--){
# 	            	s = (i + k) % numc + 0.5;
# 	            	t = j % numt;
#
# 	            	x = (sp_to +.1 * size*cos(s*twopi/numc))*cos(t*twopi/numt);
# 	            	y = (sp_to +.1 * size *cos(s*twopi/numc))*sin(t*twopi/numt);
# 	            	z = .1 * size * sin(s * twopi / numc);
#
# 	            	u=2*(float)(i + k)/numc;
# 					v=4*(float)j/numt;
# 	            	glTexCoord2f(u, v);
#
# 	            	glVertex3f(x * size, y * size, z * size);
# 	         	}
# 	      	}
# 	    glEnd();
# }
