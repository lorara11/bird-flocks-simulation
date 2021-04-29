"""
Functions used to render graphics.
"""
#2D          
vertices = ((param.X_MAX, param.Y_MIN),
            (param.X_MAX, param.Y_MAX),
            (param.X_MIN, param.Y_MAX),
            (param.X_MIN, param.Y_MIN))

edges = ((0,1), (1,2), (2,3), (3,0))

###3D
# vertices = ((param.X_MAX, param.Y_MIN, param.Z_MIN),
#             (param.X_MAX, param.Y_MAX, param.Z_MIN),
#             (param.X_MIN, param.Y_MAX, param.Z_MIN),
#             (param.X_MIN, param.Y_MIN, param.Z_MIN),
#             (param.X_MAX, param.Y_MIN, param.Z_MAX),
#             (param.X_MAX, param.Y_MAX, param.Z_MAX),
#             (param.X_MIN, param.Y_MIN, param.Z_MAX),
#             (param.X_MIN, param.Y_MAX, param.Z_MAX))

# edges = ((0,1),(0,3),(0,4),
#          (2,1),(2,3),(2,7),
#          (6,3),(6,4),(6,7),
#          (5,1),(5,4),(5,7),)

def draw_container():
    """Draws 2D square or 3D cube that contains birds"""
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()


def drawBirds(birds: list):
    """ Draws the birds """

    ###rotate_x, rotate_y, rotate_z = 0,0,0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0.0, 0.0, 10.0)
                elif event.button == 5:
                    glTranslatef(0.0, 0.0, -10.0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    #reset birds
                    ### change
                    i = 0
                    for b in initialize_birds.generateBirds():
                        birds[i] = b
                        i += 1
                
                ### ROTATIONS
                # if event.key == pygame.K_w:
                #     rotate_x = 5
                # if event.key == pygame.K_s:
                #     rotate_x = -5
                # if event.key == pygame.K_a:
                #     rotate_y = 5
                # if event.key == pygame.K_d:
                #     rotate_y = -5
                # if event.key == pygame.K_q:
                #     rotate_x = 5
                # if event.key == pygame.K_e:
                #     rotate_x = -5
            
            ### ROTATIONS
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_w:
            #         rotate_x = 0
            #     if event.key == pygame.K_s:
            #         rotate_x = 0
            #     if event.key == pygame.K_a:
            #         rotate_y = 0
            #     if event.key == pygame.K_d:
            #         rotate_y = 0
            #     if event.key == pygame.K_q:
            #         rotate_x = 0
            #     if event.key == pygame.K_e:
            #         rotate_x = 0
        
        ### ROTATIONS
        # glRotatef(rotate_x, 1, 0, 0)
        # glRotatef(rotate_y, 0, 1, 0)
        # glRotatef(rotate_z, 0, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1,1,1,0)

        draw_container()

        for bird in birds:
            head = bird.position
            tail_centre = (bird.position[0]-22*bird.direction[0],
                           bird.position[1]-22*bird.direction[1]###,
                           ###bird.position[2]-22*bird.direction[2]
                          )

            temp_dir = []

            if bird.direction[1] != 0:
                temp_dir = [1, (-bird.direction[0])/(bird.direction[1])]
                ###temp_dir = [1, (-bird.direction[0])/(bird.direction[1]), 0]
            ###elif bird.direction[2] != 0:
            ###    temp_dir = [1, 1,(-bird.direction[0]-bird.direction[1])/bird.direction[2]]
            else:
                temp_dir = [(-bird.direction[1])/bird.direction[0],1]
                ###temp_dir = [(-bird.direction[1])/bird.direction[0],1,0]

            module = math.sqrt(temp_dir[0]**2+temp_dir[1]**2)
            temp_dir = [temp_dir[0]/module, temp_dir[1]/module]
            ###module = math.sqrt(temp_dir[0]**2+temp_dir[1]**2+temp_dir[2]**2)
            ###temp_dir = [temp_dir[0]/module, temp_dir[1]/module, temp_dir[2]/module]

            tail_square1 = (tail_centre[0]-8*temp_dir[0],
                           tail_centre[1]-8*temp_dir[1]###,
                           ###tail_centre[2]-8*temp_dir[2]
                           )
            tail_square2 = (tail_centre[0]+8*temp_dir[0],
                           tail_centre[1]+8*temp_dir[1]###,
                           ###tail_centre[2]+8*temp_dir[2]
                           )

            # Draw triangle
            glBegin(GL_TRIANGLES)
            glColor3fv((1,1,1))
            glVertex2fv((int(head[0]),int(head[1])))
            ###glVertex3fv((int(head[0]),int(head[1]),int(head[2])))
            glVertex2fv((int(tail_square1[0]),int(tail_square1[1])))
            ###glVertex3fv((int(tail_square1[0]),int(tail_square1[1]),int(tail_square1[2])))
            glVertex2fv((int(tail_square2[0]),int(tail_square2[1])))
            ###glVertex3fv((int(tail_square2[0]),int(tail_square2[1]),int(tail_square2[2])))
            glEnd()

        pygame.display.flip()

        clock.tick(30)  # 30 fps

