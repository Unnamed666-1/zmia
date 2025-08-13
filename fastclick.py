import pygame
import time
from random import randint
pygame.init()

fon=(135,206,235)
window=pygame.display.set_mode((500,500))
window.fill(fon)
clock=pygame.time.Clock()

class Area():
    def __init__(self,x=0,y=0,width=10,height=10,color=None):
        self.rect=pygame.Rect(x,y,width,height)
        self.fill_color=color
    def color(self,new_color):
        self.fill_color=new_color
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def outline(self,frame_color,thickness):
        pygame.draw.rect(window,frame_color,self.rect,thickness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Label(Area):
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.image=pygame.font.SysFont("Verdana",fsize).render(text,True,text_color)
    def draw(self,shift_x = 0,shift_y = 0):
        self.fill()
        window.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))

class Picture(Area):
    def __init__(self, fillename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color = None)
        self.image = pygame.image.load(fillename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
        
red = (139,0,0)
greenyellow = (173,255,47)
wheat = (255,215,0)
dark_red = (139,0,0)
sky_blue = (135,206,235)
lime_green = (50,205,50)
light_red = (255,71,76)
black = (0,0,0)
light_green =(144,238,144)

cards = []
num_cards = 4
x = 70

for i in range(num_cards):
    new_card = Label(x,190,85,120,wheat)
    new_card.outline(sky_blue,10)
    new_card.set_text("click.png",16)
    cards.append(new_card)
    x += 100

start_time = time.time()
cur_time = time.time()

time_text = Label(0, 0, 50, 50, fon)
time_text.set_text("Часики:", 40, lime_green)
time_text.draw(20, 20)

score_text = Label(380, 0, 50, 50, fon)
score_text.set_text("Очки:", 45, lime_green)
score_text.draw(20, 20)

timer = Label(50, 55, 50, 40, fon)
timer.set_text("0", 40, lime_green)
timer.draw(0, 0)

score = Label(430, 55, 50, 40, fon)
score.set_text("0", 40, lime_green)
score.draw(0, 0)
wait = 0
points = 0
while True:
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(wheat)
            if (i+1) == click:    
                cards[i].draw(10,40)
            else:
                cards[i].fill()
    else:
        wait -= 1        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if i + 1 == click:
                        cards[i].color(greenyellow)
                        points += 1
                    else:
                        cards[i].color(red)
                        points -= 2
                    cards[i].fill()
                    score.set_text(str(points), 40, black)
                    score.draw(0, 0)
    new_time = time.time()
    if new_time - start_time >= 30:
        win = Label(0,0,500,500,light_red)
        win.set_text("Часіки протікали. ",60,black)
        win.draw(20,150)
        break
    if int(new_time)-int(cur_time)==1:
        timer.set_text(str(int(new_time - start_time)),40,black)
        timer.draw(0,0)
        cur_time = new_time
    if points >= 10:
        win = Label(0,0,500,500,light_green)
        win.set_text("Я думав ти програєш!",50,black)
        win.draw(120,150)
        result_time = Label(90,230,250,250,light_green)
        result_time.set_text("Времячко: "+str(int(new_time-start_time))+" секунд!",30,black)
        result_time.draw(0,0)
        break
    pygame.display.update()
    clock.tick(30)
pygame.display.update()