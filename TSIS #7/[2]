import pygame


pygame.init()
FPS=pygame.time.Clock()

sc=pygame.display.set_mode((1000, 800))
pygame.display.set_caption("music player")

Playlist=['first.mp3', 'second.mp3', 'third.mp3']
curm=0
curs=pygame.mixer.music.load(Playlist[curm])
pygame.mixer.music.play()
pygame.mixer.music.pause()
m1 = m2 = m3 = False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if(m1):
                    pygame.mixer.music.pause()
                    m1=0
                else:
                    pygame.mixer.music.unpause()
                    m1=1
            if event.key==pygame.K_RIGHT:
                curm=(curm+1)%3
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Playlist[curm])
                pygame.mixer.music.play()
                m2=True
                if not m1 :
                    pygame.mixer.music.pause()
            if event.key==pygame.K_LEFT:
                curm=(curm-1+3)%3
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Playlist[curm])
                pygame.mixer.music.play()
                m3=True
                if not m1 :
                    pygame.mixer.music.pause()
                   

    pygame.display.update()
    FPS.tick(60)