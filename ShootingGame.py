#!/usr/bin/python
'''
Created on Aug 25, 2015

@author: justin
'''
import sys, pygame
from random import randint
import math
pygame.init()
pygame.display.set_caption("*Shooting Noises*")

class Ship(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location

def animateShip():
    screen.blit(ship.image, ship.rect)
    
def explosionQuestionMark():
    global health, boomInterval, page
    if health <= 0:
        boomInterval += 2
        freq = 90
        boomInterval = boomInterval % freq

        imageNumber = (boomInterval % freq) / 10 + 1
        ship.image = pygame.image.load("myShipExplosion/sprite_" + str(imageNumber) + ".png")
        
        if boomInterval % freq == 88:
            page = 2
            screen = pygame.display.set_mode([width, height]);
        
class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("healthBar/healthBar1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [500, 50]

def drawHealthBar():
    if health >= 0:
        number = 11 - health/10
        healthBar.image = pygame.image.load("healthBar/healthBar" + str(number) + ".png")
    else:
        healthBar.image = pygame.image.load("healthBar/healthBar11.png")
    
    screen.blit(healthBar.image, healthBar.rect)

class BackgroundObject(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location

def animateBullets():
    global bulletInterval
    bulletInterval += 1
    freq = 3
    bulletInterval = bulletInterval % freq
        
    for bullet in bullets:
        bullet.rect.centery -= 20
        if bullet.rect.centery < -1000:
            bullets.remove(bullet)
        screen.blit(bullet.image, bullet.rect)

def generateTrees():
    global treeInterval
    treeInterval += 1
    freq = 5
    treeInterval = treeInterval % freq
    if treeInterval % freq == 0:
        newTree = BackgroundObject("backgroundObjects/otherTree.png", [randint(0, width), randint(-height, 0)])
        treeList.append(newTree)
        treePerClump = randint(0, 20)
        rang = 30
        for i in range(treePerClump):
            newerTree = BackgroundObject("backgroundObjects/otherTree.png", [newTree.rect.centerx + randint(-rang, rang), newTree.rect.centery + randint(-rang, rang)])
            treeList.append(newerTree)
    for tree in treeList:
        tree.rect.centery += 5
        if tree.rect.top > height + 2000:
            treeList.remove(tree)
    for tree in treeList:
        screen.blit(tree.image, tree.rect)
            
def generatePonds():
    global pondInterval
    pondInterval += 1
    freq = 10
    pondInterval = pondInterval % freq
    if pondInterval % freq == 0:
        newPond = BackgroundObject("backgroundObjects/pondTest.png", [randint(0, width), randint(-height, 0)])
        pondList.append(newPond)
    for pond in pondList:
        pond.rect.centery += 5
        if pygame.sprite.spritecollide(pond, treeList, False):
            pondList.remove(pond)
        if pond.rect.top > height + 2000:
            pondList.remove(pond)
    for pond in pondList:        
        screen.blit(pond.image, pond.rect)
        
def generateClouds():
    global cloudInterval
    cloudInterval += 1
    freq = 5
    cloudInterval = cloudInterval % freq
    if cloudInterval % freq == 0:
        cloudNum = randint(1, 3)
        if cloudNum == 1:
            newCloud = BackgroundObject("backgroundObjects/cloud.png", [randint(0, width), randint(-height, 0)])
            cloudList.append(newCloud)
        elif cloudNum == 2:
            newCloud = BackgroundObject("backgroundObjects/secondCloud.png", [randint(0, width), randint(-height, 0)])
            cloudList.append(newCloud)
        elif cloudNum == 3:
            newCloud = BackgroundObject("backgroundObjects/fourthCloud.png", [randint(0, width), randint(-height, 0)])
            cloudList.append(newCloud)
    for cloud in cloudList:
        cloud.rect.centery += 7
        if cloud.rect.top > height + 2000:
            cloudList.remove(cloud)
    for cloud in cloudList:        
        screen.blit(cloud.image, cloud.rect)
        
class Buttons(pygame.sprite.Sprite):
    def __init__(self, location, state):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("startScreen/notPressed.png")
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.pressed = state
    def pressedButton(self):
        self.image = pygame.image.load("startScreen/pressed.png")
        self.pressed = True
    def notPressedButton(self):
        self.image = pygame.image.load("startScreen/notPressed.png")
        self.pressed = False

def drawButtons():
    for button in buttonList:
        screen.blit(button.image, button.rect)
   
def chooseWave():
    global wave
    if len(enemyOneList) == 0:      
        wave = randint(0, 3)
        if wave == 1:
            formationOne = [[500, -550], [500, -50], [50, -300], [950, -300], \
                            [275, -425], [725, -425], [275, -175], [725, -175]]
            for i in range(len(formationOne)):
                enemy1 = Enemies("enemy1.png", formationOne[i])
                enemyOneList.append(enemy1)
        elif wave == 2:
            formationTwo = [[450, -350], [550, -350], [450, -250], [550, -250]]
            for i in range(len(formationTwo)):
                enemy1 = Enemies("enemy1.png", formationTwo[i])
                enemyOneList.append(enemy1)
        elif wave == 3:
            formationThree = [[200, -480], [400, -480], [600, -480], [800, -480], \
                              [200, -360], [400, -360], [600, -360], [800, -360], \
                              [200, -240], [400, -240], [600, -240], [800, -240], \
                              [200, -120], [400, -120], [600, -120], [800, -120]]
            for i in range(len(formationThree)):
                enemy1 = Enemies("enemy1.png", formationThree[i])
                enemyOneList.append(enemy1)
        
class Enemies(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.status = 0
        self.dead = False

class enemy1Bullets(pygame.sprite.Sprite):        
    def __init__(self, location, vector):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("enemy1Bullets.png")
            self.rect = self.image.get_rect()
            self.rect.center = location
            self.vector = vector

def animateEnemyOne():
    global score, bombs
    diff = 4
    i = 0
    for enemy in enemyOneList:
        for bullet in bullets:
            if pygame.sprite.spritecollide(bullet, [enemy], False) and enemy.dead == False and bullet.rect.top >= 0:
                enemy.dead = True
                bullets.remove(bullet)
    for j in range(len(enemyOneList)):
        screen.blit(enemyOneList[i].image, enemyOneList[i].rect)
        enemyOneList[i].rect.centery += 10
        if enemyOneList[i].rect.top >= 600:
            enemyOneList.remove(enemyOneList[i])
            i -= 1
        elif enemyOneList[i].dead == True:            
            enemyOneList[i].status += 1
            
            if enemyOneList[i].status >= diff and enemyOneList[i].status <= diff * 10:
                number = enemyOneList[i].status/diff
                enemyOneList[i].image = pygame.image.load("enemyExplosionParts/enemy1." + str(number) + ".png")
            elif enemyOneList[i].status > diff * 11:
                enemyOneList[i].image = pygame.image.load("enemyExplosionParts/enemy1.10.png")
                enemyOneList[i].dead = False
                enemyOneList.remove(enemyOneList[i])
                i -= 1
                score += 2000
                
                prob = randint(1, 100)
                if prob <= 5:
                    bombs += 1
        i += 1
    enemyOneShoot()
    
def enemyOneShoot():
    global bullet1Freq, health
    bullet1Interval = 50
    diff = 8
    bullet1Freq += 1
    bullet1Freq = bullet1Freq % bullet1Interval
    if bullet1Freq % bullet1Interval == 0 or bullet1Freq % bullet1Interval == diff or bullet1Freq % bullet1Interval == diff * 2 or bullet1Freq % bullet1Interval == diff * 3 or bullet1Freq % bullet1Interval == diff * 4:   
        for enemy in enemyOneList:
            if enemy.rect.centery > 0 and enemy.dead == False:
                speed = 10
                xlen = mousex - enemy.rect.centerx
                ylen = mousey - enemy.rect.centery
                distToMouse = math.sqrt(math.pow(xlen, 2) + math.pow(ylen, 2))
                newVector = [(xlen/distToMouse) * speed, (ylen/distToMouse) * speed]
                newBullet = enemy1Bullets([enemy.rect.centerx, enemy.rect.centery], newVector)
                enemyOneBulletList.append(newBullet)
    i = 0
    for j in range(len(enemyOneBulletList)):
        enemyOneBulletList[i].rect.centerx += enemyOneBulletList[i].vector[0]
        enemyOneBulletList[i].rect.centery += enemyOneBulletList[i].vector[1]
        if enemyOneBulletList[i].rect.centerx >= 1000 or enemyOneBulletList[i].rect.centerx <= 0 or enemyOneBulletList[i].rect.centery >= 600 or enemyOneBulletList[i].rect.centery <= 0:
            enemyOneBulletList.remove(enemyOneBulletList[i])
            i -= 1
        i += 1
    a = 0
    for b in range(len(enemyOneBulletList)):
        if pygame.sprite.spritecollide(enemyOneBulletList[a], [ship], False):
            health -= 10
            enemyOneBulletList.remove(enemyOneBulletList[a])
            a -= 1
        a += 1
            
    for bullet in enemyOneBulletList:
        screen.blit(bullet.image, bullet.rect)
        
def killAllEnemies():
    for enemy in enemyOneList:
        enemy.dead = True
        
def animateCurrentWave():
    animateEnemyOne()
    
def showScore():
    global increment, increcrement, score
    increment += increcrement;
    score += increment;
    
    scoreString = scoreFont.render(str(score), 1, (0, 0, 0))
    screen.blit(scoreString, [1025, 200])
    
def youDied():
    deathString = deathFont.render("You died!", 1, (0, 0, 0))
    screen.blit(deathString, [width/2 - deathString.get_width()/2, height/2 - deathString.get_height()/2])

def drawInstructions():
    instructString = buttonFont.render("Press space to shoot", 1, (0, 0, 0))
    screen.blit(instructString, [700, 400])
    instructString2 = buttonFont.render("Use mouse to move", 1, (0, 0, 0))
    screen.blit(instructString2, [700, 425])
    instructString3 = buttonFont.render("Click to use bombs", 1, (0, 0, 0))
    screen.blit(instructString3, [700, 450])
    
def showBombs():
    global bombs
    coords = [[1060, 450], [1120, 450], [1180, 450], [1240, 450], [1060, 550], [1120, 550], [1180, 550], [1240, 550]]
    
    if bombs > 8:
        bombs = 8
    
    for i in range(bombs):
        screen.blit(pygame.image.load("Missile.png"), [coords[i][0] - 10.5, coords[i][1] - 45])
        
size = width, height = [1000, 600]
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
bullets = []
bulletInterval = 0
treeList = []
treeInterval = 0
pondList = []
pondInterval = 0
cloudList = []
cloudInterval = 0
buttonList = []
mouseButtonPos = mousex, mousey = [width/2, height/2]
paused = False
page = 0
buttonFont = pygame.font.Font(None, 25)
titleFont = pygame.font.Font(None, 50)
deathFont = pygame.font.Font(None, 75)
scoreFont = pygame.font.Font(None, 50)
scoreboard = pygame.Surface([300, height])
scoreboard = pygame.image.load("backgroundObjects/newerScoreboard.png")
score = 0;
increment = 1;
increcrement = 1;

#enemies
wave = 0
enemyOneList = []
enemyOneBulletList = []
bullet1Freq = 0

delay = 100
interval = 100
pygame.key.set_repeat(delay, interval)

ship = Ship('myShip/newerShip.png', [width/2, height/2])
boomInterval = 0
health = 100

healthBar = HealthBar()

bombs = 3

startScreen = BackgroundObject("startScreen/trialStartBigger.png", [width/2, height/2])
startButton = Buttons([width/2, height/2], False)
buttonList.append(startButton)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_p and page == 1:
                if paused == True:
                    paused = False
                else:
                    paused = True
            elif event.key == pygame.K_SPACE and paused == False and page == 1:
                newBullet = BackgroundObject("myShip/fireBullet.png", [ship.rect.left, ship.rect.top + 40])
                newSecondBullet = BackgroundObject("myShip/fireBullet.png", [ship.rect.right, ship.rect.top + 40])
                bullets.append(newBullet)
                bullets.append(newSecondBullet)
            elif event.key == pygame.K_b:
                health = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and page == 0:
            mouseButtonPos = event.pos
            if mouseButtonPos[0] <= startButton.rect.right and mouseButtonPos[0] >= startButton.rect.left and mouseButtonPos[1] <= startButton.rect.bottom and mouseButtonPos[1] >= startButton.rect.top:
                screen = pygame.display.set_mode([width + 300, height])
                page = 1
        elif event.type == pygame.MOUSEMOTION and page == 0:
            mouseButtonPos = event.pos
            if mouseButtonPos[0] <= startButton.rect.right and mouseButtonPos[0] >= startButton.rect.left and mouseButtonPos[1] <= startButton.rect.bottom and mouseButtonPos[1] >= startButton.rect.top:
                startButton.pressedButton()
            else:
                startButton.notPressedButton()
        elif event.type == pygame.MOUSEMOTION and paused == False and page == 1:
            mousex = event.pos[0]
            mousey = event.pos[1]
            if mousex <= width:
                ship.rect.center = mousex, mousey
        elif event.type == pygame.MOUSEBUTTONDOWN and page == 1 and paused == False:
            killAllEnemies()
            bombs -= 1
            
    if page == 0:
        screen.fill([0, 255, 255])
        screen.blit(startScreen.image, startScreen.rect)
        drawButtons()
        title = titleFont.render("Not-So-Perfect Cherry Blossom", 1, (0, 0, 0))
        screen.blit(title, [width/2 - title.get_width()/2, 100])
        sbt = buttonFont.render("Start!", 1, (0, 0, 0))
        screen.blit(sbt, [startButton.rect.centerx - sbt.get_width()/2, startButton.rect.centery - sbt.get_height()/2])
        drawInstructions()
    if paused == False and page == 1:
        pygame.mouse.set_visible(False)
        screen.fill([163, 148, 34])
        generateTrees()
        generatePonds()
        generateClouds()
        chooseWave()
        animateCurrentWave()
        animateShip()
        explosionQuestionMark()
        animateBullets()
        drawHealthBar()
        screen.blit(scoreboard, [width, 0])
        showScore()
        showBombs()
    if page == 2:
        pygame.mouse.set_visible(True)
        screen.fill([0, 255, 255])
        youDied()
    pygame.display.flip()
    clock.tick(30)