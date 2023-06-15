import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)
PINK = (255, 20, 147)
Color_black=(160,82,45)
Clor_white=(238,232,170)
brown=(122,88,0)
pygame.init()
mw=pygame.display.set_mode((500,500))
clock=pygame.time.Clock()
mw.fill(LIGHT_BLUE)

events=pygame.event.get()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = LIGHT_BLUE
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))     

class Picture(Area):
    def __init__(self,file_name,x=0,y=0,width=10,height=10,color=None):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=color)
        self.image = pygame.image.load(file_name)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
x=60
y=30
block=[]
da=0
while da != 8:   
    for i in range(4):
        bw=Area(x,y,50,50,Clor_white)
        block.append(bw)
        x=x+50
        bb=Area(x,y,50,50,Color_black)
        block.append(bb)
        x=x+50
    y=y+50
    x=60
    da=da+1
    for i in range(4):
        bw=Area(x,y,50,50,Color_black)
        block.append(bw)
        x=x+50
        bb=Area(x,y,50,50,Clor_white)
        block.append(bb)
        x=x+50
    y=y+50
    x=60
    da=da+1
volody = input("""    0 стандартна гра 
1 задачі""")
if volody == "0":


    count=8
    start_x=53
    start_y=74
    x= start_x
    y= start_y
    pishak_black=[]


    for i in range(count):
        pb=Picture("Chess_pdt60.png",x,y,50,50)
        pishak_black.append(pb)
        x= x + 50
    start_w_x=53
    start_w_y=325
    pishak_white=[]
    x= start_w_x
    y= start_w_y
    for i in range(count):
        pw=Picture("pw60.png",x,y,50,50)
        pishak_white.append(pw)
        x=x+50
    tu_b=[]
    x=53
    y=24
    for i in range(2):
        t_b=Picture("tu_b60.png",x,y,50,50)
        tu_b.append(t_b)
        x=x+350
    tu_w=[]
    x=53
    y=375
    for i in range(2):
        t_w=Picture("tu_w60.png",x,y,50,50)
        tu_w.append(t_w)
        x=x+350
    sl_b=[]
    x=153
    y=24
    for i in range(2):
        s_b=Picture("sl_b60.png",x,y,50,50)
        sl_b.append(s_b)
        x=x+150
    sl_w=[]
    x=153
    y=375
    for i in range(2):
        s_w=Picture("sl_w60.png",x,y,50,50)
        sl_w.append(s_w)
        x=x+150
    ko_b=[]
    x=103
    y=24
    for i in range(2):
        k_b=Picture("ko_b60.png",x,y,50,50)
        ko_b.append(k_b)
        x=x+250
    ko_w=[]
    x=103
    y=375
    for i in range(2):
        k_w=Picture("ko_w60.png",x,y,50,50)
        ko_w.append(k_w)
        x=x+250
    f_b=Picture("fe_b60.png",205,24,50,50)
    f_w=Picture("fe_w60.png",205,375,50,50)
    f_bl=[]
    f_wl=[]
    f_bl.append(f_b)
    f_wl.append(f_w)

    k_b=Picture("ki_b60.png",255,24,50,50)
    k_w=Picture("ki_w60.png",255,375,50,50)

    k_bl=[]
    k_wl=[]
    k_bl.append(k_b)
    k_wl.append(k_w)

    temp_x=0
    temp_y=0
    drag=False
    drag_t=0

    king_b_live=True
    king_w_live=True

    all_fig=pishak_black+pishak_white+tu_b+tu_w+ko_b+ko_w+sl_b+sl_w+f_wl+f_bl+k_bl+k_wl
    fig_b=pishak_black+tu_b+ko_b+sl_b+f_bl+k_bl
    fig_w=pishak_white+tu_w+ko_w+sl_w+f_wl+k_wl

    while True:
        events=pygame.event.get()
        mw.fill(LIGHT_BLUE)
        for i in block:
            i.fill()
        for i in fig_b:
            i.draw()
        for i in fig_w:
            i.draw()





        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                temp_x=x
                temp_y=y
                for i in fig_b:
                    if i.collidepoint(x, y):
                        drag= True
                        drag_t=i
                        coll_fig=1

                for i in fig_w:
                    if i.collidepoint(x, y):
                        drag= True
                        drag_t=i
                        coll_fig=2


            elif drag_t != 0 :    
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: 
                        drag = False
            if drag == True:    
                for event in events:
                    if event.type == pygame.MOUSEMOTION  :  
                        mouse_x,mouse_y = event.pos
                        drag_t.rect.x=mouse_x - 30
                        drag_t.rect.y=mouse_y - 30



        if drag_t != 0:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y=event.pos
                    if coll_fig==1:
                        for i in fig_w:
                            if i.collidepoint(x,y):
                                fig_w.remove(i)
                    if coll_fig==2:
                        for i in fig_b:
                            if i.collidepoint(x,y):
                                fig_b.remove(i)
                    if event.button == 1:    
                        if drag == False:
                            for i in block:
                                if i.collidepoint(x,y):
                                    drag_t.rect.x=i.rect.x-7
                                    drag_t.rect.y=i.rect.y-5
                                    drag_t=0



        pygame.display.update()
        clock.tick(60)
    pygame.display.update()

if volody == "1":
    drag_t=0
    tu_w=[]
    count=3
    start_x=303
    start_y=74
    x= start_x
    y= start_y
    pishak_black=[]

    for i in range(count):
        pb=Picture("Chess_pdt60.png",x,y,50,50)
        pishak_black.append(pb)
        x= x + 50

    x=103
    y=374

    t_w=Picture("tu_w60.png",x,y,50,50)
    tu_w.append(t_w)


    k_b=Picture("ki_b60.png",355,24,50,50)
    k_w=Picture("ki_w60.png",355,174,50,50)

    k_bl=[]
    k_wl=[]
    k_bl.append(k_b)
    k_wl.append(k_w)
    all_fig=k_wl + tu_w
    drag=0
    while True:
        events=pygame.event.get()
        mw.fill(LIGHT_BLUE)
        for i in block:
            i.fill()
        for i in pishak_black:
            i.draw()
        for i in tu_w:
            i.draw()
        for i in k_bl:
            i.draw()
        for i in k_wl:
            i.draw()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                temp_x=x
                temp_y=y
                for i in all_fig:
                    if i.collidepoint(x, y):
                        drag= True
                        drag_t=i
            if drag_t != 0:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONUP:
                        x,y=event.pos
                        drag=False
                        if event.button == 1:    
                            if drag == False:
                                for i in block:
                                    if i.collidepoint(x,y):
                                        drag_t.rect.x=i.rect.x-7
                                        drag_t.rect.y=i.rect.y-5
                                        drag_t=0

            if drag == True:    
                for event in events:
                    if event.type == pygame.MOUSEMOTION  :  
                        mouse_x,mouse_y = event.pos
                        drag_t.rect.x=mouse_x - 30
                        drag_t.rect.y=mouse_y - 30
        pygame.display.update()
        clock.tick(60)
    pygame.display.update()
    
