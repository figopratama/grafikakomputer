import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#mendefinisikan sudut-sudutnya
vertices = (
#Diamond
# (-3, -4, 4), #Titik 0
# (0, -5, 3),  #Titik 1
# (3, -4, 4), #Titik 2
# (5, -2.5, 3), #Titik 3
# (5, 0, 4), #Titik 4
# (5, 2.5, 3), #Titik 5
# (3, 4, 4), #Titik 6
# (0, 5, 3), #Titik 7
# (-3, 4, 4), #Titik 8
# (-5, 2.5, 3), #Titik 9
# (-5, 0, 4), #Titik 10
# (-5, -2.5, 3), #Titik 11

# (-3, -4, 2), #Titik 12
# (0, -5, 2),  #Titik 13
# (3, -4, 2), #Titik 14
# (5, -2.5, 2), #Titik 15
# (5, 0, 2), #Titik 16
# (5, 2.5, 2), #Titik 17
# (3, 4, 2), #Titik 18
# (0, 5, 2), #Titik 19
# (-3, 4, 2), #Titik 20
# (-5, 2.5, 2), #Titik 21
# (-5, 0, 2), #Titik 22
# (-5, -2.5, 2), #Titik 23

(-5, -2.5, 2), #Titik 1
(-5, -2.5, 3), #Titik 2
(-3, -4, 4), #Titik 3
(0, -5, 3),  #Titik 4
(0, -5, 2), #Titik 5
(-3, -4, 2), #Titik 6

# (3, -4, 4), #Titik 7
# (5, -2.5, 3), #Titik 8
# (5, -2.5, 2), #Titik 9
# (3, 4, 2), #Titik 10

# (5, 0, 4), #Titik 11
# (5, 2.5, 3), #Titik 12
# (5, 2.5, 2), #Titik 13
# (5, 0, 2), #Titik 14

# (3, 4, 4), #Titik 15
# (0, 5, 3), #Titik 16
# (0, 5, 2), #Titik 17
# (3, 4, 2), #Titik 18

# (-3, 4, 4), #Titik 19
# (0, 5, 3), #Titik 20
# (0, 5, 2), #Titik 21
# (-3, 4, 2), #Titik 22

# (-5, 0, 4), #Titik 23
# (-5, 0, -2) #Titik 24


)


#mendefinisikan garis
edges = (

    #Balok
    # (0, 1),
    # (0, 3),
    # (0, 4),
    # (2, 1),
    # (2, 3),
    # (2, 7),
    # (6, 3),
    # (6, 4),
    # (6, 7),
    # (5, 1),
    # (5, 4),
    # (5, 7),

    #Diamond
    (0, 1),
    (0, 5),
    (1, 2),
    (3, 2),
    (3, 4),
    (4, 5),

    # (7, 8),
    # (8, 9),
    # (9, 10),
    # (10, 5),

    # (8, 11),
    # (11, 12),
    # (12, 13),
    # (13, 14),

)
#mendefinisikan warna
colors = (
    # #Balok
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 1, 1),
    # (1, 0, 0),

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

    #Crown
    (0, 1, 2, 3, 4, 5)
    # (6, 7, 8, 3, 4, 5),

    # (0, 1, 13, 12, 23, 11),
    # (2, 3, 15, 14, 13, 1),
    # (4, 5, 17, 16, 15, 3),
    # (6, 7, 19, 18, 17, 5),
    # (8, 9, 21, 20, 19, 7),
    # (10, 11, 23, 22, 21, 9),
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
    #mengubah perspektif, fov 90*, znear 0.1, zfar 50
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    #memindahkan objek sesuai dengan matrix translate
    glTranslatef(0.0,0.0, -20)
    #infinite looping
    while True:
        #apabila ditekan tombol x, maka program akan berhenti.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotatef(2, 1, 1, -2)
        #menghapus semua kanvas/display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        #menunggu 10ms sebelum looping lagi
        pygame.time.wait(10) 
main()