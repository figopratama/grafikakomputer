import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#mendefinisikan sudut-sudutnya
vertices = (
(1, -1, -1),
(1, 1, -1),
(-1, 1, -1),
(-1, -1, -1),
(1, -1, 1),
(1, 1, 1),
(-1, -1, 1),
(-1, 1, 1)

#Diamond
# (1, -1, 0),
# (1, 1, 0),
# (-1, -1, 0),
# (-1, 1, 0),
# (0, 0, 2.5),
# (0, 0, -2.5),

#Cincin
# (2, 0, 0)
# (1.9, 0.5, 0)
# (1.9, -0.5, 0)
# (1.75, 0.95, 0)
# (1.75, -0.95, 0)
# (1.5, 1.3, 0)
# (1.5, -1.3, 0)
# (1.2, 1.5, 0)
# (1.2, -1.5, 0)
# (0.9, 1.7, 0)
# (0.9, -1.7, 0)
# (0.6, 1.85, 0)
# (0.6, -1.85, 0)
# (0.3, 1.95, 0)
# (0.3, -1.95, 0)
# (0, 2, 0)
# (0, -2, 0)
)


#mendefinisikan garis
edges = (
#Balok
(0, 1),
(0, 3),
(0, 4),
(2, 1),
(2, 3),
(2, 7),
(6, 3),
(6, 4),
(6, 7),
(5, 1),
(5, 4),
(5, 7),


#Diamond
# (0, 1),
# (0, 4),
# (1, 4),
# (0, 2),
# (1, 2),
# (0, 3),
# (2, 3),
# (3, 4),
# (1, 5),
# (2, 5),
# (3, 5),
# (4, 5)

)
#mendefinisikan warna
colors = (
    #Balok
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),

    # (1,0,0),
    # (1,0,0),
    # (0,0,1),
    # (1,0,0),
    # (1,1,1),
    # (0,1,1),
    # (1,0,0),
    # (1,0,0),
    )
#mendefisikan sisi
surfaces = (
    #Balok
    # (0,1,2,3),
    # (3,2,7,6),
    # (6,7,5,4),
    # (4,5,1,0),
    # (1,5,7,2),
    # (4,0,3,6)

    #Diamond
    # (0, 1, 2),
    # (0, 2, 3),
    # (0, 3, 4),
    # (0, 1, 4),
    # (5, 1, 2),
    # (5, 2, 3),
    # (5, 3, 4),
    # (5, 1, 4)
)
#menggambar kubus
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

#menambahkan layar untuk menampilkan kubus
def main():
    #inisialisasi pygame
    pygame.init()
    #resolusi display layar
    display = (800,600)
    #mode layar double buffering
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #mengubah perspektif, fov 45*, znear 0.1, zfar 50
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #memindahkan objek sesuai dengan matrix translate
    glTranslatef(0.0,0.0, -20)
    #infinite looping
    while True:
        #apabila ditekan tombol x, maka program akan berhenti.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #apabila ada tombol keyboard yang ditekan, 
        #maka akan dilakukan fungsi berikut
        if event.type == pygame.KEYDOWN:
            #bila yang di tekan tombol panah kiri
            #pindahkan kubus ke kiri sebanyak 0.5
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.5,0,0)

            if event.key == pygame.K_UP:
                glTranslatef(0,1,0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0,-1,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        
        glRotatef(1, 3, 1, 1)
        #menghapus semua kanvas/display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        #menunggu 10ms sebelum looping lagi
        pygame.time.wait(10) 
main()