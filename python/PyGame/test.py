import pygame

screen_width = 1080
screen_height = 720

#initializing everything
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

#changing name
pygame.display.set_caption('cum')

#changing icon
#icon = pygame.image.load(image_name)
#pygame.display.set_icon(icon)

img = pygame.image.load('img.jpg')
img = pygame.transform.scale(img, (700, 300))

start_x = screen_width // 2
start_y = screen_height // 2
change_x, change_y = 0, 0

def cum_user(x, y):
    screen.blit(img, (x, y))

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        #checking if user wants to close window
        if event.type == pygame.QUIT:
            running = False
            break
    start_x += 0.5
    start_y += 0.5
    cum_user(start_x - 300, start_y - 300)
    
    
    
    
    
    
    
    
    
    
    pygame.display.update()
