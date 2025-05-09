import pygame

okno=pygame.display.set_mode([800,500])
chaci=pygame.time.Clock()

mach=pygame.rect.Rect([400,250],[100,100])
raceta1=pygame.rect.Rect([300,10],[200,50])
raceta2=pygame.rect.Rect([300,440],[200,50])

vx=3
ry=4

m=1
shet2=0
shet1=0
while m==1:
    sobitia=pygame.event.get()
    for sobitie in sobitia:
        if sobitie.type==pygame.QUIT:
            m=2
    
    mach.x=mach.x+vx
    if mach.right>=800:
        vx=-3
    if mach.x<=0:
        vx=3 
    

    mach.y=mach.y+ry
    if mach.bottom>=500:
        shet1=shet1+1
        mach.y=250
        mach.x=400            
        ry=-4
    
       
    
    if mach.y<=0:
        shet2=shet2+1
        mach.y=250
        mach.x=400          
        ry=4
    if shet1==5:
        print("Выиграла верхняя ракетка")
        m=3
    if shet2==5:
        print("Выиграла нижняя ракетка")
        m=3

 
    
    clavishi=pygame.key.get_pressed()
    if clavishi[pygame.K_LEFT]==True:
        raceta2.x=raceta2.x-3
    if clavishi[pygame.K_RIGHT]==True:
        raceta2.x=raceta2.x+3
    if raceta2.colliderect(mach)==True:
        ry=-4
        
    
    if clavishi[pygame.K_6]==True:
        raceta1.x=raceta1.x-3
    if clavishi[pygame.K_4]==True:
        raceta1.x=raceta1.x+3
    if raceta1.colliderect(mach)==True:
        ry=+4
        


    okno.fill([0,255,0])
    pygame.draw.ellipse(okno,[255,0,255],mach)
    pygame.draw.rect(okno,[150,50,20],raceta1)
    pygame.draw.rect(okno,[150,50,20],raceta2)
    pygame.display.update()
    
    chaci.tick(100)





    

        
