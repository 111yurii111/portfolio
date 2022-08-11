import pygame, random,time, os

pygame.init()
screen = pygame.display.set_mode([500,500])
smallfont = pygame.font.SysFont('Corbel',200)

#declaring variables
x = 0
a = 50
b = 50
aa = 50
bb = 50
player_position = [0,0,50,50]
posposx1 = [50, 100,150,200,250,300,350,400,450]
posposy1 = [50, 100,150,200,250,300,350,400,450]

ca1 = [255,0,0]
ca2 = [255,0,0]
ca3 = [255,0,0]
ca4 = [255,0,0]
ca5 = [255,0,0]
win = 0

#randomly renerating apples position
aa1 = random.choice(posposx1)
bb1 = random.choice(posposy1)

aa2 = random.choice(posposx1)
bb2 = random.choice(posposy1)

aa3 = random.choice(posposx1)
bb3 = random.choice(posposy1)

aa4 = random.choice(posposx1)
bb4 = random.choice(posposy1)

aa5 = random.choice(posposx1)
bb5 = random.choice(posposy1)

run = True
str = time.time()
while run:
    screen.fill((255,255,255))
    a = 50
    b = 50
    #draws the apples
    a1 = pygame.draw.rect(screen, (ca1), pygame.Rect(aa1,bb1,50,50))
    a2 = pygame.draw.rect(screen, (ca2), pygame.Rect(aa2,bb2,50,50))
    a3 = pygame.draw.rect(screen, (ca3), pygame.Rect(aa3,bb3,50,50))
    a4 = pygame.draw.rect(screen, (ca4), pygame.Rect(aa4,bb4,50,50))
    a5 = pygame.draw.rect(screen, (ca5), pygame.Rect(aa5,bb5,50,50))


    #draws the lines
    for i in range(9):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(a, 0, 1, 500))
        a += 50

    for i in range(9):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, b, 1000, 1))
        b += 50

    player1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(player_position))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_position == [0,0,50,50] and win >= 5:
                    win += 1
                #colecting apples
                if player_position == [aa1,bb1,50,50] and ca1 != [255,255,255]:
                    ca1 = [255,255,255]
                    win += 1
                if player_position == [aa2,bb2,50,50] and ca2 != [255,255,255]:
                    ca2 = [255,255,255]
                    win +=1
                if player_position == [aa3,bb3,50,50] and ca3 != [255,255,255]:
                    ca3 = [255,255,255]
                    win += 1
                if player_position == [aa4,bb4,50,50] and ca4 != [255,255,255]:
                    ca4 = [255,255,255]
                    win += 1
                if player_position == [aa5,bb5,50,50] and ca5 != [255,255,255]:
                    ca5 = [255,255,255]
                    win += 1
            #movement
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if player_position[0] != 450:
                    player_position[0] += 50
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if player_position[0] != 0:
                    player_position[0] -= 50
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if player_position[1] != 0:
                    player_position[1] -= 50
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if player_position[1] != 450:
                    player_position[1] += 50

    pygame.display.flip()
    if win == 6:
        #final time
        fns = time.time()
        print(round((fns - str), 2))
        run = False
pygame.quit()
