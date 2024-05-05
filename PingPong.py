from pygame import *
from random import randint

window = display.set_mode((700,500))
back = (211,210,0)
window.fill(back)
Clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
      sprite.Sprite.__init__(self)
      self.image = transform.scale(image.load(player_image), (width, height))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
    def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 400:
           self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed



font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
font3 = font.Font(None, 36)
font4 = font.Font(None, 36)

rocket1 = Player("Plate.png", 660, 250, 20, 100, 10)
rocket2 = Player("Plate.png", 40, 250, 20, 100, 10)
Ball = Player("bull.png", 350,250,50,50,9)
font1 = font.SysFont(None, 37)
lose1 = font1.render("Player 1, lose!",True, (120,120,120))
lose2 = font1.render("Player 2, lose!",True,(250,0,0))

finish = False
speed_x = 3
speed_y = 3
game = True
while game:
    window.fill(back)
    if finish != True:
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y
        rocket1.update_r()
        rocket2.update_l()

    for e in event.get():
        if e.type == QUIT:
            game = False
    if Ball.rect.y > 450 or Ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(rocket1, Ball) or sprite.collide_rect(rocket2, Ball):
        speed_x *= -1
    if Ball.rect.x < 0:
        finish = True
        window.blit(lose1,(300,250))
    if Ball.rect.x >= 700:
        finish = True
        window.blit(lose2,(300,250))
    rocket1.reset()
    rocket2.reset()
    Ball.reset()




    display.update()
    Clock.tick(60)
