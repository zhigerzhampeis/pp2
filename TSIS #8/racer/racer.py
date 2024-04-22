import pygame
import os
from random import randint 
os.chdir(r"C:\Users\Murat\OneDrive\Рабочий стол\pp2-22B031132\TSIS #8\racer")

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2500)
FPS = pygame.time.Clock()

W,H = 400, 600
sc = pygame.display.set_mode((W, H))
bg = pygame.image.load('images\AnimatedStreet.png').convert_alpha()
score = pygame.image.load('images\score_fon.png').convert_alpha()
f = pygame.font.Font(None, 40)

class Enemy(pygame.sprite.Sprite):                                      #Sprite of Enemy
    def __init__(self, x, speed, filename, group):                      #
        pygame.sprite.Sprite.__init__(self)                             #
        self.image = pygame.image.load(filename).convert_alpha()        #
        self.rect = self.image.get_rect(center=(x, 0))                  #
        self.speed = speed                                              #
        self.add(group)                                                 #
    def update(self, *args):                                            #
        if self.rect.y < args[0] - 20:                                  #
            self.rect.y += self.speed                                   #
        else:                                                           #
            self.kill()                                                 #

enemy = pygame.sprite.Group()                                           #Created sprite group for enemys
def createEnemy(group):                                                 #
    return Enemy(randint(40, W-40), 3, 'images\Enemy.png', group)       #
createEnemy(enemy)                                                      #

def collideEnemys():                                #Enemy collision detection
    for i in enemy:                                 #
        if p_rect.collidepoint(i.rect.center):      #
            exit()                                  #


class Coin(pygame.sprite.Sprite):                                   #Class of Coin
    def __init__(self, x, speed, score, filename, group):           #
        pygame.sprite.Sprite.__init__(self)                         #
        self.image = pygame.image.load(filename).convert_alpha()    #
        self.rect = self.image.get_rect(center=(x, 0))              #
        self.speed = speed                                          #
        self.score = score                                          #
        self.add(group)                                             #
                                                                    #
    def update(self, *args):                                        #
        if self.rect.y < args[0] - 20:                              #
            self.rect.y += self.speed                               #
        else:                                                       #
            self.kill()                                             #

coin = pygame.sprite.Group()                                            #Created sprite group for coins,
def createCoin(group):                                                  # which is similar to enemy's sprite group.     
    return Coin(randint(20, W-20), 4, 50, 'images\lemor.png', group)    #
createCoin(coin)                                                        #


game_score = 0
player = pygame.image.load('images/Player.png').convert_alpha()
p_rect = player.get_rect(centerx=W//2, bottom=H-5)


def collideCoins():                                 #Coins collision detection
    global game_score                               #
    for i in coin:                                  #
        if p_rect.collidepoint(i.rect.center):      #
            game_score += i.score                   #
            i.kill()                                #

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    
        elif event.type == pygame.USEREVENT:
            createEnemy(enemy)
            if randint(1,3)%3 == 0:      #<------Chance of appereance of coin is 1/3, 
                createCoin(coin)                # it will appear together with enemys.
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p_rect.x -= 5
        if p_rect.x < 0:
            p_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        p_rect.x += 5
        if p_rect.x > W-p_rect.width:
            p_rect.x = W-p_rect.width


    sc.blit(bg, (0, 0))
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (0, 0, 0))
    sc.blit(sc_text, (20, 15))
    sc.blit(player, p_rect)
    collideEnemys(); collideCoins()
    enemy.draw(sc); enemy.update(H)
    coin.draw(sc); coin.update(H)
    pygame.display.update()
    FPS.tick(60)

    
