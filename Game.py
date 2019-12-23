import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Cubes Game")
x = 50
y = 425
widht = 40
height = 60
speed = 5
isJump = False
jumpCount = 10
run=True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
    if keys[pygame.K_RIGHT] and x<500-widht -5 :
        x += speed
    if not(isJump):
        if keys[pygame.K_UP] and y>5:
            y-= speed
        if keys[pygame.K_DOWN] and y<500-height-15:
            y+=speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255), (x, y , widht, height))
    pygame.display.update()

pygame.quit()