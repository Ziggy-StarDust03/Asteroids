import pygame
from math import sqrt,sin,cos,floor,degrees,radians,ceil,asin,acos
from time import sleep
from random import randint
game = False
frame=0
parts=[]
def sincos(x1,y1,x2,y2):
    sinn=x2-x1
    coss=y2-y1
    hyp=sqrt((x1-x2)**2+(y1-y2)**2)
    if degrees(asin(coss/hyp))<0:
        b=180-degrees(acos(sinn/hyp))
        return degrees(acos(sinn/hyp))+(b*2)
    else:
        return degrees(acos(sinn/hyp))
def hiscore():
    pygame.draw.rect(dis,(0,0,0),[0,0,1300,650])
    j=pygame.font.Font('Vectorb.ttf',40).render('Highscores',True,(210,210,210))
    dis.blit(j,[530,50])
    pygame.display.update()
    sleep(1)
    global frame
    global score
    global asts
    with open('hiscores.txt','r') as f:
        lst=[]
        j=f.readline()
        split=j.split(';')
        for i in range(len(split)):
            lst.append(split[i].split(':'))
    index=-1
    if score>int(lst[-2][1]):
        index=0
        while True:
            if score>int(lst[index][1]):
                break
            index+=1
        lst.insert(index,[lst[-1][0],str(score)])
        lst.pop(-1)
    while True:
        frame+=1
        pygame.draw.rect(dis,(0,0,0),[0,0,1300,650])
        sleep(0.5)
        j=pygame.font.Font('Vectorb.ttf',40).render('Highscores',True,(210,210,210))
        dis.blit(j,[530,50])
        for i in range(5):
            if i==index:
                if frame%2==1:
                    j=pygame.font.Font('Vectorb.ttf',20).render(f'{lst[i][0]}:{lst[i][1]}',True,(210,210,210))
                    dis.blit(j,[480,(i*55)+170])
            else:
                j=pygame.font.Font('Vectorb.ttf',20).render(f'{lst[i][0]}:{lst[i][1]}',True,(210,210,210))
                dis.blit(j,[480,(i*55)+170])
        for i in range(5,10,1):
            if i==index:
                if frame%2==1:
                    j=pygame.font.Font('Vectorb.ttf',20).render(f'{lst[i][0]}:{lst[i][1]}',True,(210,210,210))
                    dis.blit(j,[750,((i-5)*55)+170])
            else:
                j=pygame.font.Font('Vectorb.ttf',20).render(f'{lst[i][0]}:{lst[i][1]}',True,(210,210,210))
                dis.blit(j,[750,((i-5)*55)+170])
        if frame%2==1:
            j=pygame.font.Font('Vectorb.ttf',25).render(f'You scored {score}',True,(210,210,210))
            dis.blit(j,[550,540])
        pygame.display.update()
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                with open('hiscores.txt','w') as f:
                    lstt=[]
                    for i in range(0,len(lst)-1,1):
                        lstt.append(':'.join([lst[i][0],lst[i][1]]))
                    f.write(';'.join(lstt)+';'+lst[-1][0])
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==49:
                    with open('hiscores.txt','w') as f:
                        lstt=[]
                        for i in range(0,len(lst)-1,1):
                            lstt.append(':'.join([lst[i][0],lst[i][1]]))
                        f.write(';'.join(lstt)+';'+lst[-1][0])
                        pygame.quit()
                elif i.key==32:
                    i=randint(1,2)
                    if i==1:
                        i=0
                    elif i==2:
                        i=650
                    with open('hiscores.txt','w') as f:
                        lstt=[]
                        for i in range(0,len(lst)-1,1):
                            lstt.append(':'.join([lst[i][0],lst[i][1]]))
                        f.write(';'.join(lstt)+';'+lst[-1][0])
                    asts=[Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False)]
                    return 0
                else:
                    continue
def particles(x,y,amount):
    for i in range(randint(amount*5,amount*8)):
        parts.append([x+randint(-2,2),y+randint(-2,2),randint(-10,10),randint(-10,10),0])
def incrs(aa,bb,cc):
    try:
        ee=cc/aa
        return [bb[0]*ee,bb[1]*ee]
    except ZeroDivisionError:
        if bb==[0,0]:
            return [0,0]
def av(aa, bb, cc):#sped,rot,movdir
    ee=[aa*cos(radians(bb)),aa*sin(radians(bb))]
    ee=[(((((ee[0]+cc[0])/2)+cc[0])/2)+cc[0])/2,(((((ee[1]+cc[1])/2)+cc[1])/2)+cc[1])/2]
    return ee
def distance(x1, y1, x2, y2):
    return sqrt(abs(x1-x2)**2+abs(y1-y2)**2)
class Shut():
    def __init__(self, x, y, dire):
        self.x = x
        self.y = y
        self.dire = dire
        self.age = 0
        self.sped=20
    def move(self):
        self.x += self.sped*cos(radians(self.dire))
        self.y += self.sped*sin(radians(self.dire))
class Sauce():
    def __init__(self, x,y,dire,typ):
        self.x=x
        self.y=y
        self.dire=dire
        self.typ=typ
        self.shutz=[]
    def move(self):
        self.x+=cos(radians(self.dire))*7
        self.y+=sin(radians(self.dire))*7
    def crash(self,j):
        global score,saucer,players
        if j!=-1:
            players[0].shutz.pop(j)
        particles(self.x,self.y,2)
        if self.typ==False:
            score+=200
        elif self.typ==True:
            score+=500
        saucer=0
    def shut(self,movdir):
        self.shutz.append(Shut(self.x,self.y,movdir))
class Obj():
    def __init__(self, x, y, rot, movdir, typ):
        if typ==False and movdir==[0,0]:
            while movdir==[0,0]:
                movdir=[randint(-2,2),randint(-2,2)]
        self.movdir = movdir
        self.x = x
        self.y = y
        self.rot = rot
        self.typ = typ
        if self.typ == True:
            self.shutz = []
            self.shown=True
            self.sped=0
        elif self.typ == False:
            self.size = 3
            self.shap = randint(1,6)
            if self.shap == 1:
                self.shap = 'Ë'
            elif self.shap == 2:
                self.shap = 'Ê'
            elif self.shap == 3:
                self.shap = 'Ì'
            elif self.shap == 4:
                self.shap = 'Í'
            elif self.shap == 5:
                self.shap = 'Î'
            elif self.shap == 6:
                self.shap = 'Ï'
    def crash(self,i,j):
        global score,level,lives
        players[0].shutz.pop(j)
        if asts[i].size > 1:
            asts.append(Obj(asts[i].x+randint(-20,20),asts[i].y+randint(-20,20),1,[(asts[i].movdir[randint(0,1)]+randint(-2,2))*1.2,(asts[i].movdir[randint(0,1)]+randint(-2,2))*1.2],False))
            asts[-1].size = asts[i].size-1
            asts.append(Obj(asts[i].x+randint(-20,20),asts[i].y+randint(-20,20),1,[(asts[i].movdir[randint(0,1)]+randint(-2,2))*1.2,(asts[i].movdir[randint(0,1)]+randint(-2,2))*1.2],False))
            asts[-1].size = asts[i].size-1
        particles(asts[i].x,asts[i].y,asts[i].size)
        if asts[i].size==3:
            score+=20
        elif asts[i].size==2:
            score+=50
        elif asts[i].size==1:
            score+=100
        if level%20>floor((score+1)/500)%20:
            lives+=1
        asts.pop(i)
    def rotat(self, ye):
        if ye == True:
            self.rot += 15
        elif ye == False:
            self.rot -= 15
        if self.rot > 360:
            self.rot = 0
        if self.rot < 0:
            self.rot = 360
    def shut(self):
        self.shutz.append(False)
        self.shutz[len(self.shutz)-1] = Shut(self.x,self.y,self.rot)
    def move(self):
        self.x += self.movdir[0]
        self.y += self.movdir[1]
pygame.init()
dis = pygame.display.set_mode((1300, 650))
pygame.display.set_caption('Asteroids')
players = []
players.append(False)
players[len(players)-1] = Obj(650, 325, 0, [0,0], True)
thrust = False
level = 1
a = False
d = False
i=randint(1,2)
if i==1:
    i=0
elif i==2:
    i=650
asts=[Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False)]
while True:
    frame+=1
    for i in asts:
        if i.x+15 > 1300:
            i.x = 1
        elif i.x+15 < -10:
            i.x = 1280
        if i.y+15 > 660:
            i.y = -9
        elif i.y+15 < -10:
            i.y = 640
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            game=True
            if i.key==49:
                pygame.quit()
    sleep(0.05)
    pygame.draw.rect(dis,(0,0,0),[0,0,1300,650])
    for i in asts:
        i.move()
        j=pygame.font.Font('Vectorb.ttf',30*i.size).render(str(i.shap),False,(210,210,210))
        dis.blit(j,[i.x-(15*i.size),i.y-(22*i.size)])
    j=pygame.font.Font('Vectorb.ttf',50).render('ASTEROIDS',False,(210,210,210))
    dis.blit(j,[470,80])
    j=pygame.font.Font('Vectorb.ttf',15).render('©1979 Atari Inc',False,(210,210,210))
    dis.blit(j,[550,550])
    if frame%30>=15:
        j=pygame.font.Font('Vectorb.ttf',23).render('Press Any Key',False,(210,210,210))
        dis.blit(j,[525,450])
    pygame.display.update()
    if game==True:
        i=randint(1,2)
        if i==1:
            i=0
        elif i==2:
            i=650
        asts=[Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False)]
        asts=[Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False),Obj(randint(1,1300),i,0,[randint(-5,5),randint(-5,5)],False)]
        players = []
        players.append(Obj(650,325,0,[0,0],True))
        parts.clear()
        wait=-1
        ee=[0,0]
        frame,thrustg,score,j=0,0,0,0
        ded=False
        lives=3
        level=1
        a=False
        d=False
        thrust=False
        score=0
        saucer=0
    while game==True:
        if saucer==0 and randint(0,420)==0:
            j=randint(1,2)
            i=j
            if j==1:
                j=1
                i=0
            elif j==2:
                j=1299
                i=180
            saucer=Sauce(j,randint(0,650),i,False)
        if saucer!=0:
            saucer.move()
            for i in range(len(saucer.shutz)):
                saucer.shutz[i].move()
                saucer.shutz[i].age+=1
                if saucer.shutz[i].age>=60:
                    saucer.shutz.pop(i)
                    break
            if saucer.x<0 or saucer.x>1300:
                saucer=0
            if frame%100==0 and players[0].shown==True:
                saucer.shut(sincos(saucer.x,saucer.y,players[0].x,players[0].y)+randint(-20,20))  #direction
        if ded==True:
            players[0].x=2000
        for i in range(len(parts)):
            try:
                parts[i][0]+=parts[i][2]
                parts[i][1]+=parts[i][3]
                parts[i][4]+=1
                if parts[i][4]>7:
                    parts.pop(i)
            except IndexError:
                break
        ee = 0
        pygame.draw.rect(dis, (0, 0, 0), [0, 0, 1300, 650])
        sleep(0.05)
        frame+=1
        if frame==wait:
            players[0].x=650
            players[0].y=325
            players[0].movdir=[0,0]
            players[0].shutz.clear()
            ded=False
        if frame==wait+40:
            players[0].shown=True
        level=floor((score+1)/500)
        if frame%3==0:
            if thrustg==0:
                thrustg=3
            elif thrustg==3:
                thrustg=0
        try:
            if len(asts)<=level and level>=1:
                if randint(1,75-((level+1)*6))==1:
                    i=randint(1,2)
                    if i==0:
                        i=0
                    elif i==1:
                        i=650
                    asts.append(Obj(randint(1,1300),i,0,[randint(-5,5)*ceil(level/100),randint(-5,5)*ceil(level/100)],False))
            else:
                if randint(1,1400-(level*16))==1:
                    i=randint(1,2)
                    if i==0:
                        i=0
                    elif i==1:
                        i=650
                    asts.append(Obj(randint(1,1300),i,0,[randint(-5,5)*ceil(level/100),randint(-5,5)*ceil(level/100)],False))
        except ValueError:
            if randint(1,30)==1:
                i=randint(1,2)
                if i==0:
                    i=0
                elif i==1:
                    i=650
                asts.append(Obj(randint(1,1300),i,0,[randint(-5,5)*ceil(level/100),randint(-5,5)*ceil(level/100)],False))

        for i in range(len(players)):
            if players[i].x > 1300:
                players[i].x = 5
            elif players[i].x < 0:
                players[i].x = 1295
            if players[i].y > 650:
                players[i].y = 5
            elif players[i].y < 0:
                players[i].y = 645
        for i in players[0].shutz:
            if i.x > 1300:
                i.x = 5
            elif i.x < 0:
                i.x = 1295
            if i.y > 650:
                i.y = 5
            elif i.y < 0:
                i.y = 645
        for i in asts:
            if i.x+15 > 1300:
                i.x = 1
            elif i.x+15 < -10:
                i.x = 1280
            if i.y+15 > 660:
                i.y = -9
            elif i.y+15 < -10:
                i.y = 640
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 97:
                    a = True
                elif event.key == 100:
                    d = True
                elif event.key == 106:
                    thrust = True
                elif event.key == 107:
                    if players[0].shown==True:
                        players[0].shut()
                elif event.key == 49:
                    pygame.quit()
            elif event.type == pygame.KEYUP:
                if event.key == 106:
                    thrust = False
                elif event.key == 97:
                    a = False
                elif event.key == 100:
                    d = False
        if a == True:
            players[0].rotat(False)
        if d == True:
            players[0].rotat(True)
        if thrust==True:
            players[0].movdir = av(players[0].sped,players[0].rot,players[0].movdir)
            players[0].sped=sqrt(players[0].movdir[0]**2+players[0].movdir[1]**2)*2
        elif thrust==False:
            players[0].movdir=incrs(players[0].sped,players[0].movdir,players[0].sped-0.3)
        if thrust == True:
            players[0].sped += 2
        if thrust == False:
            players[0].sped -= 0.2
        if players[0].sped > 20:
            players[0].sped = 20
        elif players[0].sped < 0:
            players[0].sped = 0
        if players[0].sped == 0:
            players[0].movdir = [players[0].sped*cos(radians(players[0].rot)),players[0].sped*sin(radians(players[0].rot))]
        players[0].move()
        ee=False
        if saucer!=0:
            if distance(saucer.x,saucer.y,players[0].x,players[0].y)<45:
                if players[0].shown:
                    saucer.crash(-1)
                    players[0].movdir=[0,0]
                    players[0].sped=0
                    players[0].shown=False
                    lives=lives-1
                    ded=True
                    if lives<=0:
                        hiscore()
                        game=False
                    elif lives>0:
                        wait=frame+40
                    particles(players[0].x,players[0].y,3)
        for i in range(len(asts)):
            try:
                if saucer!=0:
                    for ee in range(len(saucer.shutz)):
                        if distance(saucer.shutz[ee].x,saucer.shutz[ee].y,players[0].x,players[0].y)<30:
                            if players[0].shown==True:
                                players[0].movdir=[0,0]
                                players[0].sped=0
                                players[0].shown=False
                                lives=lives-1
                                ded=True
                                if lives<=0:
                                    hiscore()
                                    game=False
                                elif lives>0:
                                    wait=frame+40
                                particles(players[0].x,players[0].y,3)
                if distance(asts[i].x,asts[i].y,players[0].x,players[0].y) < asts[i].size*15:
                    if players[0].shown==True:
                        players[0].movdir=[0,0]
                        players[0].sped=0
                        players[0].shown=False
                        lives=lives-1
                        ded=True
                        if lives<=0:
                            hiscore()
                            game=False
                        elif lives>0:
                            wait=frame+40
                        particles(players[0].x,players[0].y,3)
            except IndexError:
                break
            for j in range(len(players[0].shutz)):
                    try:
                        if saucer!=0:
                            if distance(saucer.x,saucer.y,players[0].shutz[j].x,players[0].shutz[j].y)<20:
                                saucer.crash(j)
                        if distance(asts[i].x,asts[i].y,players[0].shutz[j].x,players[0].shutz[j].y) < asts[i].size*15:
                            asts[i].crash(i,j)
                    except IndexError:
                        break
        for i in asts:
            i.move()
        for i in parts:
            pygame.draw.rect(dis,(210,210,210),[i[0],i[1],1,1])
        for i in asts:
            j=pygame.font.Font('Vectorb.ttf',30*i.size).render(str(i.shap),True,(210,210,210))
            dis.blit(j,[i.x-(15*i.size),i.y-(22*i.size)])
        if ded==False:
            if players[0].shown==False:
                if frame%6<3:
                    pygame.draw.lines(dis,(210,210,210),False,[(players[0].x+(8*cos(radians(players[0].rot-140))),players[0].y+(8*sin(radians(players[0].rot-140)))),((players[0].x+(10*cos(radians(players[0].rot)))),(players[0].y+(10*sin(radians(players[0].rot))))),((players[0].x+(8*cos(radians(players[0].rot+140)))),(players[0].y+(8*sin(radians(players[0].rot+140)))))])   
                    pygame.draw.line(dis,(210,210,210),[players[0].x+(6*cos(radians(players[0].rot-140))),players[0].y+(6*sin(radians(players[0].rot-140)))],[players[0].x+(6*cos(radians(players[0].rot+140))),players[0].y+(6*sin(radians(players[0].rot+140)))])
                    if thrust == True:
                        pygame.draw.lines(dis,(210,210,210),True,((players[0].x+(6*cos(radians(players[0].rot-140))),players[0].y+(6*sin(radians(players[0].rot-140)))),(players[0].x+(6*cos(radians(players[0].rot+140))),players[0].y+(6*sin(radians(players[0].rot+140)))),(players[0].x+((9+thrustg)*cos(radians(players[0].rot+180))),players[0].y+((9+thrustg)*sin(radians(players[0].rot+180))))))
            else:
                pygame.draw.lines(dis,(210,210,210),False,[(players[0].x+(8*cos(radians(players[0].rot-140))),players[0].y+(8*sin(radians(players[0].rot-140)))),((players[0].x+(10*cos(radians(players[0].rot)))),(players[0].y+(10*sin(radians(players[0].rot))))),((players[0].x+(8*cos(radians(players[0].rot+140)))),(players[0].y+(8*sin(radians(players[0].rot+140)))))])   
                pygame.draw.line(dis,(210,210,210),[players[0].x+(6*cos(radians(players[0].rot-140))),players[0].y+(6*sin(radians(players[0].rot-140)))],[players[0].x+(6*cos(radians(players[0].rot+140))),players[0].y+(6*sin(radians(players[0].rot+140)))])
                if thrust == True:
                    pygame.draw.lines(dis,(210,210,210),True,((players[0].x+(6*cos(radians(players[0].rot-140))),players[0].y+(6*sin(radians(players[0].rot-140)))),(players[0].x+(6*cos(radians(players[0].rot+140))),players[0].y+(6*sin(radians(players[0].rot+140)))),(players[0].x+((9+thrustg)*cos(radians(players[0].rot+180))),players[0].y+((9+thrustg)*sin(radians(players[0].rot+180))))))
        for i in range(len(players[0].shutz)):
            players[0].shutz[i].move()
            players[0].shutz[i].age += 1
            if players[0].shutz[i].age > 35:
                del players[0].shutz[i]
                break
        for i in players[0].shutz:
            pygame.draw.rect(dis,(210,210,210),[i.x,i.y,2,2])
        i=pygame.font.Font('Vectorb.ttf',25).render(str(score),True,(210,210,210))
        dis.blit(i,[20,20])
        if saucer!=0:
            i=pygame.font.Font('Vectorb.ttf',50).render('Ç',True,(210,210,210))
            dis.blit(i,[saucer.x-25,saucer.y-50])
            for i in saucer.shutz:
                pygame.draw.rect(dis,(210,210,210),[i.x,i.y,2,2])
        for i in range(lives):
            pygame.draw.lines(dis,(210,210,210),False,[(14*((i+1)+1)+(8*cos(radians(270-140))),80+(8*sin(radians(270-140)))),(14*((i+1)+1)+(10*cos(radians(270))),80+(10*sin(radians(270)))),(((14*((i+1)+1))+(8*cos(radians(270+140)))),(80+(8*sin(radians(270+140)))))])
            pygame.draw.line(dis,(210,210,210),[(14*((i+1)+1))+(6*cos(radians(270-140))),80+(6*sin(radians(270-140)))],[(14*((i+1)+1))+(6*cos(radians(270+140))),80+(6*sin(radians(270+140)))])
        pygame.display.update()