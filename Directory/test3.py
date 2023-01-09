class Explosion:
    def __init__(self,x,y):
        self.count=0
        self.temps=TpsDiff(10)
        self.x=x
        self.y=y
    def explode(self):
        if self.count==11:
            self.count=0
            explo=False
            explosion_sprites_list.empty()
        scr = pygame.image.load('Explosion/'+str(self.count)+'exp.png').convert_alpha()
        screen.blit(scr,(self.x,self.y))
        self.temps.advance()
        if self.temps.advance():
            self.count+=1
        
        
