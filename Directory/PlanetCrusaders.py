#IMPORTS
import threading
import math
import pygame
import random
from tkinter import*
##from PIL import Image


#BOOL
Start=False
mouv=False
done=False
tircontinue=False
pistol,machineg,shotg,rocketl=True,False,False,False
premier=False
spawning=True
scorebool=True
programall=True
testing=False
affichagevague=True
affichagefirst=True
vaguestart=False
introstat0 = True
introstat1 = True

#VAR
ai=0
var1=['varx','vary']
ammo=100
bgX,bgY=0,0
countir=0
damage=1
deplacement_x=1
deplacement_y=1
difficulte=1500
dist=400
framex,framey=0,0
grdinv=5
i=0
kills=0
lengthscore=0
lettres=0
maxim=0
nameofficial=''
nbrore=0
nbrvaisseau=10
noml=0
Ra=60
randoshit=0
temps=0
typearme=15
tps=0
v=0
vie=10
vitesseb=2 
vitessea=10
W,H = 1920,1080
vague=1
tempsfirst=0
prevaisseau=0
first=True

#LIST
nameofficialsplit=[]
scorel=[]
scorenom=[]
scorenum=[]
scoreordre=[]
matrice_inventaire=[]
#aucune utilisation de cv2 ralentissant le programme 
widthimages={'0':56,'1':13,'2':57,'3':56,'4':56,'5':56,'6':57,'7':56,'8':56,'9':56,'a':54,'b':68,'c':70,'d':47,'e':46,'f':45,'g':49,'h':48,'i':19,'j':39,'k':47,'l':41,'m':60,'n':47,'o':51,'p':49,'q':51,'r':50,'s':51,'t':48,'u':48,'v':56,'w':0,'x':55,'y':52,'z':47}
    
#règle les difficultées
#probleme de reduction du programme avec tkinter

def positif(a):
    return int((a**2)**0.5)

def negatif(a):
    if a>0:
        return -a

##################################################################################################################################################################################
#                                           DEFINITIONS AFFICHANT UN NOMBRE SUR L'ÉCRAN EN APPELANT "POINT"
##################################################################################################################################################################################

#Utilise un élément x (var[x]) de la liste self dans la def point et l'affiche
#affiche le nombre dependemment de la longueur du chiffre initiale (info)
def Point(x,y,info,typet,direction,taille,affichage):
    global matrice_inventaire
    points=str(info)
    self,widthstr=[],[]
    for lettre in points:
        if lettre!='-':
        #divise et transforme les chiffres de info en string dans la liste self
            self.append(lettre)
    if direction=='droite':
        slef=self.reverse()
    for i in range(len(self)):
        if self[i]==' ':
            widthstr.append(20)
        else:
            if affichage:
                image='Directory/Police/'+typet+'/'+str(taille)+'%'+'/'+self[i]+".png"
                scr = pygame.image.load(image).convert_alpha() 
            if direction=='gauche':
                if affichage:
                    screen.blit(scr, (x+int(sum(widthstr))+i*3,y))
                widthstr.append(widthimages[self[i]]*taille/100)
            if direction=='droite':
                widthstr.append(widthimages[self[i]]*taille/100)
                if affichage:
                    screen.blit(scr, (x-int(sum(widthstr))-i*3,y))
    if not affichage:
        return int(sum(widthstr))

##################################################################################################################################################################################

def StartFalse():
    global Start
    Start = False
    
def quitkillspersec():
    global done
    global pygame
    global fen
    global done
    StartFalse()
    fen.destroy()
    done=True
    pygame.quit()

def quit3(a):
    global done
    global pygame
    global fen
    global done
    StartFalse()
    fen.destroy()
    done=True
    pygame.quit()


def intro1():
    delete=False
    global tps
    global nameofficial
    global introstat1
    global done
    global introstat0
    first=True
    introstat1 = True
    startscreen1=pygame.image.load('Directory/intro2a.png').convert()
    startscreen2=pygame.image.load('Directory/intro2b.png').convert()
    startscreen3=pygame.image.load('Directory/intro3.png').convert()
    if len(scorenom)<=5:
        lengthscore=len(scorenom)
    else:
        lengthscore=5
    while introstat1:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        tps+=1
        stop=0
        if 748<mouse_x<1218 and 896<mouse_y<972 and nameofficial!='':
            screen.blit(startscreen1,(0,0))
        elif nameofficial!='':
            screen.blit(startscreen2,(0,0))
        else:
            screen.blit(startscreen3,(0,0))
        screen.blit(cursor,(mouse_x,mouse_y))
        for i in range(lengthscore):
            Point(715,i*25+520,str(scorenom[i]),'tech','gauche',50,True)
            Point(1190,i*25+520,str(scorenum[i]),'tech','droite',50,True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                introstat0 = False
                introstat1 = False
            elif event.type == pygame.MOUSEBUTTONDOWN and 748<mouse_x<1218 and 896<mouse_y<972 and nameofficial!='':
                introstat0 = False
                introstat1 = False
            elif event.type == pygame.KEYDOWN:
                if len(nameofficial)<15:
                    if event.key == pygame.K_a:
                        nameofficial+='a'
                    if event.key == pygame.K_b:
                        nameofficial+='b'
                    if event.key == pygame.K_c:
                        nameofficial+='c'
                    if event.key == pygame.K_d:
                        nameofficial+='d'
                    if event.key == pygame.K_e:
                        nameofficial+='e'
                    if event.key == pygame.K_f:
                        nameofficial+='f'
                    if event.key == pygame.K_g:
                        nameofficial+='g'
                    if event.key == pygame.K_h:
                        nameofficial+='h'
                    if event.key == pygame.K_i:
                        nameofficial+='i'
                    if event.key == pygame.K_j:
                        nameofficial+='j'
                    if event.key == pygame.K_k:
                        nameofficial+='k'
                    if event.key == pygame.K_l:
                        nameofficial+='l'
                    if event.key == pygame.K_m:
                        nameofficial+='m'
                    if event.key == pygame.K_n:
                        nameofficial+='n'
                    if event.key == pygame.K_o:
                        nameofficial+='o'
                    if event.key == pygame.K_p:
                        nameofficial+='p'
                    if event.key == pygame.K_q:
                        nameofficial+='q'
                    if event.key == pygame.K_r:
                        nameofficial+='r'
                    if event.key == pygame.K_s:
                        nameofficial+='s'
                    if event.key == pygame.K_t:
                        nameofficial+='t'
                    if event.key == pygame.K_u:
                        nameofficial+='u'
                    if event.key == pygame.K_v:
                        nameofficial+='v'
                    if event.key == pygame.K_w:
                        print(mouse_x,mouse_y)
                    if event.key == pygame.K_x:
                        nameofficial+='x'
                    if event.key == pygame.K_y:
                        nameofficial+='y'
                    if event.key == pygame.K_z:
                        nameofficial+='z'
                    if event.key == pygame.K_SPACE:
                        nameofficial+='  '
                    if event.key == pygame.K_1:
                        nameofficial+='1'
                    if event.key == pygame.K_2:
                        nameofficial+='2'
                    if event.key == pygame.K_3:
                        nameofficial+='3'
                    if event.key == pygame.K_4:
                        nameofficial+='4'
                    if event.key == pygame.K_5:
                        nameofficial+='5'
                    if event.key == pygame.K_6:
                        nameofficial+='6'
                    if event.key == pygame.K_7:
                        nameofficial+='7'
                    if event.key == pygame.K_8:
                        nameofficial+='8'
                    if event.key == pygame.K_9:
                        nameofficial+='9'
                    if event.key == pygame.K_0:
                        nameofficial+='0'
                if event.key == pygame.K_BACKSPACE:
                    delete=True
                    first = True
                if event.key == pygame.K_ESCAPE:
                    introstat1 = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    delete=False
        if first:
            nameofficial=nameofficial[:len(nameofficial)-1]
            first=False
            stop=tps
        elif delete and (tps-stop)%25==0:
            nameofficial=nameofficial[:len(nameofficial)-1]
         
        Point(500,100,nameofficial,'tech','gauche',100,True)
        pygame.display.update()
        pygame.display.flip()
    
def Intro():
    pygame.init()
    intro=pygame.mixer.music.play()
    global tps
    global introstat1
    global introstat0
    global done
    startscreen1=pygame.image.load('Directory/intro1.png').convert()
    startscreen2=pygame.image.load('Directory/intro0.png').convert()
    while introstat0:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        if 789<mouse_x<1124 and 685<mouse_y<808:
            screen.blit(startscreen1,(0,0))
        else:
            screen.blit(startscreen2,(0,0))
        screen.blit(cursor,(mouse_x,mouse_y))
        tps+=1
##        screen.blit(testx,(mouse_x,0))
##        screen.blit(testy,(0,mouse_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN and 789<mouse_x<1124 and 685<mouse_y<808:
                intro1()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print(mouse_x,mouse_y)
                elif event.key == pygame.K_ESCAPE:
                    programall=False
                    introstat0 = False
                    introstat1 = False
                    done=True
                    pygame.quit()
                    return

        pygame.display.update()
        pygame.display.flip()
        intro=pygame.mixer.music.stop()


#Met en place le menu

class TpsDiff(pygame.sprite.Sprite):
    def __init__(self,maxi):
        super().__init__()
        self.count=0
        self.maximum=maxi
        self.answer=False
    def advance(self):
        self.count+=1
        if self.count>self.maximum:
            self.answer=True
            self.count=0
        else:
            self.answer=False       

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.count=0
        self.x=x
        self.y=y
        self.timing=TpsDiff(1)
    def explode(self):
        self.timing.advance()
        if self.count==11:
            self.count=0
            explosion_sprites_list.remove(self)
        scr = pygame.image.load('Directory/Explosion/'+str(self.count)+'exp.png').convert_alpha()
        screen.blit(scr,(self.x,self.y))
        if self.timing.answer:
            self.count+=1

#Démare le tire d'une balle et gère la reduction de munitions
def tir(a):
    global ammo
    global bullet_sprites_list
    global bullet
    global all_sprites_list
    bullet = Bullet()
    if rocketl==True:
        bullet.image = pygame.image.load("Directory/tir.png").convert_alpha()
    else:
        bullet.image = pygame.image.load("Directory/tir1.png").convert_alpha()    
    bullet.rect.x = joueur.rect.x
    bullet.rect.y = joueur.rect.y
    bullet_sprites_list.add(bullet)
    ammo-=a

#Met en place un inventaire sous forme de matrice
def matrice():
    global matrice_inventaire
    global grdinv
    for x in range(grdinv):
        matrice_inventaire.append([])
        for y in range(grdinv):
            matrice_inventaire[x].append(0)

#Établit le mennu de fin montrant les kills/sec et le temps joué
def killspersec():
    global pygame
    if done==True:
        pygame.quit()
        while Start==True:
            global fen
            fen=Tk()
            ks0=Label(fen,text='Kills per Second :    ')
            ks0.grid(row=1,column=0)
            ks=Label(fen,text=round(kills/(temps/60),3),fg='red')
            ks.grid(row=1,column=1)
            ks1=Label(fen,text='hours:min:sec    :    ')
            ks1.grid(row=2,column=0)
            ks2=Label(fen,text=str(round(temps/216000,0))+':'+str(round(temps/3600,0))+':'+str(round(temps/60,1)),fg='red')
            ks2.grid(row=2,column=1)
            dg=Button(fen,text='Quit', command=quitkillspersec, height=1, width=5,font=('Courier New', '40'))
            dg.grid(row=3)
            fen.bind('<Escape>',quit3)
            fen.mainloop()
    
def Merge(a,b,collision):
    global v
    global enemy_sprites_list
    global enemys_sprites_list
    global enemya_sprites_list
    global enemyb_sprites_list
    global enemyc_sprites_list
    global all_sprites_list
    for enemy1 in a:
        collision = pygame.sprite.spritecollide(enemy1, a, False)
        for enemy2 in collision:
            if enemy1!=enemy2:
                x=(enemy1.rect.x+enemy2.rect.x)/2
                y=(enemy1.rect.y+enemy2.rect.y)/2
                if b==enemyb_sprites_list:
                    newenemy=EnemyB(x,y)
                elif b==enemya_sprites_list:
                    newenemy=EnemyA(x,y)
                elif b==enemys_sprites_list:
                    newenemy=EnemyS(x,y)
                enemy_sprites_list.add(newenemy)
                b.add(newenemy)
                all_sprites_list.add(newenemy)                    
                enemy_sprites_list.remove(enemy1)                    
                enemy_sprites_list.remove(enemy2)
                a.remove(enemy1)                    
                a.remove(enemy2)
                all_sprites_list.remove(enemy1)
                all_sprites_list.remove(enemy2)
                v-=1

def Arme(x,y):
    if rocketl:
        file='rocketl.png'
    elif pistol:
        file='pistolet.png'
    elif shotg:
        file='shotgun.png'
    elif machineg:
        file='mitraillette.png'
    arme=pygame.image.load('Directory/arme/'+file).convert_alpha()
    screen.blit(arme, (x,y))


##################################################################################################################################################################################
#                                           				GÈRE LES MOUVEMENTS
##################################################################################################################################################################################

#Permet de mettre les
def sinray(degre):
    return round(math.sin(math.radians(degre)),1)*Ra

def cosray(degre):
    return round(math.cos(math.radians(degre)),1)*Ra

#simule le déplacement du joueur
def mouv2(fichier,var,vitessemouv):
    #permet de simuler un mouvement...
    global framex
    global framey
    #...si le mouvement est sur x
    if var=='x' or var=='xy':
        if temps%vitessemouv==0:
            framex+=1
            if framex==4:
                framex=0
        if framex==0 or framex==2:
            joueur.image = pygame.image.load(fichier+'.png').convert_alpha()
        elif framex==1:
            joueur.image = pygame.image.load(fichier+"_p1.png").convert_alpha()
        elif framex==3:
            joueur.image = pygame.image.load(fichier+"_p2.png").convert_alpha()
    #...si le mouvement est sur y
    if var=='y' or var=='xy':
        if temps%vitessemouv==0:
            framey+=1
            if framey==4:
                framey=0
        if framey==0 or framey==2:
            joueur.image = pygame.image.load(fichier+".png").convert_alpha()
        elif framey==1:
            joueur.image = pygame.image.load(fichier+"_p1.png").convert_alpha()
        elif framey==3:
            joueur.image = pygame.image.load(fichier+"_p2.png").convert_alpha()


def mouvement(vitessemouv):
    directory='Directory/Joueur/'
    #detecte la presence de mouvement
    if w or s or d or a:
        mouv=True
    else:
        mouv=False
    #permet le changement d'images simulant un mouvement, utilisation des cosinus et sinus afin que le personnage fasse face au curseur
    deplacementx=positif(deplacement_x)
    deplacementy=positif(deplacement_y)

    #####determine le sens et direction du personnage en...

    #...detectant si la souris est a droite du personnage
    if cosray(22.5)<=deplacementx<=cosray(0) and sinray(0)<=deplacementy<=sinray(22.5) and mouse_x>joueur.rect.x:
        joueur.image = pygame.image.load(directory+"vaisseaud.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseaud','x',vitessemouv)

    #...detectant si la souris est en haut a droite du personnage
    elif cosray(67.5)<=deplacementx<=cosray(22.5) and sinray(22.5)<=deplacementy<=sinray(67.5) and mouse_x>joueur.rect.x and mouse_y<joueur.rect.y:
        joueur.image = pygame.image.load(directory+"vaisseauh.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseauh','xy',vitessemouv)

    #...detectant si la souris est en haut du personnage
    elif cosray(90)<=deplacementx<=cosray(67.5) and sinray(67.5)<=deplacementy<=sinray(90) and mouse_y<joueur.rect.y:
        joueur.image = pygame.image.load(directory+"vaisseauh.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseauh','y',vitessemouv)

    #...detectant si la souris est en haut a gauche du personnage
    elif cosray(67.5)<=deplacementx<=cosray(22.5) and sinray(22.5)<=deplacementy<=sinray(67.5) and mouse_x<joueur.rect.x and mouse_y<joueur.rect.y:
        joueur.image = pygame.image.load(directory+"vaisseauh.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseauh','xy',vitessemouv)

    #...detectant si la souris est a gauche du personnage
    elif cosray(22.5)<=deplacementx<=cosray(0) and sinray(0)<=deplacementy<=sinray(22.5) and mouse_x<joueur.rect.x:
        joueur.image = pygame.image.load(directory+"vaisseaug.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseaug','x',vitessemouv)

    #...detectant si la souris est en bas a droite du personnage
    elif cosray(67.5)<=deplacementx<=cosray(22.5) and sinray(22.5)<=deplacementy<=sinray(67.5) and mouse_x<joueur.rect.x and mouse_y>joueur.rect.y:
        joueur.image = pygame.image.load(directory+"vaisseaub.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseaub','xy',vitessemouv)

    #...detectant si la souris est en bas du personnage
    elif cosray(90)<=deplacementx<=cosray(67.5) and sinray(67.5)<=deplacementy<=sinray(90) and mouse_y>joueur.rect.y:
        joueur.image = pygame.image.load(directory+"vaisseaub.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseaub','y',vitessemouv)
    #...detectant si la souris est en bas a droite du personnage
    elif cosray(67.5)<=deplacementx<=cosray(22.5) and sinray(22.5)<=deplacementy<=sinray(67.5) and mouse_x>joueur.rect.x and mouse_y>joueur.rect.y:
        joueur.image = pygame.image.load(directory+"vaisseaub.png").convert_alpha()
        if mouv:
            mouv2(directory+'vaisseaub','xy',vitessemouv)

def deplacementsprite(liste):
    for sprite in liste:
        if joueur.rect.x==W-dist and bgX!=-W and d:
            sprite.rect.x-=vitessea
        if joueur.rect.x==dist and bgX!=0 and a:
            sprite.rect.x+=vitessea
        if joueur.rect.y==H-dist and bgY!=-H and s:
            sprite.rect.y-=vitessea
        if joueur.rect.y==dist and bgY!=0 and w:
            sprite.rect.y+=vitessea

def Vitesse(prim,multi,liste):
    prim*=multi
    for enemy in liste:
        if joueur.rect.x<enemy.rect.x:
            enemy.rect.x-=prim
        if enemy.rect.x<joueur.rect.x:
            enemy.rect.x+=prim
        if joueur.rect.y<enemy.rect.y-88:
            enemy.rect.y-=prim
        if enemy.rect.y-88<joueur.rect.y:
            enemy.rect.y+=prim
           
##################################################################################################################################################################################
#                                           			GÈRE L'INVENTAIRE
##################################################################################################################################################################################

def InvSpa(nbrsqr,distance):
    global matrice_inventaire
    Point(1100,140,'10 ressources pour une vie','tech','gauche',50,True)
    Point(1100,240,'r pour 10 ammo','tech','gauche',50,True)
    for x in range(1,nbrsqr+1):
        for y in range(1,nbrsqr+1):
            interspacex=x*distance+(x-1)*100
            interspacey=y*distance+(y-1)*100
            Point(int(interspacex)+15,int(interspacey)+15,matrice_inventaire[x-1][y-1],'tech','gauche',50,True)
            square=pygame.image.load("Directory/InvSpa.png").convert_alpha()
            if x==1 and y==1:
                inv=pygame.image.load("Directory/ore.png").convert_alpha()
                screen.blit(inv, (int(interspacex)+40,int(interspacey)+40))
            else:
                screen.blit(square, (int(interspacex),int(interspacey)))

def Inventaire(nbrsqr):
    global ammo
    global matrice_inventaire
    global all_sprites_list
    global screen
    global event
    global done
    global Start1
    global vie
    cotesqr=100
    inventaire=pygame.image.load("Directory/inventaire.jpg").convert_alpha()
    while Start1:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        screen.blit(inventaire, (0,0))
        screen.blit(cursor,(mouse_x,mouse_y))
        var=(H-(nbrsqr)*cotesqr)/(nbrsqr+1)
        InvSpa(nbrsqr,var)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Start1=False
                elif event.key == pygame.K_0:
                    Start1=False
                    done=True
            elif event.type == pygame.MOUSEBUTTONDOWN and 1100<mouse_x<1100+int(Point(1100,140,'10 r pour v','tech','gauche',50,False)) and 140<mouse_y<140+100 and matrice_inventaire[0][0]>=10:
                matrice_inventaire[0][0]-=10
                vie+=1
                Inventaire(nbrsqr)
            elif event.type == pygame.MOUSEBUTTONDOWN and 1100<mouse_x<1100+int(Point(1100,240,'r pour 10 ammo','tech','gauche',50,False)) and 240<mouse_y<340 and matrice_inventaire[0][0]>=1:
                matrice_inventaire[0][0]-=1
                ammo+=5
                Inventaire(nbrsqr)
        pygame.display.update()
        pygame.display.flip()
        
##################################################################################################################################################################################
#                                           				CRÉE LES SPRITES
##################################################################################################################################################################################

class Joueur(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/Joueur/vaisseauh.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = x
        self.rect.y = y
    def changespeedn(self,x,y):
        self.change_x+=x
        self.change_y+=y
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x>W-dist and bgX!=-W:
            self.rect.x=W-dist
        elif self.rect.x>W-90:
            self.rect.x=W-90

        if self.rect.x<dist and bgX!=0:
            self.rect.x=dist
        elif self.rect.x<0:
            self.rect.x=0

        if self.rect.y>H-dist and bgY!=-H:
            self.rect.y=H-dist
        elif self.rect.y>H-164:
            self.rect.y=H-164

        if self.rect.y<dist and bgY!=0:
            self.rect.y=dist
        elif self.rect.y<0:
            self.rect.y=0

class EnemyC(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/ennemi/c.png").convert_alpha()       
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.viemax=1
    def changespeeda(self,x,y):
        self.change_y+=y
        self.change_x+=x
    def update(self):
        self.rect.x += int(self.change_x)
        self.rect.y += int(self.change_y)

class EnemyB(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/ennemi/b.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.viemax=2
    def changespeeda(self,x,y):
        self.change_y+=y
        self.change_x+=x
    def update(self):
        self.rect.x += int(self.change_x)
        self.rect.y += int(self.change_y)

class EnemyA(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/ennemi/a.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.viemax=3
    def changespeeda(self,x,y):
        self.change_y+=y
        self.change_x+=x
    def update(self):
        self.rect.x += int(self.change_x)
        self.rect.y += int(self.change_y)

class EnemyS(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/ennemi/s.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.viemax=4
    def changespeeda(self,x,y):
        self.change_y+=y
        self.change_x+=x
    def update(self):
        self.rect.x += int(self.change_x)
        self.rect.y += int(self.change_y)
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Directory/tir1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x=int(deplacement_x)
        self.y=int(deplacement_y)
        if rocketl:
            self.type='rocketl'
        elif shotg:
            self.type='shotg'
        elif machineg:
            self.type='machineg'
        elif pistol:
            self.type='pistol'
    def update(self):
#mettre en float pour précision
        self.rect.x += self.x
        self.rect.y += self.y

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/tir.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = int(x)
        self.rect.y = int(y)
        
class Ore(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Directory/ore.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect.x = int(x)
        self.rect.y = int(y)

##################################################################################################################################################################################

def spawnore(maximum):
    global nbrore
    while nbrore!=maximum:
        ore=Ore(random.randint(bgX,2*W+bgX),random.randint(bgY,2*H+bgY))
        all_sprites_list.add(ore)
        ore_sprites_list.add(ore)
        nbrore+=1




while programall:
        #BOOL
    Start=False
    mouv=False
    done=False
    tircontinue=False
    pistol,machineg,shotg,rocketl=True,False,False,False
    premier=False
    spawning=True
    scorebool=True
    programall=True
    testing=False
    affichagevague=True
    affichagefirst=True
    vaguestart=False
    introstat0 = True
    introstat1 = True

    #VAR
    ai=0
    var1=['varx','vary']
    ammo=100
    bgX,bgY=0,0
    countir=0
    damage=1
    deplacement_x=1
    deplacement_y=1
    difficulte=1500
    dist=400
    framex,framey=0,0
    grdinv=5
    i=0
    kills=0
    lengthscore=0
    lettres=0
    maxim=0
    nameofficial=''
    nbrore=0
    nbrvaisseau=10
    noml=0
    Ra=60
    randoshit=0
    temps=0
    typearme=15
    tps=0
    v=0
    vie=10
    vitesseb=2 
    vitessea=10
    W,H = 1920,1080
    vague=1
    tempsfirst=0
    prevaisseau=0
    first=True

    #LIST
    nameofficialsplit=[]
    scorel=[]
    scorenom=[]
    scorenum=[]
    scoreordre=[]
    matrice_inventaire=[]
    #aucune utilisation de cv2 ralentissant le programme
    ScoreL=open('Directory/score.txt')
    for line in ScoreL:
        i+=1
        scorel.append(str(line))
        for lettre in line:
            line=line.replace('\n','')
            if lettre==':':
                scorenom.append(line[:lettres])
                scorenum.append(line[lettres+1:])
            lettres+=1
        lettres=0
    ScoreL.close()
    pygame.init()
    pygame.display.set_caption('Planet Crusaders')
    clock = pygame.time.Clock()
    event=pygame.event
    screen = pygame.display.set_mode([W, H],pygame.FULLSCREEN) 
    bg = pygame.image.load('Directory/bg.jpg').convert()
    excla=pygame.image.load('Directory/excla.png').convert_alpha()
    testx=pygame.image.load('Directory/x.png').convert_alpha()
    testy=pygame.image.load('Directory/y.png').convert_alpha()
    crosshair=pygame.image.load('Directory/crosshair.png').convert_alpha()
    cursor=pygame.image.load('Directory/cursor.png').convert_alpha()

    intro=pygame.mixer.music.load('Directory/intro.mp3')

    vagues=TpsDiff(difficulte)
    affichagevagues=TpsDiff(150)
    
    joueur = Joueur(960,540)

    #Crée les groupes de sprites
    all_sprites_list=pygame.sprite.Group()
    ally_sprites_list = pygame.sprite.Group()
    enemy_sprites_list = pygame.sprite.Group()
    enemyc_sprites_list = pygame.sprite.Group()
    enemyb_sprites_list = pygame.sprite.Group()
    enemya_sprites_list = pygame.sprite.Group()
    enemys_sprites_list = pygame.sprite.Group()
    bullet_sprites_list = pygame.sprite.Group()
    drop_sprites_list = pygame.sprite.Group()
    enemy_hit_list = pygame.sprite.Group()
    
    enemyc_collide_list = pygame.sprite.Group()
    enemyb_collide_list = pygame.sprite.Group()
    enemya_collide_list = pygame.sprite.Group()
    ore_sprites_list = pygame.sprite.Group()
    explosion_sprites_list= pygame.sprite.Group()

    #ajoute les spries dans ces listes
    ally_sprites_list.add(joueur)
    all_sprites_list.add(joueur)
    score = 0
    matrice()

    if testing:
        matrice_inventaire[0][0]=100

    w,a,s,d=False,False,False,False
    #Débute la boucle principale du programme
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    
    Intro()
    if done:
        break

    game=pygame.mixer.music.load('Directory/game.mp3')

    game=pygame.mixer.music.play()
    while not done:
        screen.blit(bg,(int(bgX),int(bgY)))
        #permet calculer grâcce au Théorème de Thalès la différence en abscisse et en ordonnée par rapport à un rayon réduit entre la souris et le
        #vaisseau principale
        mouse_x,mouse_y=pygame.mouse.get_pos()
        screen.blit(crosshair,(mouse_x-36,mouse_y-36))
        Point(mouse_x+60,mouse_y+36,str(positif(ammo)),'tech','droite',100,True)

        distance_souris_sprite_x=mouse_x-joueur.rect.x
        distance_souris_sprite_y=mouse_y-joueur.rect.y
        distance_souris_sprite=(distance_souris_sprite_x**2+distance_souris_sprite_y**2)**0.5
        if distance_souris_sprite!=0:
            deplacement_x=(Ra*distance_souris_sprite_x)/distance_souris_sprite
            deplacement_y=(Ra*distance_souris_sprite_y)/distance_souris_sprite
        mouvement(8)
        spawnore(10)
        
    ##    if temps%50==0:
    ##        print("bgX = ",bgX,"      bgY = ",bgY)
    ##        print("Joueur x = ",joueur.rect.x,"Joueur y = ",joueur.rect.y)

        if vagues.answer:
            affichagevagues.advance()
            if not affichagevagues.answer:
                Point(1000,400,vague,'tech','gauche',500,True)
            else:
                for l in range(nbrvaisseau):     
                    if var1[random.randint(0,1)]=='varx':
                        varx=[bgX,bgX+2*W]
                        vartotaley=[bgY,bgY+random.randint(0,2*H)]
                        enemyc = EnemyC(varx[random.randint(0,1)],vartotaley[random.randint(0,1)])
                    else:
                        vartotalex=[bgX,bgX+random.randint(0,2*W)]
                        vary=[bgY,bgY+2*H]
                        enemyc = EnemyC(vartotalex[random.randint(0,1)],vary[random.randint(0,1)])                
                    enemyc_sprites_list.add(enemyc)
                    enemy_sprites_list.add(enemyc)
                    all_sprites_list.add(enemyc)
                    v+=1
                vagues.advance()
                nbrvaisseau+=5
                difficulte*=0.95
                vague+=1
                vagues=TpsDiff(difficulte)
        else:
            vagues.advance()
                
        #met en place la vitesse pour les vaisseaux ennemis
        Vitesse(2,1,enemyc_sprites_list)
        Vitesse(2,2,enemyb_sprites_list)
        Vitesse(2,3,enemya_sprites_list)
        Vitesse(2,4,enemys_sprites_list)
        
    #Gère l'interaction entre le joueur et le programe par l'intermédiaire du clavier
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #change la vitesse par rapport aux touches w,a,s,d
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    joueur.changespeedn(-vitessea, 0)
                    a=True
                elif event.key == pygame.K_d:
                    joueur.changespeedn(vitessea, 0)
                    d=True
                elif event.key == pygame.K_w:
                    joueur.changespeedn(0, -vitessea)
                    w=True
                elif event.key == pygame.K_s:
                    joueur.changespeedn(0, vitessea)
                    s=True
                elif event.key == pygame.K_e:
                    Start1=True
                    if a==True:
                        joueur.changespeedn(vitessea, 0)
                        a=False
                    if w==True:
                        joueur.changespeedn(0, vitessea)
                        w=False
                    if s==True:
                        joueur.changespeedn(0,-vitessea)
                        s=False
                    if d==True:
                        joueur.changespeedn(-vitessea, 0)
                        d=False
                    Inventaire(grdinv)
                    
                elif event.key == pygame.K_ESCAPE:
                    done=True

                elif event.key == pygame.K_4:
                    #Lance Roquette
                    pistol,machineg,shotg,rocketl=False,False,False,True
                elif event.key == pygame.K_3:
                    #Shot-Gun
                    pistol,machineg,shotg,rocketl=False,False,True,False
                elif event.key == pygame.K_2:
                    #Mitraillette
                    pistol,machineg,shotg,rocketl=False,True,False,False
                elif event.key == pygame.K_1:
                    #Pistolet
                    pistol,machineg,shotg,rocketl=True,False,False,False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    joueur.changespeedn(vitessea, 0)
                    a=False
                elif event.key == pygame.K_d:
                    joueur.changespeedn(-vitessea, 0)
                    d=False
                elif event.key == pygame.K_w:
                    joueur.changespeedn(0, vitessea)
                    w=False
                elif event.key == pygame.K_s:
                    joueur.changespeedn(0,-vitessea)
                    s=False

            #active le tir du joueur
            elif event.type == pygame.MOUSEBUTTONDOWN:
                tircontinue=True
            elif event.type == pygame.MOUSEBUTTONUP:
                tircontinue=False
                countir=0

    #Permet un tir continue limitée par 'bullet_sprites_list.empty()' (limite a supprimer)
    #lorsque le joueur clique sur un bouton de la souris, il tire une balle (appui constant possible)

    #Met en place les armes différentes
        if ammo>=1 and tircontinue and pistol:
            damage=1
            if countir%40==0:
                tir(1)
            countir+=1

        elif ammo>=1 and tircontinue and machineg:
            damage=0.5
            if countir%5==0:
                tir(1)
            countir+=1

        elif tircontinue and shotg and ammo>=5:
            damage=2
            if countir%60==0:
                tir(5)
            countir+=1

        elif tircontinue and rocketl and ammo>=15:
            damage=0
            if countir%120==0:
                tir(15)
            countir+=1


    #Gère la collision entre le joueur et le vaisseau enemy
        for ship in ally_sprites_list:
            ships_hit_list=pygame.sprite.spritecollide(ship, enemy_sprites_list, False)

            for enemy in ships_hit_list:
                if enemy in enemyc_sprites_list:
                    vie-=1
                    enemyc_sprites_list.remove(enemy)
                elif enemy in enemyb_sprites_list:
                    vie-=2
                    enemyb_sprites_list.remove(enemy)
                elif enemy in enemya_sprites_list:
                    vie-=3
                    enemya_sprites_list.remove(enemy)
                elif enemy in enemys_sprites_list:
                    vie-=4
                    enemys_sprites_list.remove(enemy)
                explos=Explosion(enemy.rect.x-32,enemy.rect.y-32)
                explosion_sprites_list.add(explos)
                v-=1
                ships_hit_list.remove(enemy)
                all_sprites_list.remove(enemy)
                enemy_sprites_list.remove(enemy)
                if vie<=0:
                    all_sprites_list.remove(joueur)
                    ally_sprites_list.remove(joueur)
                    done=True

    #Gère la collision entre le joueur et les drops enemys
        for ship in ally_sprites_list:
            drop_hit_list=pygame.sprite.spritecollide(ship, drop_sprites_list, False)

            for drop in drop_hit_list:
                all_sprites_list.remove(drop)
                drop_sprites_list.remove(drop)
                ammo+=10

    #Gère la collision des ore avec le joueur
        for ship in ally_sprites_list:
            ore_hit_list=pygame.sprite.spritecollide(ship, ore_sprites_list, False)

            for ore in ore_hit_list:
                all_sprites_list.remove(ore)
                ore_sprites_list.remove(ore)
                nbrore-=1
                matrice_inventaire[0][0]+=1

        for enemy in enemy_sprites_list:
            if enemy.viemax<=0:
                if enemy in enemyc_sprites_list:
                    enemyc_sprites_list.remove(enemy)
                elif enemy in enemyb_sprites_list:
                    enemyb_sprites_list.remove(enemy)
                elif enemy in enemya_sprites_list:
                    enemya_sprites_list.remove(enemy)
                elif enemy in enemys_sprites_list:
                    enemys_sprites_list.remove(enemy)
                coin=Coin(enemy.rect.x,enemy.rect.y)
                all_sprites_list.add(coin)
                drop_sprites_list.add(coin)
                enemy_sprites_list.remove(enemy)
                all_sprites_list.remove(enemy)
                v-=1
                kills+=1
                
            #Met en place des point d'Exclamation alertant le joueur de la venue d'un enemy
            #quand il ce trouve soit en haut, en bas, a droite ou a gauche de l'ecran 
            if enemy.rect.x>W and H>enemy.rect.y>0:
                screen.blit(excla,(1880,enemy.rect.y))
            elif enemy.rect.x<0 and H>enemy.rect.y>0:
                screen.blit(excla,(30,enemy.rect.y))
            elif enemy.rect.y>H and W>enemy.rect.x>0:
                screen.blit(excla,(enemy.rect.x,1016))
            elif enemy.rect.y<0 and W>enemy.rect.x>0:
                screen.blit(excla,(enemy.rect.x,20))
            #quand il ce trouve en bas a gouche, en bas a droite, en haut a gauche ou en haut à droite
            elif enemy.rect.x<0 and enemy.rect.y<0:
                screen.blit(excla,(30,30))
            elif enemy.rect.x>W and enemy.rect.y>H:
                screen.blit(excla,(1880,1016))
            elif enemy.rect.x<0 and enemy.rect.y>H:
                screen.blit(excla,(30,1016))
            elif enemy.rect.x>W and enemy.rect.y<0:
                screen.blit(excla,(1880,30))
             
    #Supprime les vaisseauenemy avec contact avec la balle du vaisseau du joueur
        for bullet in bullet_sprites_list:
            enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_sprites_list, False)

            for enemy in enemy_hit_list:
                enemy_hit_list.remove(enemy)
                enemy.viemax-=damage
                if bullet.type=='rocketl':
                    explos=Explosion(enemy.rect.x-32,enemy.rect.y-32)
                    explosion_sprites_list.add(explos)
                    if enemy.rect.x-32<joueur.rect.x<enemy.rect.x+96 and enemy.rect.y-32<joueur.rect.y<enemy.rect.y+96:
                            vie-=2
                    for sprite in enemy_sprites_list:
                        if enemy.rect.x-150<sprite.rect.x<enemy.rect.x+214 and enemy.rect.y-150<sprite.rect.y<enemy.rect.y+214:
                            sprite.viemax-=3
                            
                bullet_sprites_list.remove(bullet)
                all_sprites_list.remove(bullet)
                    
                    
            if bullet.rect.x>bgX+3840 or bullet.rect.x<bgX or bullet.rect.y>bgY+2160 or bullet.rect.y<bgY:
                all_sprites_list.remove(bullet)
                bullet_sprites_list.remove(bullet)

        Merge(enemyc_sprites_list,enemyb_sprites_list,enemyc_collide_list)
        Merge(enemyb_sprites_list,enemya_sprites_list,enemyb_collide_list)
        Merge(enemya_sprites_list,enemys_sprites_list,enemya_collide_list)
            
            
        #gère la carte
    #Skip ces fonctions si le vaisseau principale est sur les bordures limites et si les infos de l'écran sont a leurs limites
        if joueur.rect.x==dist and bgX==0:
            pass
        elif joueur.rect.x==W-dist and bgX==-W:
            pass
        elif joueur.rect.y==dist and bgY==0:
            pass
        elif joueur.rect.y==H-dist and bgY==-H:
            pass

    #Permet le maintien de la carte entre l'écran et la taille de l'image
        else:
            if bgX>0:
                screen.blit(bg,(0,bgY))
            if bgX<-W:
                screen.blit(bg,(-W,bgY))
            if bgY>0:
                screen.blit(bg,(bgX,0))
            if bgY<-H:
                screen.blit(bg,(bgX,-H))

    #Gère l'arrière plan par rapport au joueur en mouvement et en contacte avec les bordures limites
            if joueur.rect.x==W-dist and d:
                bgX-=vitessea
            if joueur.rect.x==dist and a:
                bgX+=vitessea
            if joueur.rect.y==H-dist and s:
                bgY-=vitessea
            if joueur.rect.y==dist and w:
                bgY+=vitessea

    #Permet le mouvement des sprites ennemis par rapport au vaisseau du joueur lorsqu'ilse déplace sur les bordures de l'écran
            for enemy in enemy_sprites_list:
                    
                if joueur.rect.x==W-dist and d and bgX!=-W:
                    enemy.rect.x-=vitessea
                if joueur.rect.x==dist and a and bgX!=0:
                    enemy.rect.x+=vitessea
                if joueur.rect.y==H-dist and s and bgY!=-H:
                    enemy.rect.y-=vitessea
                if joueur.rect.y==dist and w and bgY!=0:
                    enemy.rect.y+=vitessea

        for sprite in explosion_sprites_list:
            sprite.explode()

        
        deplacementsprite(drop_sprites_list)
        deplacementsprite(ore_sprites_list)
        
        
        
        Point(940,940,str(vie),'tech','gauche',125,True)
        Point(940,100,str(kills),'tech','gauche',200,True)
        Arme(1500,908)
        bullet_sprites_list.update()
        bullet_sprites_list.draw(screen)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        temps+=1
        clock.tick(60)

    killspersec()
    if kills!=0 and nameofficial!='test0110':
        scorenom.append(nameofficial)
        scorenum.append(kills)

    for variablea in range(len(scorenum)):
        noml,maxim,randoshit=0,0,0
        for z in scorenum[variablea:]:
            if int(z)>int(maxim):
                maxim=int(z)
                randoshit=noml
            noml+=1
        scorenum.insert(variablea,maxim)
        scorenom.insert(variablea,scorenom[randoshit])
        scorenum.pop(randoshit+1)
        scorenom.pop(randoshit+1)
        scoreordre.append(scorenom[variablea]+':'+str(scorenum[variablea]))
      
    ScoreL=open('Directory/score.txt','w')
    for w in range(len(scoreordre)):
        ScoreL.write(str(scoreordre[w])+'\n')
    ScoreL.close()
    pygame.quit()
