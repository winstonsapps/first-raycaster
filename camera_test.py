import pygame
import pygame.camera

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (1280, 720))
cam.start()
size = width, height = 1280, 720
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
    screen.blit(pygame.transform.flip(cam.get_image(), True, True), (0,0))

    pygame.display.flip()
    
    clock.tick(60)


