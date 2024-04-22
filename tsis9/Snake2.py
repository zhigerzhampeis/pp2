import pygame,random,sys

pygame.init()
#we use points to create the squares of our snake
class Point: 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self,p):
        if self.x==p.x and self.y==p.y:
            return True
        else:
            return False

BLOCK = 20
font = pygame.font.Font(None,25)
#create snake class and initialize it to starting pos, score and level 
class Snake: 
    def __init__(self, w=640, h=480):
        self.ScreenW = w
        self.ScreenH = h
        self.state = True
        # init screen
        self.screen = pygame.display.set_mode((self.ScreenW, self.ScreenH))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        
        # init game state
        self.xdir = 1
        self.ydir = 0
        
        self.head = Point(self.ScreenW/2, self.ScreenH/2)
        self.body = [Point(self.head.x-BLOCK, self.head.y),
                      Point(self.head.x-(2*BLOCK), self.head.y)]
        self.score = 0
        self.speed = 10
        self.level = 1
        self.food = None
        self.new_food()
        self.time = pygame.time.get_ticks()
        self.delta = 5000

    def new_food(self): #random spawn of foods
        time = pygame.time.get_ticks()
        x = random.randint(0, (self.ScreenW-BLOCK)//BLOCK)*BLOCK
        y = random.randint(0, (self.ScreenH-BLOCK)//BLOCK)*BLOCK
        self.food = Point(x, y)
        if self.food in self.body or self.food==self.head:
            self.new_food()
        #weighted generation of foods
        food = ['apple','orange', 'melon']
        self.food_type = random.choices(food,weights=[5,4,1],k=1)[0]

    def move(self):
        for event in pygame.event.get(): #to exit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not self.state: #after game over use space to restart
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.xdir = 1
                        self.ydir = 0
            
                        self.head = Point(self.ScreenW/2, self.ScreenH/2)
                        self.body = [Point(self.head.x-BLOCK, self.head.y),
                                    Point(self.head.x-(2*BLOCK), self.head.y)]
                        self.score = 0
                        self.speed = 10
                        self.level = 1
                        self.food = None
                        self.new_food()
                        self.time = pygame.time.get_ticks()
                        self.state = True

            keys = pygame.key.get_pressed() #checking user input
            
            if keys[pygame.K_LEFT]:
                self.ydir = 0
                self.xdir = -1

            elif keys[pygame.K_RIGHT]:
                self.ydir = 0
                self.xdir = 1

            elif keys[pygame.K_UP]:
                self.ydir = -1
                self.xdir = 0

            elif keys[pygame.K_DOWN]:
                self.ydir = 1
                self.xdir = 0
        if self.state: #moving the snake squares one by one
            for i in range(len(self.body)-1):
                self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
            self.body[len(self.body)-1].x, self.body[len(self.body)-1].y = self.head.x, self.head.y
            self.head.x += self.xdir * BLOCK
            self.head.y += self.ydir * BLOCK

    def update(self): #Drawing to the screen using draw method
        if self.state:
            self.screen.fill("black")
            pygame.draw.rect(self.screen, "green",  pygame.Rect(self.head.x, self.head.y, BLOCK, BLOCK))
            for sqr in self.body:
                pygame.draw.rect(self.screen, "green", pygame.Rect(sqr.x, sqr.y, BLOCK, BLOCK)) 
            if self.food_type=='apple':
                pygame.draw.rect(self.screen,"red", pygame.Rect(self.food.x, self.food.y, BLOCK, BLOCK))
            elif self.food_type=='orange':
                pygame.draw.circle(self.screen,"orange",(self.food.x+BLOCK/2,self.food.y+BLOCK/2),BLOCK/2)
            elif self.food_type=='melon':
                pygame.draw.ellipse(self.screen,"yellow", pygame.Rect(self.food.x, self.food.y, BLOCK+5, BLOCK))

        text_score = font.render("Score: " + str(self.score), True, "white")
        text_level = font.render("Level: " + str(self.level), True, "white")
        self.screen.blit(text_score, (0,0))
        self.screen.blit(text_level, (0,25))
        pygame.display.flip()

    def collision(self): #defining the collision process
        for sqr in self.body:
            if self.head.x == sqr.x and self.head.y == sqr.y:
                for i in self.body:
                    return True
            if self.head.x not in range(0, self.ScreenW) or self.head.y not in range(0, self.ScreenH):
                return True
            
    def start(self):
        #moving the snake
        self.move()
        if self.state:
            #check for collision
            if self.collision():
                self.state = False
            #creating delta_time variable to keep track of 
            #how many second passed after creating new food
            self.delta_time = pygame.time.get_ticks() - self.time
            if self.delta_time > self.delta:
                self.new_food()
                self.time = pygame.time.get_ticks()
            #generate new food
            if self.head == self.food:
                self.time = pygame.time.get_ticks()
                self.score += 1
                if self.score%4==0:
                    self.level+=1
                    self.speed+=5
                self.body.append(Point(self.food.x,self.food.y))
                self.new_food()
        else:
            self.screen.fill("black")
            text1 = font.render("Score: " + str(self.score),True,"white")
            text2 = font.render("Press space to restart",True,"white")
            self.screen.blit(text1, (self.ScreenW/2-30,self.ScreenH/2-50))
            self.screen.blit(text2,(self.ScreenW/2-80,self.ScreenH/2))
        #Update everything
        self.update()
        self.clock.tick(self.speed)
        
game = Snake()
while True: #game loop
    game.start()