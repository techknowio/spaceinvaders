#! /usr/bin/env python3
import pygame
import pygame.mixer
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ishit=0
        self.image = pygame.image.load("spaceship.png").convert()
        self.image = pygame.transform.rotate(self.image,90)
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.y = random.randrange(1, 550)
        self.rect.topleft = 800, self.y
        self.move = random.randrange(1, 5)
        
    def hit(self):
        self.image =pygame.image.load("blackhole.png").convert()
        self.ishit = 1
                
    def update(self):
        if self.ishit == 1:
            self=None
        else:
            self._move()

    def _move(self):
        newpos = self.rect.move((-self.move, 0))
        if self.rect.right == 0:
            self.y = random.randrange(100, 500)
            self.rect.topleft = 800, self.y
            self.move = random.randrange(1, 5)
            newpos = self.rect.move((-self.move, 0))
        self.rect = newpos

def main(): 
    print ("Starting!")
    pygame.init()
    pygame.mixer.init()
    running=1
    linecolor=255,255,255
    bgcolorfire=255,0,0
    x=y=0
    file = "laser.ogg"
    fire = pygame.mixer.Sound(file)
    file = "background.ogg"
    backgroundMusic = pygame.mixer.Sound(file)
    backgroundMusic.play(-1)
    LEFT=1
    FLASH=1
    totalaliens=2
    amountoadd = 5
    totalkilled=0
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Space Invaders')
    amounttoadd=0
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((000, 000, 000))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    alien1 = Alien()
    alienSprites = [alien1,Alien()]
    aliens = pygame.sprite.RenderPlain((alienSprites))

    while running:
        clock.tick(120)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEMOTION:
            x,y=event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            fire.play()
            if FLASH: screen.fill(bgcolorfire)
            pygame.display.flip()
            for a in aliens:
                if a.rect.collidepoint(x,y) == 1:
                    totalkilled = totalkilled +1
                    a.hit()
                    totalaliens=totalaliens-1

        
        if totalaliens == 0:
            print (totalkilled % 10)
            if totalkilled % 10 == 2:
                   amounttoadd=amounttoadd+5
            
            print (amounttoadd)
            myAliens = []
            added = 0
            while added < amounttoadd:
                myAliens.append(Alien())
                added=added+1
                
            alienSprites=myAliens
            totalaliens=added
            aliens = pygame.sprite.RenderPlain((alienSprites))

        aliens.update()
        screen.blit(background, (0, 0))
        aliens.draw(screen)
        pygame.draw.line(screen, linecolor, (x, 0), (x, 599))
        pygame.draw.line(screen, linecolor, (0, y), (799, y))
        pygame.display.flip()

if __name__ == '__main__':
    main()
