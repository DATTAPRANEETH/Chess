import pygame



pygame.init()
ds = pygame.display.set_mode((1200, 800))
white = (255, 255, 255)
green = (134, 167, 137)
black = (5, 5, 5)
ds.fill(green)
def boxonclicktocr(pos):
    c1=pos[0]
    c2=pos[1]
    c1=c1//100
    c2=c2//100
    return [c1,c2]
def fromcrtocenter(c):
    row=int(c[0])
    col=int(c[1])
    centerx=row*100+50
    centery=col*100+50
    return [centerx,centery]
def wgivesinglediagnol(st):
    if st!=0:
        spy=st
        k=int(spy[0])
        k1=int(spy[1])
        ld=str(k-1)+str(k1-1)
        rd=str(k+1)+str(k1-1)
        front=str(k)+str(k1-1)
        return [ld,rd,front]
    else:
        return ["-1","-1"]
def bgivesinglediagnol(st):
    if st!=0:
        spy=st
        k=int(spy[0])
        k1=int(spy[1])
        ld=str(k-1)+str(k1+1)
        rd=str(k+1)+str(k1+1)
        front=str(k)+str(k1+1)
        return [ld,rd,front]
    else:
        return ["-1","-1"]
def STR(x,y):
    if x>=0 and y>=0 and x<=7 and y<=7:
        return str(x)+str(y)
    else:
        return str(-1)
def drawrectfrompos(x):
    pygame.draw.rect(ds,black,(int(x[0])*100,int(x[1])*100,100,100),5)
def horsereach(k): 
    if k!=0:  
        x=int(k[0])
        y=int(k[1])
        l=[STR(x-1,y-2),STR(x+1,y-2),STR(x-1,y+2),STR(x+1,y+2),STR(x-2,y-1),STR(x+2,y-1),STR(x-2,y+1),STR(x+2,y+1)]
        l=[i for i in l if i!="-1"]
        l=[i for i in l if int(i[0]) <= 7 and int(i[-1]) <= 7 and i not in wsl+wh+wc+we+wk+wq]   
        return l
    else:
        return []
def camelreach(k):
    if k!=0:

        x=int(k[0])
        y=int(k[1])
        x2=x
        y2=y
        x3=x
        y3=y
        x4=x
        y4=y
        l=[]
        
        while x>=0 and y>=0:
            x=x-1
            y=y-1
            o1=STR(x,y)
            if o1 in wsl+wc+wh+we+wk+wq:
                break
            elif o1 in bsl+bc+bh+be+bk+bq+ib:
                l.append(o1)
                break
            else:
                l.append(o1)
        while x2<=7 and y2>=0:
            x2=x2+1
            y2=y2-1
            o1=STR(x2,y2)
            if o1 in wsl+wc+wh+we+wk+wq:
                break
            elif o1 in bsl+bc+bh+be+bk+bq+ib:
                l.append(o1)
                break
            else:
                l.append(o1)
        while x3>=0 and y3<=7:
            x3=x3-1
            y3=y3+1
            o1=STR(x3,y3)
            if o1 in wsl+wc+wh+we+wk+wq:
                break
            elif o1 in bsl+bc+bh+be+bk+bq+ib:
                l.append(o1)
                break
            else:
                l.append(o1)
        while x4<=7 and y4<=7:
            x4=x4+1
            y4=y4+1
            o1=STR(x4,y4)
            if o1 in wsl+wc+wh+we+wk+wq:
                break
            elif o1 in bsl+bc+bh+be+bk+bq+ib:
                l.append(o1)
                break
            else:
                l.append(o1)
        return l
    else:
        return []
def elephantreach(k):
    if k!=0:
        x = int(k[0])
        y = int(k[1])
        x2 = x
        y2 = y
        x3 = x
        y3 = y
        x4 = x
        y4 = y
        l=[]
        while y <= 7:
            y = y + 1
            q = STR(x, y)
            if q in wc + wh + wsl + we + wk + wq:
                break
            elif q in bc + bh + bsl + be + bk + bq+ib:
                l.append(q)
                break
            else:
                l.append(q)

        while y2 >= 0:
            y2 = y2 - 1
            q2 = STR(x2, y2)
            if q2 in wc + wh + wsl + we + wk + wq:
                break
            elif q2 in bc + bh + bsl + be + bk + bq+ib:
                l.append(q2)
                break
            else:
                l.append(q2)

        while x3 >= 0:
            x3 = x3 - 1
            q3 = STR(x3, y3)
            if q3 in wc + wh + wsl + we + wk + wq:
                break
            elif q3 in bc + bh + bsl + be + bk + bq+ib:
                l.append(q3)
                break
            else:
                l.append(q3)

        while x4 <= 7:
            x4 = x4 + 1
            q4 = STR(x4, y4)
            if q4 in wc + wh + wsl + we + wk + wq:
                break
            elif q4 in bc + bh + bsl + be + bk + bq+ib:
                l.append(q4)
                break
            else:
                l.append(q4)
        return l
    else:
        return []
def wkingreach(k):
    x=int(k[0])
    y=int(k[1])
    l=[STR(x-1,y-1),STR(x,y-1),STR(x+1,y-1),STR(x-1,y),STR(x+1,y),STR(x-1,y+1),STR(x,y+1),STR(x+1,y+1)]
    l=[i for i in l if i not in we+wh+wc+wq+wsl]
    l=[i for i in l if i!='-1']
    return l
def bkingreach(k):
    x=int(k[0])
    y=int(k[1])
    l=[STR(x-1,y-1),STR(x,y-1),STR(x+1,y-1),STR(x-1,y),STR(x+1,y),STR(x-1,y+1),STR(x,y+1),STR(x+1,y+1)]
    l=[i for i in l if i not in be+bh+bc+bq+bsl]
    l=[i for i in l if i!='-1']
    return l
def bhorsereach(k):        
    if k!=0:  
        x=int(k[0])
        y=int(k[1])
        l=[STR(x-1,y-2),STR(x+1,y-2),STR(x-1,y+2),STR(x+1,y+2),STR(x-2,y-1),STR(x+2,y-1),STR(x-2,y+1),STR(x+2,y+1)]
        l=[i for i in l if i!="-1"]
        l=[i for i in l if int(i[0]) <= 7 and int(i[-1]) <= 7 and i not in bsl+bh+bc+be+bk+bq]   
        return l
    else:
        return []    
def bcamelreach(k):
    if k!=0:

        x=int(k[0])
        y=int(k[1])
        x2=x
        y2=y
        x3=x
        y3=y
        x4=x
        y4=y
        l=[]
        
        while x>=0 and y>=0:
            x=x-1
            y=y-1
            o1=STR(x,y)
            if o1 in bsl+bc+bh+be+bk+bq:
                break
            elif o1 in wsl+wc+wh+we+wk+wq+iw:                
                l.append(o1)
                break
            else:
                l.append(o1)
        while x2<=7 and y2>=0:
            x2=x2+1
            y2=y2-1
            o1=STR(x2,y2)
            if o1 in bsl+bc+bh+be+bk+bq:
                break
            elif o1 in wsl+wc+wh+we+wk+wq+iw:
                l.append(o1)
                break
            else:
                l.append(o1)
        while x3>=0 and y3<=7:
            x3=x3-1
            y3=y3+1
            o1=STR(x3,y3)
            if o1 in bsl+bc+bh+be+bk+bq:
                break
            elif o1 in wsl+wc+wh+we+wk+wq+iw:
                l.append(o1)
                break
            else:
                l.append(o1)
        while x4<=7 and y4<=7:
            x4=x4+1
            y4=y4+1
            o1=STR(x4,y4)
            if o1 in bsl+bc+bh+be+bk+bq:
                break
            elif o1 in wsl+wc+wh+we+wk+wq+iw:
                l.append(o1)
                break
            else:
                l.append(o1)
        return l
    else:
        return []
def belephantreach(k):
    if k!=0:
        x = int(k[0])
        y = int(k[1])
        x2 = x
        y2 = y
        x3 = x
        y3 = y
        x4 = x
        y4 = y
        l=[]
        while y <= 7:
            y = y + 1
            q = STR(x, y)
            if q in bc + bh + bsl + be + bk + bq:
                break
            elif q in wc + wh + wsl + we + wk + wq+iw:
                l.append(q)
                break
            else:
                l.append(q)

        while y2 >= 0:
            y2 = y2 - 1
            q2 = STR(x2, y2)
            if q2 in bc + bh + bsl + be + bk + bq:
                break
            elif q2 in wc + wh + wsl + we + wk + wq+iw:
                l.append(q2)
                break
            else:
                l.append(q2)

        while x3 >= 0:
            x3 = x3 - 1
            q3 = STR(x3, y3)
            if q3 in bc + bh + bsl + be + bk + bq:
                break
            elif q3 in wc + wh + wsl + we + wk + wq+iw:
                l.append(q3)
                break
            else:
                l.append(q3)

        while x4 <= 7:
            x4 = x4 + 1
            q4 = STR(x4, y4)
            if q4 in bc + bh + bsl + be + bk + bq:
                break
            elif q4 in wc + wh + wsl + we + wk + wq+iw:
                l.append(q4)
                break
            else:
                l.append(q4)
        return l
    else:
        return []
def bchecker():
    man2_temp = []
    for i in bsl:
        bleo_temp = bgivesinglediagnol(i)
        man2_temp.extend([bleo_temp[0], bleo_temp[1]])
    for i in be:
        bleo1_temp = belephantreach(i)
        man2_temp.extend(bleo1_temp)
    for i in bc:
        bleo2_temp = bcamelreach(i)
        man2_temp.extend(bleo2_temp)
    for i in bh:
        bleo3_temp = bhorsereach(i)
        man2_temp.extend(bleo3_temp)
    for i in bq:
        bleo41_temp = bcamelreach(i)
        bleo42_temp = belephantreach(i)
        bleo4_temp = bleo41_temp + bleo42_temp
        man2_temp.extend(bleo4_temp)
    for i in bk:
        bleo5_temp = bkingreach(i)
        man2_temp.extend(bleo5_temp)
    man2_temp = [i for i in man2_temp if i != "-1"]
    if wk[0] in man2_temp:
        return 1
    else:
        return 0
def wchecker():
    man2_temp = []
    for i in wsl:
        bleo_temp = wgivesinglediagnol(i)
        man2_temp.extend([bleo_temp[0], bleo_temp[1]])
    for i in we:
        bleo1_temp = elephantreach(i)
        man2_temp.extend(bleo1_temp)
    for i in wc:
        bleo2_temp = camelreach(i)
        man2_temp.extend(bleo2_temp)
    for i in wh:
        bleo3_temp = horsereach(i)
        man2_temp.extend(bleo3_temp)
    for i in wq:
        bleo41_temp = camelreach(i)
        bleo42_temp = elephantreach(i)
        bleo4_temp = bleo41_temp + bleo42_temp
        man2_temp.extend(bleo4_temp)
    for i in wk:
        bleo5_temp = wkingreach(i)
        man2_temp.extend(bleo5_temp)
    man2_temp = [i for i in man2_temp if i != "-1"]
    if bk[0] in man2_temp:
        return 1
    else:
        return 0
def wjf():
    pol={}
    for i in wsl:
        if i!=0:
            if i[1]=="6":
                h0=int(i[0])
                h1=int(i[1])
                pol[i]=[STR(h0,h1-1),STR(h0,h1-2)]
            elif int(i[1])<6 and int(i[1])>0:
                h0=int(i[0])
                h1=int(i[1])                
                pol[i]=[STR(h0,h1-1)]
    return pol
def bjf():
    pol={}
    for i in bsl:
        if i!=0:
            if i[1]=="1":
                h0=int(i[0])
                h1=int(i[1])
                pol[i]=[STR(h0,h1+1),STR(h0,h1+2)]
            elif int(i[1])<7 and int(i[1])>1:
                h0=int(i[0])
                h1=int(i[1])                
                pol[i]=[STR(h0,h1+1)]
    return pol
def bbchecker(o):
    man2_temp = []
    for i in bsl:
        bleo_temp = bgivesinglediagnol(i)
        man2_temp.extend([bleo_temp[0], bleo_temp[1]])
    for i in be:
        bleo1_temp = belephantreach(i)
        man2_temp.extend(bleo1_temp)
    for i in bc:
        bleo2_temp = bcamelreach(i)
        man2_temp.extend(bleo2_temp)
    for i in bh:
        bleo3_temp = bhorsereach(i)
        man2_temp.extend(bleo3_temp)
    for i in bq:
        bleo41_temp = bcamelreach(i)
        bleo42_temp = belephantreach(i)
        bleo4_temp = bleo41_temp + bleo42_temp
        man2_temp.extend(bleo4_temp)

    for i in bk:
        bleo5_temp = bkingreach(i)
        man2_temp.extend(bleo5_temp)
    man2_temp = [i for i in man2_temp if i != "-1"]

    if o in man2_temp:
        return 1
    else:
        return 0          
def wwchecker(o):
    man2_temp = []
    for i in wsl:
        bleo_temp = wgivesinglediagnol(i)
        man2_temp.extend([bleo_temp[0], bleo_temp[1]])
    for i in we:
        bleo1_temp = elephantreach(i)
        man2_temp.extend(bleo1_temp)
    for i in wc:
        bleo2_temp = camelreach(i)
        man2_temp.extend(bleo2_temp)
    for i in wh:
        bleo3_temp = horsereach(i)
        man2_temp.extend(bleo3_temp)
    for i in wq:
        bleo41_temp = camelreach(i)
        bleo42_temp = elephantreach(i)
        bleo4_temp = bleo41_temp + bleo42_temp
        man2_temp.extend(bleo4_temp)

    for i in wk:
        bleo5_temp = wkingreach(i)
        man2_temp.extend(bleo5_temp)
    man2_temp = [i for i in man2_temp if i != "-1"]

    if o in man2_temp:
        return 1
    else:
        return 0  
def checkbpower(crstr):
    o=crstr
    if o in bsl:
        return 1
    elif o in bc:
        return 2
    elif o in bh:
        return 3
    elif o in be:
        return 4
    elif o in bq:
        return 5
    elif o in bk:
        return 6
    else:
        return -1
def checkwpower(crstr):
    o=crstr
    if o in wsl:
        return 1
    elif o in wc:
        return 2
    elif o in wh:
        return 3
    elif o in we:
        return 4
    elif o in wq:
        return 5
    elif o in wk:
        return 6
    else:
        return -1
def kalake():
    man2_temp = []
    for i in bsl:
        bleo_temp = bgivesinglediagnol(i)
        man2_temp.extend([bleo_temp[0], bleo_temp[1]])
    for i in be:
        bleo1_temp = belephantreach(i)
        man2_temp.extend(bleo1_temp)
    for i in bc:
        bleo2_temp = bcamelreach(i)
        man2_temp.extend(bleo2_temp)
    for i in bh:
        bleo3_temp = bhorsereach(i)
        man2_temp.extend(bleo3_temp)
    for i in bq:
        bleo41_temp = bcamelreach(i)
        bleo42_temp = belephantreach(i)
        bleo4_temp = bleo41_temp + bleo42_temp
        man2_temp.extend(bleo4_temp)

    for i in bk:
        bleo5_temp = wkingreach(i)
        man2_temp.extend(bleo5_temp)
    man2_temp = [i for i in man2_temp if i != "-1"]  
    return man2_temp 
def bkalake():
    man_temp = []
    for i in wsl:
        bleo_tep = wgivesinglediagnol(i)
        man_temp.extend([bleo_tep[0], bleo_tep[1]])
    for i in we:
        bleo1_tep = elephantreach(i)
        man_temp.extend(bleo1_tep)
    for i in wc:
        bleo2_tep = camelreach(i)
        man_temp.extend(bleo2_tep)
    for i in wh:
        bleo3_tep =horsereach(i)
        man_temp.extend(bleo3_tep)
    for i in wq:
        bleo41_tep = camelreach(i)
        bleo42_tep = elephantreach(i)
        bleo4_tep = bleo41_tep + bleo42_tep
        man_temp.extend(bleo4_tep)

    for i in wk:
        bleo5_tep = wkingreach(i)
        man_temp.extend(bleo5_tep)
    man_temp = [i for i in man_temp if i != "-1"]  
    return man_temp     

    
    
pygame.draw.line(ds, white, (0, 0), (800, 0), 2)
pygame.draw.line(ds, white, (0, 0), (0, 800), 2)
pygame.draw.line(ds, white, (800, 800), (800, 0), 2)
pygame.draw.line(ds, white, (800, 800), (0, 800), 2)
wpl=[]
ws=[]
bs=[]
bpl=[]
wq=["37"]
bq=["30"]
bk=["40"]
wk=["47"]
we=["07","77"]
be=["00","70"]
wh=["17","67"]
bh=["10","60"]
wc=["27","57"]
bc=["20","50"]
iw=[]
ib=[]
wsl=[str(i)+"6" for i in range(0,8)]
bsl=[str(i)+"1" for i in range(0,8)]


for i in range(0, 8):
    for j in range(0, 8):
        i1 = 100 * i
        j1 = 100 * j
        if (i + j) % 2 == 0:
            pygame.draw.rect(ds, white, (i1, j1, 100, 100))
        else:
            pygame.draw.rect(ds, green, (i1, j1, 100, 100))
for j in range(8):
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/wp.png")
    i1=i.get_rect()
    i1.center=(100*j+50,650)
    ws.append([i,i1,j])

    z=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bwp.png")
    z1=z.get_rect()
    z1.center=(100*j+50,150)
    bs.append([z,z1])    
for j in range(2):
    k=j*700+50
    k1=j*500+150
    k2=j*300+250
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/wrook.png")
    i1=i.get_rect()
    i1.center=(k,750)
    wpl.append([i,i1,"e"])
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bwrook.png")
    i1=i.get_rect()
    i1.center=(k,50)
    bpl.append([i,i1,"e"])
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/strategy.png")
    i1=i.get_rect()
    i1.center=(k1,750)
    wpl.append([i,i1,"h"])
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bstrategy.png")
    i1=i.get_rect()
    i1.center=(k1,50)
    bpl.append([i,i1,"h"])
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bishop.png")
    i1=i.get_rect()
    i1.center=(k2,750)
    wpl.append([i,i1,"c"])
    i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bbishop.png")
    i1=i.get_rect()
    i1.center=(k2,50)
    bpl.append([i,i1,"c"])
i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/king.png")
i1=i.get_rect()
i1.center=(450,750)
wpl.append([i,i1,"k"])
z=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/queen.png")
z1=z.get_rect()
z1.center=(350,750)
wpl.append([z,z1,"q"])
i=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bking.png")
i1=i.get_rect()
i1.center=(450,50)
bpl.append([i,i1,"k"])
z=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bqueen.png")
z1=z.get_rect()
z1.center=(350,50)
bpl.append([z,z1,"q"])
run = True
white_pointer=-1
black_pointer=-1
clock = pygame.time.Clock()
turn = 1
wcheckedby=[]
bcheckedby=[]
markwhite=0
blackshown=0
markblack=0
whiteshown=0
kingmoved=0            
wlrook=0
wrrook=0
bkingmoved=0
blrook=0
brrook=0
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False            
        wlcastlepossible=1
        wrcastlepossible=1
        blcastlepossible=1
        brcastlepossible=1
        man=[]
        wd={}
        bd={}
        wdwos={}
        bdwos={}
        if wlrook==1:
            wlcastlepossible=0
        if wrrook==1:
            wrcastlepossible=0
        if kingmoved==1:
            wrcastlepossible=0
            wlcastlepossible=0
        if blrook==1:
            blcastlepossible=0
        if brrook==1:
            brcastlepossible=0
        if bkingmoved==1:
            blcastlepossible=0
            brcastlepossible=0
        if blcastlepossible==1:
            if "10" in bc+bh+bq+bh:
                blcastlepossible=0
            if "20" in bc+bh+bq+bh:
                blcastlepossible=0     
        if brcastlepossible==1:
            if "40" in bc+bh+bq+bh:
                brcastlepossible=0
            if "50" in bc+bh+bq+bh:
                brcastlepossible=0     
            if "60" in bc+bh+bq+bh:
                brcastlepossible=0   
        deer=[]
        for i in we:
            deer.extend(elephantreach(i))
        for i in wh:
            deer.extend(horsereach(i))   
        for i in wc:
            deer.extend(camelreach(i)) 
        for i in wq:
            deer.extend(camelreach(i))
            deer.extend(elephantreach(i))
        for i in wk:
            deer.extend(wkingreach(i))
        for i in wsl:
            j=wgivesinglediagnol(i)
            deer.extend(j) 
        if blcastlepossible==1:
            if "00" in deer:
                blcastlepossible=0
            if "10" in deer:
                blcastlepossible=0        
            if "20" in deer:
                blcastlepossible=0                                                                             
            if "30" in deer:
                blcastlepossible=0
        if brcastlepossible==1:
            if "30" in deer:
                brcastlepossible=0
            if "40" in deer:
                brcastlepossible=0
            if "50" in deer:
                brcastlepossible=0                
            if "60" in deer:
                brcastlepossible=0                
            if "70" in deer:
                brcastlepossible=0                
         

        if wlcastlepossible==1:
            if "17" in wc+wh+wq+wh:
                wlcastlepossible=0
            if "27" in wc+wh+wq+wh:
                wlcastlepossible=0 
            if "37" in wc+wh+wq+wh:
                wlcastlepossible=0
        if wrcastlepossible==1:
            if "57" in wc+wh+wq+wh:
                wrcastlepossible=0
            if "67" in wc+wh+wq+wh:
                wrcastlepossible=0 
        aad=[]
        for i in be:
            aad.extend(belephantreach(i))
        for i in bc:
            aad.extend(bcamelreach(i))  
        for i in bh:
            aad.extend(bhorsereach(i)) 
        for i in bq:
            aad.extend(belephantreach(i))                                 
            aad.extend(bcamelreach(i))
        for i in bk:
            aad.extend(bkingreach(i))
        for i in bsl:
            j=bgivesinglediagnol(i)            
            aad.extend(j)
        if wlcastlepossible==1:
            if "07" in aad:
                wlcastlepossible=0
            if "17" in aad:
                wlcastlepossible=0
            if "27" in aad:
                wlcastlepossible=0
            if "37" in aad:
                wlcastlepossible=0
            if "47" in aad:
                wlcastlepossible=0                
        if wrcastlepossible==1:
            if "47" in aad:
                wrcastlepossible=0            
            if "57" in aad:
                wrcastlepossible=0
            if "67" in aad:
                wrcastlepossible=0  
            if "77" in aad:
                wrcastlepossible=0                                         
        if whiteshown==1:
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                c1=event.pos[0]
                c2=event.pos[1]
                if c2>100 and c2<200:
                    if c1>1100 and c1<1200:
                        wq.append(markwhite)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/queen.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markwhite)
                        wpl.append([i4,i44,'q'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))                        
                    elif c1>1000 and c1<1100:
                        wc.append(markwhite)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bishop.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markwhite)
                        wpl.append([i4,i44,'c'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))       
                    elif c1>900 and c1<1000:
                        wh.append(markwhite)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/strategy.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markwhite)
                        wpl.append([i4,i44,'h'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))                                                       
                    elif c1>800 and c1<900:
                        we.append(markwhite)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/wrook.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markwhite)
                        wpl.append([i4,i44,'e'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))       
                whiteshown=0                     
        if blackshown==1:
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                c1=event.pos[0]
                c2=event.pos[1]
                if c2>100 and c2<200:
                    if c1>1100 and c1<1200:
                        bq.append(markblack)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bqueen.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markblack)
                        bpl.append([i4,i44,'q'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))                        
                    elif c1>1000 and c1<1100:
                        bc.append(markblack)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bbishop.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markblack)
                        bpl.append([i4,i44,'c'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))       
                    elif c1>900 and c1<1000:
                        bh.append(markblack)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bstrategy.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markblack)
                        bpl.append([i4,i44,'h'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))                                                       
                    elif c1>800 and c1<900:
                        be.append(markblack)
                        i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bwrook.png")
                        i44=i4.get_rect()
                        i44.center=fromcrtocenter(markblack)
                        bpl.append([i4,i44,'e'])
                        for i in range(8, 12):
                            for j in range(0, 12):
                                i1 = 100 * i
                                j1 = 100 * j

                                pygame.draw.rect(ds, green, (i1, j1, 100, 100)) 
                blackshown=0  
        for i in wsl:
            leo=wgivesinglediagnol(i)
            man.extend([leo[0],leo[1]])
            wd[i]=[leo[0],leo[1]]
        for i in we:
            leo1=elephantreach(i)
            man.extend(leo1)
            wd[i]=leo1
            wdwos[i]=leo1
        for i in wc:
            leo2=camelreach(i)
            man.extend(leo2)
            wd[i]=leo2
            wdwos[i]=leo2
        for i in wh:
            leo3=horsereach(i)
            man.extend(leo3)
            wd[i]=leo3
            wdwos[i]=leo3
        for i in wq:
            leo41=camelreach(i)
            leo42=elephantreach(i)
            leo4=leo41+leo42
            man.extend(leo4)
            wd[i]=leo4
            wdwos[i]=leo4
        for i in wk:
            leo5=wkingreach(i)
            man.extend(leo5)
            wd[i]=leo5
            wdwos[i]=leo5
        man=[i for i in man if i!="-1"]

        if bk[0] in man:
            wcheck=1
        else:
            wcheck=0
            
            
        man2=[]
        for i in bsl:
            bleo=bgivesinglediagnol(i)
            man2.extend([bleo[0],bleo[1]])
            bd[i]=[bleo[0],bleo[1]]
        for i in be:
            bleo1=belephantreach(i)
            man2.extend(bleo1)
            bd[i]=bleo1
            bdwos[i]=bleo1
        for i in bc:
            bleo2=bcamelreach(i)
            man2.extend(bleo2)
            bd[i]=bleo2
            bdwos[i]=bleo2
        for i in bh:
            bleo3=bhorsereach(i)
            man2.extend(bleo3)
            bd[i]=bleo3
            bdwos[i]=bleo3
        for i in bq:
            bleo41=bcamelreach(i)
            bleo42=belephantreach(i)
            bleo4=bleo41+bleo42
            man2.extend(bleo4)
            bd[i]=bleo4
            bdwos[i]=bleo4
        for i in bk:
            bleo5=wkingreach(i)
            man2.extend(bleo5)
            bd[i]=bleo5
            bdwos[i]=bleo5
        man2=[i for i in man2 if i!="-1"]

        if wk[0] in man2:
            bcheck=1
        else:
            bcheck=0            
        if wcheck==1:
            t=bk[0]
            pygame.draw.rect(ds,(255,0,0),(int(t[0])*100,int(t[1])*100,100,100),5)
        if bcheck==1:
            t1=wk[0]
            pygame.draw.rect(ds,(255,0,0),(int(t1[0])*100,int(t1[1])*100,100,100),5)
        


                                        
        if turn==1:            
            if bcheck==0:
   
                if white_pointer!=-1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        crstr1=crstr
                        c1=event.pos[0]
                        c2=event.pos[1]
                        c=[c1,c2]
                        cr=boxonclicktocr(c)
                        crstr2=str(cr[0])+str(cr[1]) 
    

                        if crstr2 not in reachablebox:
                            for i in range(0, 8):
                                for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                    
                        else:
                            turn=0
                            if crstr1 in wsl:
                                try:
                                    ind = wsl.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop

                                
                                if crstr2 in bsl:
                                    ind2=bsl.index(crstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif crstr2 in bh:
                                    ii=bh.index(crstr2)
                                    bh[ii]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif crstr2 in bc:
                                    ii=bc.index(crstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']  
                                elif crstr2 in be:
                                    ii=be.index(crstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']                                                                                                    
                                elif crstr2 in bq:
                                    ii=bq.index(crstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']  
                                  
                                if crstr1 in wsl:                          
                                    wsl.remove(crstr1)
                                    
                                    wsl.insert(ind, crstr2)

                                # Update ws list
                                ws[ind][1].center = fromcrtocenter(crstr2) 
                                leo=wgivesinglediagnol(crstr2)
                                leo.pop()
                                if bk[0] in leo:
                                    bcheckedby.append(crstr2) 
                                if crstr2[1]=='0':
                                    sos=wsl.index(crstr2)
                                    
                                    wsl[sos]=0     
                                    ws[sos]=[0,0] 
                                    t=pygame.font.SysFont('calibri',48)
                                    r1=t.render("SELECT",True,black)
                                    r11=r1.get_rect()
                                    r11.center=(1000,50)
                                    i1=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/wrook.png")
                                    i11=i1.get_rect()
                                    i11.center=(850,150)
                                    i2=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/strategy.png")
                                    i22=i2.get_rect()
                                    i22.center=(950,150)
                                    i3=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bishop.png")
                                    i33=i3.get_rect()
                                    i33.center=(1050,150)
                                    i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/queen.png")
                                    i44=i4.get_rect()
                                    i44.center=(1150,150)
                                    drawrectfrompos("81")
                                    drawrectfrompos("91")
                                    pygame.draw.rect(ds,black,(1000,100,100,100),5)
                                    pygame.draw.rect(ds,black,(1100,100,100,100),5)
                                    
                                    ds.blit(r1,r11)
                                    ds.blit(i1,i11)
                                    ds.blit(i2,i22)
                                    ds.blit(i3,i33)
                                    ds.blit(i4,i44)  
                                    whiteshown=1   
                                    markwhite=crstr2
                                else:
                                    whiteshown=0                               
                                                                           
                            elif crstr1 in wh:
                                lak=[i for i in wpl if i[2]=="h"]

                                try:
                                    ind = wh.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                wh[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2)
                                lai=horsereach(crstr2)
                                if bk[0] in lai:
                                    bcheckedby.append(crstr2)
                                if crstr2 in bsl:
                                    ind2=bsl.index(crstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif crstr2 in bh:
                                    ind=bh.index(crstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h']
                                elif crstr2 in bc:
                                    ii=bc.index(crstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']  
                                elif crstr2 in be:
                                    ii=be.index(crstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']    
                                elif crstr2 in bq:
                                    ii=bq.index(crstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']  
                                                                                                                                                     
                            elif crstr1 in wc:
                                lak=[i for i in wpl if i[2]=="c"]

                                try:
                                    ind = wc.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                wc[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2)       
                                lai=camelreach(crstr2)
                                if bk[0] in lai:
                                    bcheckedby.append(crstr2)                
                                if crstr2 in bsl:
                                    ind2=bsl.index(crstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif crstr2 in bh:
                                    ind=bh.index(crstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif crstr2 in bc:
                                    ii=bc.index(crstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']
                                elif crstr2 in be:
                                    ii=be.index(crstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']  
                                elif crstr2 in bq:
                                    ii=bq.index(crstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']                                                                                                                              
                            elif crstr1 in wq:
                                lak=[i for i in wpl if i[2]=="q"]

                                try:
                                    ind = wq.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  

                                wq[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2)   
                                lai=camelreach(crstr2)
                                lai2=elephantreach(crstr2)
                                if bk[0] in lai+lai2:
                                    bcheckedby.append(crstr2)                                                   
                                if crstr2 in bsl:
                                    ind2=bsl.index(crstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif crstr2 in bh:
                                    ind=bh.index(crstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif crstr2 in bc:
                                    ii=bc.index(crstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']
                                elif crstr2 in be:
                                    ii=be.index(crstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']  
                                elif crstr2 in bq:
                                    ii=bq.index(crstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']   
                            elif crstr1 in wk:
                                if crstr2 not in we:
                                    lak=[i for i in wpl if i[2]=="k"]

                                    try:
                                        ind = wk.index(crstr1)
                                    except ValueError:
                                        # Handle the case where crstr1 is not found in wsl
                                        print("Error: crstr1 not found in wsl.")
                                        continue  # Skip the rest of the loop  
                                    wk[ind]=crstr2
                                    lak[ind][1].center = fromcrtocenter(crstr2) 
                                    kingmoved=1                   
                                    if crstr2 in bsl:
                                        ind2=bsl.index(crstr2)
                                        bs[ind2]=[0,0]
                                        bsl[ind2]=0
                                    elif crstr2 in bh:
                                        ind=bh.index(crstr2)
                                        bh[ind]=0
                                        mo=[i for i in bpl if i[2]=="h"]
                                        illa=mo[ind]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            bpl[inde]=[0,0,'h'] 
                                        
                                    elif crstr2 in bc:
                                        ii=bc.index(crstr2)
                                        bc[ii]=0
                                        mo=[i for i in bpl if i[2]=="c"]
                                        illa=mo[ii]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            bpl[inde]=[0,0,'c']
                                            
                                    elif crstr2 in be:
                                        ii=be.index(crstr2)
                                        be[ii]=0
                                        mo=[i for i in bpl if i[2]=="e"]
                                        illa=mo[ii]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            bpl[inde]=[0,0,'e']  
                                            
                                    elif crstr2 in bq:
                                        ii=bq.index(crstr2)
                                        bq[ii]=0
                                        mo=[i for i in bpl if i[2]=="q"]
                                        illa=mo[ii]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            bpl[inde]=[0,0,'q']                                           
                                else:
                                    if crstr2=="07":
                                        lak=[i for i in wpl if i[2]=="k"]
                                        try:
                                            ind = wk.index(crstr1)
                                        except ValueError:
                                            # Handle the case where crstr1 is not found in wsl
                                            print("Error: crstr1 not found in wsl.")
                                            continue  # Skip the rest of the loop  
                                        wk[ind]="17"
                                        lak[ind][1].center = fromcrtocenter("17")  
                                        lak2=[i for i in wpl if i[2]=="e"]
                                        we[0]="27"
                                        lak2[0][1].center=fromcrtocenter("27")            
                                    elif crstr2=="77":
                                        lak=[i for i in wpl if i[2]=="k"]
                                        try:
                                            ind = wk.index(crstr1)
                                        except ValueError:
                                            # Handle the case where crstr1 is not found in wsl
                                            print("Error: crstr1 not found in wsl.")
                                            continue  # Skip the rest of the loop  
                                        wk[ind]="67"
                                        lak[ind][1].center = fromcrtocenter("67")  
                                        lak2=[i for i in wpl if i[2]=="e"]
                                        we[0]="57"
                                        lak2[0][1].center=fromcrtocenter("57")                                                                 
                            elif crstr1 in we:    
                                lak=[i for i in wpl if i[2]=="e"]
                                
                                try:
                                    ind = we.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                we[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2)
                                if ind==0:
                                    wlrook=1
                                elif ind==1:
                                    wrrook=1                               
                                lai=elephantreach(crstr2)
                                if bk[0] in lai:
                                    bcheckedby.append(crstr2)                                                                                             
                                if crstr2 in bsl:
                                    ind2=bsl.index(crstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif crstr2 in bh:
                                    ind=bh.index(crstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif crstr2 in bc:
                                    ii=bc.index(crstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']   
                                elif crstr2 in be:
                                    iei=be.index(crstr2)
                                    be[iei]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[iei]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']   
                                elif crstr2 in bq:
                                    ii=bq.index(crstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']                                                                                                    
                            for i in range(0, 8):
                                for j in range(0, 8):
                                    i1 = 100 * i
                                    j1 = 100 * j
                                    if (i + j) % 2 == 0:
                                        pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                    else:
                                        pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                            


            
                        white_pointer=-1                                            
                else:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        reachablebox=[]

                        c1=event.pos[0]
                        c2=event.pos[1]
                        c=[c1,c2]
                        cr=boxonclicktocr(c)
                        crstr=str(cr[0])+str(cr[1])


                        found=0
                        selected=0
                        if crstr in wsl:
                            found=1
                            if found==1:
                                if white_pointer==-1:
                                    if crstr[1]=='6':
                                        leo=wgivesinglediagnol(crstr)
                                        drawrectfrompos(crstr)
                                        if leo[2] not in bsl+bh+wh+wsl+bc+wc+be+we+wq+bq+wk+bk:
                                            reachablebox.append(crstr[0]+str(int(crstr[1])-1))
                                            if wgivesinglediagnol(leo[2])[2] not in bsl+bh+wh+wsl+bc+wc+be+we+bq+wq+bk+wk:
                                                reachablebox.append(crstr[0]+str(int(crstr[1])-2))
                                        
 
                                        i=0
                                        while i<len(reachablebox):
                                                pi=wsl.index(crstr)
                                                ant=wsl[pi]
                                                wsl[pi]=reachablebox[i]
                                                lpl=kalake()                                            
                                                if wk[0] in lpl:                                                
                                                    reachablebox[i]=0

                                                wsl[pi]=ant
                                                i=i+1
                                        if leo[0] in bsl+bh+bc+be+bk+bq:
                                            if leo[0] in bc:
                                                ind=bc.index(leo[0])
                                                sdr=bc[ind]
                                                bc[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bc[ind]=sdr
                                            elif leo[0] in bh:
                                                ind=bh.index(leo[0])
                                                sdr=bh[ind]
                                                bh[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bh[ind]=sdr   
                                            elif leo[0] in be:
                                                ind=be.index(leo[0])
                                                sdr=be[ind]
                                                be[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                be[ind]=sdr  
                                            elif leo[0] in bq:
                                                ind=bq.index(leo[0])
                                                sdr=bq[ind]
                                                bq[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bq[ind]=sdr
                                            elif leo[0] in bsl:
                                                ind=bsl.index(leo[0])
                                                sdr=bsl[ind]
                                                bsl[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bsl[ind]=sdr                                                
                                            elif leo[0] in bk:
                                                ind=bk.index(leo[0])
                                                sdr=bk[ind]
                                                bk[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bk[ind]=sdr
                                        if leo[1] in bsl + bh + bc + be + bk + bq:
                                            if leo[1] in bc:
                                                ind = bc.index(leo[1])
                                                sdr = bc[ind]
                                                bc[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bc[ind] = sdr
                                            elif leo[1] in bh:
                                                ind = bh.index(leo[1])
                                                sdr = bh[ind]
                                                bh[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bh[ind] = sdr   
                                            elif leo[1] in be:
                                                ind = be.index(leo[1])
                                                sdr = be[ind]
                                                be[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                be[ind] = sdr  
                                            elif leo[1] in bq:
                                                ind = bq.index(leo[1])
                                                sdr = bq[ind]
                                                bq[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bq[ind] = sdr
                                            elif leo[1] in bsl:
                                                ind = bsl.index(leo[1])
                                                sdr = bsl[ind]
                                                bsl[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bsl[ind] = sdr                                                
                                            elif leo[1] in bk:
                                                ind = bk.index(leo[1])
                                                sdr = bk[ind]
                                                bk[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bk[ind] = sdr

                                                                                         
                                        
                                   

                                        reachablebox=[i for i in reachablebox if i!=0]
                                        for i in reachablebox:
                                            drawrectfrompos(i)
                                            
                                       
                                        white_pointer=crstr
                                        
                                    elif crstr[1]!='0':
                                        leo=wgivesinglediagnol(crstr)
                                        drawrectfrompos(crstr)
                                        if leo[2] not in bsl+bh+wh+bc+wc+be+we+bk+wk+bq+wq+wsl:                                        
                                            reachablebox.extend([crstr[0]+str(int(crstr[1])-1)])
                                        



                                        i=0
                                        while i<len(reachablebox):
                                        
                                            pi=wsl.index(crstr)
                                            ant=wsl[pi]
                                            wsl[pi]=reachablebox[i]
                                            
                                            lpl=kalake()
                                            if wk[0] in lpl:
                                                
                                                reachablebox[i]=0

                                            wsl[pi]=ant
                                            i=i+1
                                          
                                            
                                        if leo[0] in bsl+bh+bc+be+bk+bq:
                                            if leo[0] in bc:
                                                ind=bc.index(leo[0])
                                                sdr=bc[ind]
                                                bc[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bc[ind]=sdr
                                            elif leo[0] in bh:
                                                ind=bh.index(leo[0])
                                                sdr=bh[ind]
                                                bh[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bh[ind]=sdr   
                                            elif leo[0] in be:
                                                ind=be.index(leo[0])
                                                sdr=be[ind]
                                                be[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                be[ind]=sdr  
                                            elif leo[0] in bq:
                                                ind=bq.index(leo[0])
                                                sdr=bq[ind]
                                                bq[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bq[ind]=sdr
                                            elif leo[0] in bsl:
                                                ind=bsl.index(leo[0])
                                                sdr=bsl[ind]
                                                bsl[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bsl[ind]=sdr                                                
                                            elif leo[0] in bk:
                                                ind=bk.index(leo[0])
                                                sdr=bk[ind]
                                                bk[ind]=0
                                                ind2=wsl.index(crstr)
                                                sdr2=wsl[ind2]
                                                wsl[ind2]=leo[0]
                                                bad=bbchecker(wk[0])
                                                if bad==0:
                                                    reachablebox.append(leo[0])
                                                wsl[ind2]=sdr2
                                                bk[ind]=sdr
                                        if leo[1] in bsl + bh + bc + be + bk + bq:
                                            if leo[1] in bc:
                                                ind = bc.index(leo[1])
                                                sdr = bc[ind]
                                                bc[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bc[ind] = sdr
                                            elif leo[1] in bh:
                                                ind = bh.index(leo[1])
                                                sdr = bh[ind]
                                                bh[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bh[ind] = sdr   
                                            elif leo[1] in be:
                                                ind = be.index(leo[1])
                                                sdr = be[ind]
                                                be[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                be[ind] = sdr  
                                            elif leo[1] in bq:
                                                ind = bq.index(leo[1])
                                                sdr = bq[ind]
                                                bq[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bq[ind] = sdr
                                            elif leo[1] in bsl:
                                                ind = bsl.index(leo[1])
                                                sdr = bsl[ind]
                                                bsl[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bsl[ind] = sdr                                                
                                            elif leo[1] in bk:
                                                ind = bk.index(leo[1])
                                                sdr = bk[ind]
                                                bk[ind] = 0
                                                ind2 = wsl.index(crstr)
                                                sdr2 = wsl[ind2]
                                                wsl[ind2] = leo[1]
                                                bad = bbchecker(wk[0])
                                                if bad == 0:
                                                    reachablebox.append(leo[1])
                                                wsl[ind2] = sdr2
                                                bk[ind] = sdr

                                                                          
                                   

                                        reachablebox=[i for i in reachablebox if i!=0]


                                        for i in reachablebox:
                                            drawrectfrompos(i)                                     

                                        white_pointer=crstr

                                else:
                                    for i in range(0, 8):
                                        for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    white_pointer=-1
                        elif crstr in wh:
                            found=1
                            if found==1:
                                
                                r=crstr
                                x=int(r[0])
                                y=int(r[1])
                                l=[STR(x-1,y-2),STR(x+1,y-2),STR(x-1,y+2),STR(x+1,y+2),STR(x-2,y-1),STR(x+2,y-1),STR(x-2,y+1),STR(x+2,y+1)]
                                l=[i for i in l if i!="-1"]
                                l=[i for i in l if int(i[0]) <= 7 and int(i[-1]) <= 7 and i not in wsl+wh+wc+we+wk+wq]    
                                reachablebox.extend(l)
                                i=0
                                while i<len(reachablebox):
                                
                                    pi=wh.index(crstr)
                                    ant=wh[pi]
                                    wh[pi]=reachablebox[i]
                                    
                                    lpl=kalake()
                                    if wk[0] in lpl:
                                        if reachablebox[i] not in bc+bq:
                                            reachablebox[i]=0

                                    wh[pi]=ant
                                    i=i+1  
                                reachablebox=[i for i in reachablebox if i!=0]                              
                                drawrectfrompos(r)
                                for i in reachablebox:
                                    drawrectfrompos(i)

                                white_pointer=crstr
                            else:
                                    for i in range(0, 8):
                                        for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    white_pointer=-1
                        elif crstr in wc:
                            found=1
                            r=crstr
                            x=int(crstr[0])
                            y=int(crstr[1])
                            r=STR(x,y)
                            r2=r
                            x2=x
                            y2=y
                            x3=x
                            y3=y
                            x4=x
                            y4=y
                            
                            while x>=0 and y>=0:
                                x=x-1
                                y=y-1
                                o1=STR(x,y)
                                if o1 in wsl+wc+wh+we+wk+wq:
                                    break
                                elif o1 in bsl+bc+bh+be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)
                            while x2<=7 and y2>=0:
                                x2=x2+1
                                y2=y2-1
                                o1=STR(x2,y2)
                                if o1 in wsl+wc+wh+we+wk+wq:
                                    break
                                elif o1 in bsl+bc+bh+be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)
                            while x3>=0 and y3<=7:
                                x3=x3-1
                                y3=y3+1
                                o1=STR(x3,y3)
                                if o1 in wsl+wc+wh+we+wk+wq:
                                    break
                                elif o1 in bsl+bc+bh+be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)
                            while x4<=7 and y4<=7:
                                x4=x4+1
                                y4=y4+1
                                o1=STR(x4,y4)
                                if o1 in wsl+wc+wh+we+wk+wq:
                                    break
                                elif o1 in bsl+bc+bh+be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1) 
                            i=0
                            while i<len(reachablebox):
                            
                                pi=wc.index(crstr)
                                ant=wc[pi]
                                wc[pi]=reachablebox[i]
                                
                                lpl=kalake()
                                if wk[0] in lpl:
                                    if reachablebox[i] not in bc+bq:
                                        reachablebox[i]=0

                                wc[pi]=ant
                                i=i+1
                            
                            reachablebox=[i for i in reachablebox if i!=0]        
                                                               
                            if found==1:
                                
                                drawrectfrompos(crstr)
                                reachablebox=[i for i in reachablebox if i!='-1']
                                for i in reachablebox:
                                    drawrectfrompos(i)

                                white_pointer=crstr
                            else:
                                for i in range(0, 8):
                                    for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    white_pointer=-1                                    
                        elif crstr in we:
                            found=1
                            x=int(crstr[0])
                            y=int(crstr[1])
                            x2=x
                            y2=y
                            x3=x
                            y3=y
                            x4=x
                            y4=y
                            while y<=7:
                                y=y+1
                                q=STR(x,y)
                                if q in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q)
                                    break
                                else:
                                    reachablebox.append(q)
                            while y2>=0:
                                y2=y2-1
                                q2=STR(x2,y2)
                                if q2 in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q2 in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q2)
                                    break
                                else:
                                    reachablebox.append(q2)
                            while x3>=0:
                                x3=x3-1
                                q3=STR(x3,y3)
                                if q3 in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q3 in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q3)
                                    break
                                else:
                                    reachablebox.append(q3)
                            while x4<=7:
                                x4=x4+1
                                q4=STR(x4,y4)
                                if q4 in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q4 in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q4)
                                    break
                                else:
                                    reachablebox.append(q4)


                            i=0
                            while i<len(reachablebox):
                                
                                pi=we.index(crstr)
                                ant=we[pi]
                                we[pi]=reachablebox[i]
                                
                                lpl=kalake()
                                if wk[0] in lpl:
                                    if reachablebox[i] not in be+bq:                             
                                        reachablebox[i]=0

                                we[pi]=ant
                                i=i+1
                        

                            reachablebox=[i for i in reachablebox if i!=0]                                    
                            if found==1:
                                
                                drawrectfrompos(crstr)
                                reachablebox=[i for i in reachablebox if i!='-1']

                                for i in reachablebox:
                                    drawrectfrompos(i)

                                white_pointer=crstr
                            else:
                                for i in range(0, 8):
                                    for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    white_pointer=-1                                  
                        elif crstr in wq:
                            found=1
                            x=int(crstr[0])
                            y=int(crstr[1])
                            x2=x
                            y2=y
                            x3=x
                            y3=y
                            x4=x
                            y4=y
                            while y<=7:
                                y=y+1
                                q=STR(x,y)
                                if q in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q)
                                    break
                                else:
                                    reachablebox.append(q)
                            while y2>=0:
                                y2=y2-1
                                q2=STR(x2,y2)
                                if q2 in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q2 in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q2)
                                    break
                                else:
                                    reachablebox.append(q2)
                            while x3>=0:
                                x3=x3-1
                                q3=STR(x3,y3)
                                if q3 in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q3 in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q3)
                                    break
                                else:
                                    reachablebox.append(q3)
                            while x4<=7:
                                x4=x4+1
                                q4=STR(x4,y4)
                                if q4 in wc+wh+wsl+we+wk+wq:
                                    break
                                elif q4 in bc+bh+bsl+be+bk+bq:
                                    reachablebox.append(q4)
                                    break
                                else:
                                    reachablebox.append(q4)
                            # Assuming crstr is a list with at least two elements
                            x = int(crstr[0])
                            y = int(crstr[1])
                            r = STR(x, y)
                            r2 = r
                            x_positive_diagonal = x
                            y_positive_diagonal = y
                            x_negative_diagonal = x
                            y_negative_diagonal = y
                            x_horizontal_right = x
                            y_horizontal_right = y
                            x_horizontal_left = x
                            y_horizontal_left = y

                            while x_positive_diagonal >= 0 and y_positive_diagonal >= 0:
                                x_positive_diagonal -= 1
                                y_positive_diagonal -= 1
                                o1 = STR(x_positive_diagonal, y_positive_diagonal)
                                if o1 in wsl + wc + wh + we+wk+wq:
                                    break
                                elif o1 in bsl + bc + bh + be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)

                            while x_horizontal_right <= 7 and y_horizontal_right >= 0:
                                x_horizontal_right += 1
                                y_horizontal_right -= 1
                                o1 = STR(x_horizontal_right, y_horizontal_right)
                                if o1 in wsl + wc + wh + we + wk+wq:
                                    break
                                elif o1 in bsl + bc + bh + be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)

                            while x_negative_diagonal >= 0 and y_negative_diagonal <= 7:
                                x_negative_diagonal -= 1
                                y_negative_diagonal += 1
                                o1 = STR(x_negative_diagonal, y_negative_diagonal)
                                if o1 in wsl + wc + wh + we+wk+wq:
                                    break
                                elif o1 in bsl + bc + bh + be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)

                            while x_horizontal_left <= 7 and y_horizontal_left <= 7:
                                x_horizontal_left += 1
                                y_horizontal_left += 1
                                o1 = STR(x_horizontal_left, y_horizontal_left)
                                if o1 in wsl + wc + wh + we+wk+wq:
                                    break
                                elif o1 in bsl + bc + bh + be+bk+bq:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)
                            i=0
                            while i<len(reachablebox):
                            
                                pi=wq.index(crstr)
                                ant=wq[pi]
                                wq[pi]=reachablebox[i]
                                
                                lpl=kalake()
                                if wk[0] in lpl:
                                    if reachablebox[i] not in bc+bq+be:
                                        reachablebox[i]=0

                                wq[pi]=ant
                                i=i+1
                            
                            reachablebox=[i for i in reachablebox if i!=0]                                     
                                                                
                            if found==1:
                                
                                drawrectfrompos(crstr)
                                reachablebox=[i for i in reachablebox if i!='-1']

                                for i in reachablebox:
                                    drawrectfrompos(i)

                                white_pointer=crstr
                            else:
                                for i in range(0, 8):
                                    for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    white_pointer=-1                                 
                        elif crstr in wk:
                            found=1
                            x=int(crstr[0])
                            y=int(crstr[1])

                            l=[STR(x-1,y-1),STR(x,y-1),STR(x+1,y-1),STR(x-1,y),STR(x+1,y),STR(x-1,y+1),STR(x,y+1),STR(x+1,y+1)]
                            l=[i for i in l if i not in wsl+wh+we+wq+wc]
                            l=[i for i in l if i!='-1']
                            reachablebox.extend(l)
                            livi=kalake()
                            
                            for o in reachablebox:
                                smn=checkbpower(o)
                                if smn==3:
                                    h=bh.index(o)
                                    faz=bh[h]
                                    bh[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        reachablebox.remove(o)
                                    bh[h]=faz
                                elif smn==2:
                                    h=bc.index(o)
                                    faz=bc[h]
                                    bc[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        reachablebox.remove(o)
                                    bc[h]=faz
                                elif smn==4:
                                    h=be.index(o)
                                    faz=be[h]
                                    be[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        reachablebox.remove(o)
                                    be[h]=faz                                    
                                elif smn==5:
                                    h=bq.index(o)
                                    faz=bq[h]
                                    bq[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        reachablebox.remove(o)
                                    bq[h]=faz                                
                                elif smn==1:
                                    h=bsl.index(o)
                                    faz=bsl[h]
                                    bsl[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        reachablebox.remove(o)
                                    bsl[h]=faz   

                                for i in be:
                                    j=belephantreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)

                                for i in bc:
                                    j=bcamelreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)                                        

                                for i in bh:
                                    j=bhorsereach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)  

                                for i in bk:
                                    j=bkingreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k) 
                                for i in bq:
                                    j=bcamelreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)
                                    j2=belephantreach(i)                                              
                                    for k in j2:
                                        if k in reachablebox:
                                            reachablebox.remove(k)                            
                            if wlcastlepossible==1:
                                reachablebox.append("07")
                            if wrcastlepossible==1:
                                reachablebox.append("77")
                            if found==1:
                                
                                drawrectfrompos(crstr)
                                reachablebox=[i for i in reachablebox if i!='-1']

                                for i in reachablebox:
                                    drawrectfrompos(i)

                                white_pointer=crstr
                            else:
                                for i in range(0, 8):
                                    for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    white_pointer=-1                               
            elif bcheck==1:
                found=0
                pandit=0
                asuran=wcheckedby[-1]
                possiblemoves={} #This is to find which can attack
                for i in wd:
                    if i not in wk:
                        l=wd[i]
                        for j in l:
                            if j==asuran:
                                possiblemoves[i]=[j]
                #This is to find which can block
                for i in wdwos:
                    if i not in wk:
                        l=wdwos[i]
                        
                        for j in l:
                            if int(j)>0 and j!='-1':
                                iw.append(j)
                                g=bchecker()
                                if g==0:
                                    if i not in possiblemoves:
                                        possiblemoves[i]=[j]
                                    else:
                                        possiblemoves[i].append(j)
                                iw=[]
                
                dust=wjf()

                for i in dust:
                    l=dust[i]
                    
                    for j in l:
                        if int(j)>=0 and j!='-1':
                            iw.append(j)
                            g=bchecker()
                            if g==0:
                                possiblemoves[i]=[j]
                            iw=[]    
                d=wk[0]
                dr=wkingreach(d)

                for i in dr:
                    ntr=wk[0]
                    wk[0]=i
                    g=bchecker()
                    if g==0:
                        if ntr not in possiblemoves:
                            possiblemoves[ntr]=[i]
                        else:
                            possiblemoves[ntr].append(i)

                    wk[0]=ntr

                if wk[0] in possiblemoves:
                    
                            for o in possiblemoves[wk[0]]:
                                smn=checkbpower(o)
                                if smn==3:
                                    h=bh.index(o)
                                    faz=bh[h]
                                    bh[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        possiblemoves[wk[0]].remove(o)
                                    bh[h]=faz
                                elif smn==2:
                                    h=bc.index(o)
                                    faz=bc[h]
                                    bc[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        possiblemoves[wk[0]].remove(o)
                                    bc[h]=faz
                                elif smn==4:
                                    h=be.index(o)
                                    faz=be[h]
                                    be[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        possiblemoves[wk[0]].remove(o)
                                    be[h]=faz                                    
                                elif smn==5:
                                    h=bq.index(o)
                                    faz=bq[h]
                                    bq[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        possiblemoves[wk[0]].remove(o)
                                    bq[h]=faz                                
                                elif smn==1:
                                    h=bsl.index(o)
                                    faz=bsl[h]
                                    bsl[h]=0

                                    ops=bbchecker(o)
                                    if ops==1:
                                        possiblemoves[wk[0]].remove(o)
                                    bsl[h]=faz   
                
                for i in possiblemoves:
                    if possiblemoves[i]!=[]:
                        pandit=pandit+1

                if pandit==0:
                    wpl=[]
                    bpl=[]
                    ws=[]
                    bs=[]
                    
                    turn=2
                    t=pygame.font.SysFont('calibri',48)
                    r1=t.render("BLACK WINS",True,black)
                    r11=r1.get_rect()
                    r11.center=(1000,50)
                    ds.blit(r1,r11)
                                                     
                if white_pointer!=-1:
                    if event.type==pygame.MOUSEBUTTONDOWN:

                        ucrstr1=ucrstr
                        uc1=event.pos[0]
                        uc2=event.pos[1]
                        uc=[uc1,uc2]
                        ucr=boxonclicktocr(uc)
                        ucrstr2=str(ucr[0])+str(ucr[1]) 
    

                        if ucrstr2 not in reachableboxc:
                            for i in range(0, 8):
                                for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                            white_pointer=-1
                        else:
                            if ucrstr1 in wsl:
                                try:
                                    ind = wsl.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop
                                wsl.remove(ucrstr1)
                                
                                wsl.insert(ind, ucrstr2)

                                # Update ws list
                                ws[ind][1].center = fromcrtocenter(ucrstr2)
                                if ucrstr2 in bsl:
                                    ind2=bsl.index(ucrstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif ucrstr2 in bh:
                                    ii=bh.index(ucrstr2)
                                    bh[ii]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif ucrstr2 in bc:
                                    ii=bc.index(ucrstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']  
                                elif ucrstr2 in be:
                                    ii=be.index(ucrstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']                                                                                                    
                                elif ucrstr2 in bq:
                                    ii=bq.index(ucrstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']                            

                                else:                                
                                    ips=bchecker()
                                    if ips==1:
                                        wsl.remove(ucrstr2)
                                        wsl.insert(ind,ucrstr1)
                                        
                                        ws[ind][1].center=fromcrtocenter(ucrstr1)
                                        white_pointer=-1
                                        bcheck=0
                                        turn=1                                
                            elif ucrstr1 in wh:
                                lak=[i for i in wpl if i[2]=="h"]

                                try:
                                    ind = wh.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                wh[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)


                                if ucrstr2 in bsl:
                                    ind2=bsl.index(ucrstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif ucrstr2 in bh:
                                    ind=bh.index(ucrstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h']
                                elif ucrstr2 in bc:
                                    ii=bc.index(ucrstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']  
                                elif ucrstr2 in be:
                                    ii=be.index(ucrstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']    
                                elif ucrstr2 in bq:
                                    ii=bq.index(ucrstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']  
                                else:
                                    ips=bchecker()
                                    if ips==1:
                                        lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                        wh[ind]=ucrstr1
                                        white_pointer=-1
                                        bcheck=0
                                        turn=1                                                                                                                                                         
                            elif ucrstr1 in wc:
                                lak=[i for i in wpl if i[2]=="c"]

                                try:
                                    ind = wc.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                wc[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)       
                     
                                if ucrstr2 in bsl:
                                    ind2=bsl.index(ucrstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif ucrstr2 in bh:
                                    ind=bh.index(ucrstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif ucrstr2 in bc:
                                    ii=bc.index(ucrstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']
                                elif ucrstr2 in be:
                                    ii=be.index(ucrstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']  
                                elif ucrstr2 in bq:
                                    ii=bq.index(ucrstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']   
                                else:
                                    ips=bchecker()
                                    if ips==1:
                                        lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                        wc[ind]=ucrstr1
                                        white_pointer=-1
                                        bcheck=0
                                        turn=1                                                                                                                                                                 
                            elif ucrstr1 in wq:
                                lak=[i for i in wpl if i[2]=="q"]

                                try:
                                    ind = wq.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  

                                wq[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)   
                                                            
                                if ucrstr2 in bsl:
                                    ind2=bsl.index(ucrstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif ucrstr2 in bh:
                                    ind=bh.index(ucrstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif ucrstr2 in bc:
                                    ii=bc.index(ucrstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']
                                elif ucrstr2 in be:
                                    ii=be.index(ucrstr2)
                                    be[ii]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']  
                                elif ucrstr2 in bq:
                                    ii=bq.index(ucrstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q']   
                                else:
                                    ips=bchecker()
                                    if ips==1:
                                        lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                        wq[ind]=ucrstr1
                                        white_pointer=-1
                                        bcheck=0
                                        turn=1  
                            elif ucrstr1 in wk:
                                    lak=[i for i in wpl if i[2]=="k"]

                                    try:
                                        ind = wk.index(ucrstr1)
                                    except ValueError:
                                        # Handle the case where ucrstr1 is not found in wsl
                                        print("Error: ucrstr1 not found in wsl.")
                                        continue  # Skip the rest of the loop  
                                    wk[ind]=ucrstr2
                                    lak[ind][1].center = fromcrtocenter(ucrstr2) 
                                    ips=bchecker()
                                    if ips==1:
                                        lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                        wk[ind]=ucrstr1
                                        white_pointer=-1
                                        turn=1                                                            
                                    if ucrstr2 in bsl:
                                        ind2=bsl.index(ucrstr2)
                                        bs[ind2]=[0,0]
                                        bsl[ind2]=0
                                    elif ucrstr2 in bh:
                                        ind=bh.index(ucrstr2)
                                        jatka1=bh[ind]
                                        bh[ind]=0
                                        mo=[i for i in bpl if i[2]=="h"]
                                        illa=mo[ind]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            jatka2=bpl[inde]
                                            bpl[inde]=[0,0,'h'] 
                                        ips=bchecker()
                                        if ips==1:
                                            lak[ind][1].center=fromcrtocenter(ucrstr1)                                                                           
                                            wk[ind]=ucrstr1
                                            white_pointer=-1
                                            turn=1  
                                            bh[ind]=jatka1
                                            bpl[inde]=jatka2                                         
                                    elif ucrstr2 in bc:
                                        ii=bc.index(ucrstr2)
                                        jatka1=bc[ii]
                                        bc[ii]=0
                                        mo=[i for i in bpl if i[2]=="c"]
                                        illa=mo[ii]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            jatka2=bpl[inde]
                                            bpl[inde]=[0,0,'c']
                                        ips=bchecker()
                                        if ips==1:
                                            lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                            wk[ind]=ucrstr1
                                            white_pointer=-1
                                            turn=1  
                                            bh[ind]=jatka1
                                            bpl[inde]=jatka2                                         
                                    elif ucrstr2 in be:
                                        ii=be.index(ucrstr2)
                                        jatka1=bh[ii]
                                        be[ii]=0
                                        mo=[i for i in bpl if i[2]=="e"]
                                        illa=mo[ii]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            jatka2=bpl[inde]
                                            bpl[inde]=[0,0,'e']  
                                        ips=bchecker()
                                        if ips==1:
                                            lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                            wk[ind]=ucrstr1
                                            white_pointer=-1
                                            turn=1  
                                            bh[ind]=jatka1
                                            bpl[inde]=jatka2                                          
                                    elif ucrstr2 in bq:
                                        ii=bq.index(ucrstr2)
                                        jatka1=bq[ii]
                                        bq[ii]=0
                                        jatka2=[]
                                        mo=[i for i in bpl if i[2]=="q"]
                                        illa=mo[ii]
                                        if illa in bpl:
                                            inde=bpl.index(illa)
                                            jatka2=bpl[inde]
                                            bpl[inde]=[0,0,'q'] 
                                        ips=bchecker()
                                        if ips==1:
                                            lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                            wk[ind]=ucrstr1
                                            white_pointer=-1
                                            bcheck=1
                                            turn=1  
                                            bh[ind]=jatka1
                                            bpl[inde]=jatka2
                                         
                            elif ucrstr1 in we:    
                                lak=[i for i in wpl if i[2]=="e"]

                                try:
                                    ind = we.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                we[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)   
                          
                                if ucrstr2 in bsl:
                                    ind2=bsl.index(ucrstr2)
                                    bs[ind2]=[0,0]
                                    bsl[ind2]=0
                                elif ucrstr2 in bh:
                                    ind=bh.index(ucrstr2)
                                    bh[ind]=0
                                    mo=[i for i in bpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'h'] 
                                elif ucrstr2 in bc:
                                    ii=bc.index(ucrstr2)
                                    bc[ii]=0
                                    mo=[i for i in bpl if i[2]=="c"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'c']   
                                elif ucrstr2 in be:
                                    iei=be.index(ucrstr2)
                                    be[iei]=0
                                    mo=[i for i in bpl if i[2]=="e"]
                                    illa=mo[iei]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'e']   
                                elif ucrstr2 in bq:
                                    ii=bq.index(ucrstr2)
                                    bq[ii]=0
                                    mo=[i for i in bpl if i[2]=="q"]
                                    illa=mo[ii]
                                    if illa in bpl:
                                        inde=bpl.index(illa)
                                        bpl[inde]=[0,0,'q'] 
                                else:
                                    ips=bchecker()
                                    if ips==1:
                                        lak[ind][1].center=fromcrtocenter(ucrstr1)                                    
                                        we[ind]=ucrstr1
                                        white_pointer=-1
                                        bcheck=0
                                        turn=1                                                                                                                                             
                            for i in range(0, 8):
                                for j in range(0, 8):
                                    i1 = 100 * i
                                    j1 = 100 * j
                                    if (i + j) % 2 == 0:
                                        pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                    else:
                                        pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                            turn=0


            
                            white_pointer=-1 
                else:   
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        reachableboxc=[]

                        u1=event.pos[0]
                        u2=event.pos[1]
                        u=[u1,u2]
                        ur=boxonclicktocr(u)
                        ucrstr=str(ur[0])+str(ur[1])       
                        if ucrstr in possiblemoves:
                            found=1
                            drawrectfrompos(ucrstr)
                            reachableboxc.extend(possiblemoves[ucrstr])
                            if found==1:
                                

                                for i in reachableboxc:
                                    drawrectfrompos(i) 
                                white_pointer=ucrstr 
                            else:

                                for i in range(0, 8):
                                    for j in range(0, 8):
                                        i1 = 100 * i
                                        j1 = 100 * j
                                        if (i + j) % 2 == 0:
                                            pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                        else:
                                            pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                white_pointer=-1                                                                   

        elif turn==0:
            if wcheck==0:
                if black_pointer != -1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        crstr1 = crstr
                        c1 = event.pos[0]
                        c2 = event.pos[1]
                        c = [c1, c2]
                        cr = boxonclicktocr(c)
                        crstr2 = str(cr[0]) + str(cr[1])

                        if crstr2 not in reachablebox:
                            for i in range(0, 8):
                                for j in range(0, 8):
                                    i1 = 100 * i
                                    j1 = 100 * j
                                    if (i + j) % 2 == 0:
                                        pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                    else:
                                        pygame.draw.rect(ds, green, (i1, j1, 100, 100))

                        else:
                            if crstr in bsl:
                                try:
                                    ind = bsl.index(crstr1)
                                except ValueError:
                                    print("Error: crstr1 not found in bsl.")
                                    continue

                                bsl.remove(crstr1)
                                bsl.insert(ind, crstr2)
                                if crstr2 in wsl:
                                    bii=wsl.index(crstr2)
                                    wsl[bii]=0
                                    ws[bii]=[0,0]
                                elif crstr2 in wh:
                                    ii=wh.index(crstr2)
                                    wh[ii]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ii]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                              
                                elif crstr2 in wc:
                                    ic=wc.index(crstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c'] 
                                elif crstr2 in we:
                                    ic=we.index(crstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e']    
                                elif crstr2 in wq:
                                    ic=wq.index(crstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                          
                                bs[ind][1].center = fromcrtocenter(crstr2)
                                leo=bgivesinglediagnol(crstr2)
                                leo.pop()
                                if wk[0] in leo:
                                    wcheckedby.append(crstr2)
                                if crstr2[1]=='7':
                                    sos=bsl.index(crstr2)
                                    
                                    bsl[sos]=0     
                                    bs[sos]=[0,0] 
                                    t=pygame.font.SysFont('calibri',48)
                                    r1=t.render("SELECT",True,black)
                                    r11=r1.get_rect()
                                    r11.center=(1000,50)
                                    i1=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bwrook.png")
                                    i11=i1.get_rect()
                                    i11.center=(850,150)
                                    i2=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bstrategy.png")
                                    i22=i2.get_rect()
                                    i22.center=(950,150)
                                    i3=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bbishop.png")
                                    i33=i3.get_rect()
                                    i33.center=(1050,150)
                                    i4=pygame.image.load("C:/Users/datta/OneDrive/Desktop/Images game/New folder/bqueen.png")
                                    i44=i4.get_rect()
                                    i44.center=(1150,150)
                                    drawrectfrompos("81")
                                    drawrectfrompos("91")
                                    pygame.draw.rect(ds,black,(1000,100,100,100),5)
                                    pygame.draw.rect(ds,black,(1100,100,100,100),5)
                                    
                                    ds.blit(r1,r11)
                                    ds.blit(i1,i11)
                                    ds.blit(i2,i22)
                                    ds.blit(i3,i33)
                                    ds.blit(i4,i44)  
                                    blackshown=1   
                                    markblack=crstr2  
                                else:
                                    blackshown=0                                     
                            elif crstr in bh:
                                lak=[i for i in bpl if i[2]=="h"]

                                try:
                                    ind = bh.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bh[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2) 
                                lai=bhorsereach(crstr2)
                                if wk[0] in lai:
                                    wcheckedby.append(crstr2)
                                    

                                if crstr2 in wsl:
                                    ind2=wsl.index(crstr2)
                                    ws[ind2]=[0,0]          
                                    wsl[ind2]=0 
                                elif crstr2 in wh:
                                    ind=wh.index(crstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif crstr2 in wc:
                                    ic=wc.index(crstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c'] 
                                elif crstr2 in we:
                                    ic=we.index(crstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e']  
                                elif crstr2 in wq:
                                    ic=wq.index(crstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                           
                            elif crstr1 in bc:
                                lak=[i for i in bpl if i[2]=="c"]

                                try:
                                    ind = bc.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bc[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2)   
                                lai=bcamelreach(crstr2)
                                if wk[0] in lai:
                                    wcheckedby.append(crstr2)                                                   
                                if crstr2 in wsl:
                                    ind2=wsl.index(crstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif crstr2 in wh:
                                    ind=wh.index(crstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif crstr2 in wc:
                                    ic=wc.index(crstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c']  
                                elif crstr2 in we:
                                    ic=we.index(crstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif crstr2 in wq:
                                    ic=wq.index(crstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                                                               
                            elif crstr1 in bq:
                                lak=[i for i in bpl if i[2]=="q"]

                                try:
                                    ind = bq.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bq[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2)
                                lai=bcamelreach(crstr2)
                                lai2=belephantreach(crstr2)
                                if wk[0] in lai+lai2:
                                    wcheckedby.append(crstr2)
                                                        
                                if crstr2 in wsl:
                                    ind2=wsl.index(crstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif crstr2 in wh:
                                    ind=wh.index(crstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif crstr2 in wc:
                                    ic=wc.index(crstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c']  
                                elif crstr2 in we:
                                    ic=we.index(crstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif crstr2 in wq:
                                    ic=wq.index(crstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q'] 
                            elif crstr1 in bk:
                                if crstr2 not in be:
                                    lak=[i for i in bpl if i[2]=="k"]

                                    try:
                                        ind = bk.index(crstr1)
                                    except ValueError:
                                        # Handle the case where crstr1 is not found in wsl
                                        print("Error: crstr1 not found in wsl.")
                                        continue  # Skip the rest of the loop  
                                    bk[ind]=crstr2
                                    lak[ind][1].center = fromcrtocenter(crstr2)      
                                    bkingmoved=1                    
                                    if crstr2 in wsl:
                                        ind2=wsl.index(crstr2)
                                        ws[ind2]=[0,0]
                                        wsl[ind2]=0
                                    elif crstr2 in wh:
                                        ind=wh.index(crstr2)
                                        wh[ind]=0
                                        mo=[i for i in wpl if i[2]=="h"]
                                        illa=mo[ind]
                                        if illa in wpl:
                                            inde=wpl.index(illa)
                                            wpl[inde]=[0,0,'h']                 
                                    elif crstr2 in wc:
                                        ic=wc.index(crstr2)
                                        wc[ic]=0
                                        mo=[i for i in wpl if i[2]=="c"]
                                        illa=mo[ic]
                                        if illa in wpl:
                                            inde=wpl.index(illa)
                                            wpl[inde]=[0,0,'c']  
                                    elif crstr2 in we:
                                        ic=we.index(crstr2)
                                        we[ic]=0
                                        mo=[i for i in wpl if i[2]=="e"]
                                        illa=mo[ic]
                                        if illa in wpl:
                                            inde=wpl.index(illa)
                                            wpl[inde]=[0,0,'e'] 
                                    elif crstr2 in wq:
                                        ic=wq.index(crstr2)
                                        wq[ic]=0
                                        mo=[i for i in wpl if i[2]=="q"]
                                        illa=mo[ic]
                                        if illa in wpl:
                                            inde=wpl.index(illa)
                                            wpl[inde]=[0,0,'q'] 
                                else:
                                    lak=[i for i in bpl if i[2]=="k"]

                                    try:
                                        ind = bk.index(crstr1)
                                    except ValueError:
                                        # Handle the case where crstr1 is not found in wsl
                                        print("Error: crstr1 not found in wsl.")
                                        continue  # Skip the rest of the loop  
                                    laka=[i for i in bpl if i[2]=="e"]
                                    
                                    if crstr2=="00":
                                        bk[ind]="10"
                                        lak[ind][1].center = fromcrtocenter("10")  
                                        be[0]="20"
                                        laka[0][1].center=fromcrtocenter("20")       
                                    elif crstr2=="70":
                                        bk[ind]="60"
                                        lak[ind][1].center = fromcrtocenter("60")  
                                        be[1]="50"
                                        laka[1][1].center=fromcrtocenter("50")                                                                           
                            elif crstr1 in be:
                                lak=[i for i in bpl if i[2]=="e"]

                                try:
                                    ind = be.index(crstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                be[ind]=crstr2
                                lak[ind][1].center = fromcrtocenter(crstr2) 
                                lai=belephantreach(crstr2)
                                if ind==0:
                                    blrook=1
                                elif ind==1:
                                    brrook=1
                                if wk[0] in lai:
                                    wcheckedby.append(crstr2)                         
                                if crstr2 in wsl:
                                    ind2=wsl.index(crstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif crstr2 in wh:
                                    ind=wh.index(crstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif crstr2 in wc:
                                    ic=wc.index(crstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c'] 
                                elif crstr2 in we:
                                    ic=we.index(crstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif crstr2 in wq:
                                    ic=wq.index(crstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                          
                            for i in range(0, 8):
                                for j in range(0, 8):
                                    i1 = 100 * i
                                    j1 = 100 * j
                                    if (i + j) % 2 == 0:
                                        pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                    else:
                                        pygame.draw.rect(ds, green, (i1, j1, 100, 100))

                            turn = 1

                        black_pointer = -1

                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        reachablebox = []

                        c1 = event.pos[0]
                        c2 = event.pos[1]
                        c = [c1, c2]
                        cr = boxonclicktocr(c)
                        crstr = str(cr[0]) + str(cr[1])

                        found = 0
                        selected = 0

                        if crstr in bsl:
                            found = 1

                            if found == 1:
                                    if black_pointer==-1:
                                        if crstr[1]=='1':
                                            leo=bgivesinglediagnol(crstr)
                                            drawrectfrompos(crstr)
                                            if leo[2] not in bsl+bh+wh+wsl+bc+wc+be+we+bk+wk+bq+wq:
                                                
                                                reachablebox.append(crstr[0]+str(int(crstr[1])+1))
                                                if bgivesinglediagnol(leo[2])[2] not in bsl+bh+wh+wsl+bc+wc+be+we+bk+wk+bq+wq:
                                                    
                                                    reachablebox.append(crstr[0]+str(int(crstr[1])+2))
                                            

                                            i=0
                                            while i<len(reachablebox):
                                            
                                                pi=bsl.index(crstr)
                                                ant=bsl[pi]
                                                bsl[pi]=reachablebox[i]
                                                
                                                lpl2=bkalake()
                                                if bk[0] in lpl2:
                                                    
                                                    reachablebox[i]=0

                                                bsl[pi]=ant
                                                i=i+1
                                            if leo[0] in wsl + wh + wc + we + wk + wq:
                                                if leo[0] in wc:
                                                    ind = wc.index(leo[0])
                                                    sdr = wc[ind]
                                                    wc[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wc[ind] = sdr
                                                elif leo[0] in wh:
                                                    ind = wh.index(leo[0])
                                                    sdr = wh[ind]
                                                    wh[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wh[ind] = sdr   
                                                elif leo[0] in we:
                                                    ind = we.index(leo[0])
                                                    sdr = we[ind]
                                                    we[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    we[ind] = sdr  
                                                elif leo[0] in wq:
                                                    ind = wq.index(leo[0])
                                                    sdr = wq[ind]
                                                    wq[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wq[ind] = sdr
                                                elif leo[0] in wsl:
                                                    ind = wsl.index(leo[0])
                                                    sdr = wsl[ind]
                                                    wsl[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wsl[ind] = sdr                                                
                                                elif leo[0] in wk:
                                                    ind = wk.index(leo[0])
                                                    sdr = wk[ind]
                                                    wk[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wk[ind] = sdr

                                                
                                                
                                            if leo[1] in wsl + wh + wc + we + wk + wq:
                                                if leo[1] in wc:
                                                    ind = wc.index(leo[1])
                                                    sdr = wc[ind]
                                                    wc[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wc[ind] = sdr
                                                elif leo[1] in wh:
                                                    ind = wh.index(leo[1])
                                                    sdr = wh[ind]
                                                    wh[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wh[ind] = sdr   
                                                elif leo[1] in we:
                                                    ind = we.index(leo[1])
                                                    sdr = we[ind]
                                                    we[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    we[ind] = sdr  
                                                elif leo[1] in wq:
                                                    ind = wq.index(leo[1])
                                                    sdr = wq[ind]
                                                    wq[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wq[ind] = sdr
                                                elif leo[1] in wsl:
                                                    ind = wsl.index(leo[1])
                                                    sdr = wsl[ind]
                                                    wsl[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wsl[ind] = sdr                                                
                                                elif leo[1] in wk:
                                                    ind = wk.index(leo[1])
                                                    sdr = wk[ind]
                                                    wk[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wk[ind] = sdr
                                                
                                    

                                            reachablebox=[i for i in reachablebox if i!=0]                                                
                                            for i in reachablebox:
                                                drawrectfrompos(i)                                            
                                            black_pointer=crstr
                                            
                                        elif crstr[1]!='7':
                                            leo=bgivesinglediagnol(crstr)
                                            drawrectfrompos(crstr)
                                            if leo[2] not in bsl+bh+wh+wsl+bc+wc+be+we+bk+wk+bq+wq:                                        
                                                reachablebox.extend([crstr[0]+str(int(crstr[1])+1)])
                                            

                                            i=0    
                                            while i<len(reachablebox):
                                            
                                                pi=bsl.index(crstr)
                                                ant=bsl[pi]
                                                bsl[pi]=reachablebox[i]
                                                
                                                lpl2=bkalake()
                                                if bk[0] in lpl2:
                                                    
                                                    reachablebox[i]=0

                                                bsl[pi]=ant
                                                i=i+1
                                            if leo[0] in wsl + wh + wc + we + wk + wq:
                                                if leo[0] in wc:
                                                    ind = wc.index(leo[0])
                                                    sdr = wc[ind]
                                                    wc[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wc[ind] = sdr
                                                elif leo[0] in wh:
                                                    ind = wh.index(leo[0])
                                                    sdr = wh[ind]
                                                    wh[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wh[ind] = sdr   
                                                elif leo[0] in we:
                                                    ind = we.index(leo[0])
                                                    sdr = we[ind]
                                                    we[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    we[ind] = sdr  
                                                elif leo[0] in wq:
                                                    ind = wq.index(leo[0])
                                                    sdr = wq[ind]
                                                    wq[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wq[ind] = sdr
                                                elif leo[0] in wsl:
                                                    ind = wsl.index(leo[0])
                                                    sdr = wsl[ind]
                                                    wsl[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wsl[ind] = sdr                                                
                                                elif leo[0] in wk:
                                                    ind = wk.index(leo[0])
                                                    sdr = wk[ind]
                                                    wk[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[0]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[0])
                                                    bsl[ind2] = sdr2
                                                    wk[ind] = sdr

                                                
                                                
                                            if leo[1] in wsl + wh + wc + we + wk + wq:
                                                if leo[1] in wc:
                                                    ind = wc.index(leo[1])
                                                    sdr = wc[ind]
                                                    wc[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wc[ind] = sdr
                                                elif leo[1] in wh:
                                                    ind = wh.index(leo[1])
                                                    sdr = wh[ind]
                                                    wh[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wh[ind] = sdr   
                                                elif leo[1] in we:
                                                    ind = we.index(leo[1])
                                                    sdr = we[ind]
                                                    we[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    we[ind] = sdr  
                                                elif leo[1] in wq:
                                                    ind = wq.index(leo[1])
                                                    sdr = wq[ind]
                                                    wq[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wq[ind] = sdr
                                                elif leo[1] in wsl:
                                                    ind = wsl.index(leo[1])
                                                    sdr = wsl[ind]
                                                    wsl[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wsl[ind] = sdr                                                
                                                elif leo[1] in wk:
                                                    ind = wk.index(leo[1])
                                                    sdr = wk[ind]
                                                    wk[ind] = 0
                                                    ind2 = bsl.index(crstr)
                                                    sdr2 = bsl[ind2]
                                                    bsl[ind2] = leo[1]
                                                    bad = wwchecker(bk[0])
                                                    if bad == 0:
                                                        reachablebox.append(leo[1])
                                                    bsl[ind2] = sdr2
                                                    wk[ind] = sdr
                                                
                                    

                                            reachablebox=[i for i in reachablebox if i!=0]  
                                            for i in reachablebox:
                                                drawrectfrompos(i)                                                
                                            black_pointer=crstr
                                    else:
                                        for i in range(0, 8):
                                            for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                        black_pointer=-1
                        elif crstr in bh:  
                                found=1
                                if found==1:
                                    r=crstr
                                    x=int(r[0])
                                    y=int(r[1])
                                    l=[STR(x-1,y-2),STR(x+1,y-2),STR(x-1,y+2),STR(x+1,y+2),STR(x-2,y-1),STR(x+2,y-1),STR(x-2,y+1),STR(x+2,y+1)]
                                    l=[i for i in l if i!="-1"]
                                    l=[i for i in l if int(i[0]) <= 7 and int(i[-1]) <= 7 and i not in bsl+bh+bk+bq+be+bc]    
                                    reachablebox.extend(l)
                                    drawrectfrompos(r)
                                    i=0
                                    while i<len(reachablebox):
                                    
                                        pi=bh.index(crstr)
                                        ant=bh[pi]
                                        bh[pi]=reachablebox[i]
                                        
                                        lpl2=bkalake()
                                        if bk[0] in lpl2:
                                            if reachablebox[i] not in wc+wq:
                                                reachablebox[i]=0

                                        bh[pi]=ant
                                        i=i+1  
                                    reachablebox=[i for i in reachablebox if i!=0]                                     
                                    for i in reachablebox:
                                        drawrectfrompos(i)
                                    black_pointer=crstr
                                else:
                                        for i in range(0, 8):
                                            for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                        black_pointer=-1
                        elif crstr in bc:
                            found=1
                            
                            r=crstr

                            x=int(crstr[0])
                            y=int(crstr[1])
                            r=STR(x,y)
                            x2=x
                            y2=y
                            x3=x
                            y3=y
                            x4=x
                            y4=y
                            while x>=0 and y<=7:
                                x=x-1
                                y=y+1
                                o1=STR(x,y)

                                if o1 in bsl+bc+bh+bk+be+bq:
                                    break
                                elif o1 in wsl+wc+wh+wk+wq+we+iw:
                                    reachablebox.append(o1)
                                    break
                                else:
                                    reachablebox.append(o1)
                            while x2<=7 and y2<=7:
                                x2=x2+1
                                y2=y2+1
                                o2=STR(x2,y2)
                                if o2 in bsl+bc+bh+bk+be+bq:

                                    break
                                elif o2 in  wsl+wc+wh+wk+wq+we+iw:
                                    reachablebox.append(o2)
                                    break
                                else:
                                    reachablebox.append(o2)
                            while x3<=7 and y3>=0:
                                x3=x3+1
                                y3=y3-1
                                o3=STR(x3,y3)
                                if o3 in bsl+bc+bh+bk+be+bq:

                                    break
                                elif o3 in wsl+wc+wh+wk+wq+we+iw:
                                    reachablebox.append(o3)
                                    break
                                else:
                                    reachablebox.append(o3)                                
                            while x4>=0 and y4>=0:
                                x4=x4-1
                                y4=y4-1
                                o4=STR(x4,y4)
                                if o4 in bsl+bc+bh+bk+be+bq:

                                    break
                                elif o4 in  wsl+wc+wh+wk+wq+we+iw:
                                    reachablebox.append(o4)
                                    break
                                else:
                                    reachablebox.append(o4)
                            i=0
                            while i<len(reachablebox):
                            
                                pi=bc.index(crstr)
                                ant=bc[pi]
                                bc[pi]=reachablebox[i]
                                
                                lpl2=bkalake()
                                if bk[0] in lpl2:
                                    if reachablebox[i] not in wc+wq:
                                        reachablebox[i]=0

                                bc[pi]=ant
                                i=i+1
                            
                            reachablebox=[i for i in reachablebox if i!=0]                                      
                            if found==1:
                                    drawrectfrompos(crstr)
                                    reachablebox=[i for i in reachablebox if i!='-1']
                                    for i in reachablebox:
                                        drawrectfrompos(i)

                                    black_pointer=crstr
                            else:
                                for i in range(0, 8):
                                    for j in range(0, 8):
                                            i1 = 100 * i
                                            j1 = 100 * j
                                            if (i + j) % 2 == 0:
                                                pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                            else:
                                                pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                    black_pointer=-1   
                        elif crstr in be:
                                found=1
                                x=int(crstr[0])
                                y=int(crstr[1])
                                x2=x
                                y2=y
                                x3=x
                                y3=y
                                x4=x
                                y4=y
                                while y<=7:
                                    y=y+1
                                    q=STR(x,y)
                                    if q in bsl+bc+bh+bk+be+bq:
                                        break
                                    elif q in  wsl+wc+wh+wk+wq+we+iw:
                                        reachablebox.append(q)
                                        break
                                    else:
                                        reachablebox.append(q)
                                while y2>=0:
                                    y2=y2-1
                                    q2=STR(x2,y2)
                                    if q2 in bsl+bc+bh+bk+be+bq:
                                        break
                                    elif q2 in  wsl+wc+wh+wk+wq+we+iw:
                                        reachablebox.append(q2)
                                        break
                                    else:
                                        reachablebox.append(q2)
                                while x3>=0:
                                    x3=x3-1
                                    q3=STR(x3,y3)
                                    if q3 in bsl+bc+bh+bk+be+bq:
                                        break
                                    elif q3 in wsl+wc+wh+wk+wq+we+iw:
                                        reachablebox.append(q3)
                                        break
                                    else:
                                        reachablebox.append(q3)
                                while x4<=7:
                                    x4=x4+1
                                    q4=STR(x4,y4)
                                    if q4 in bsl+bc+bh+bk+be+bq:
                                        break
                                    elif q4 in wsl+wc+wh+wk+wq+we+iw:
                                        reachablebox.append(q4)
                                        break
                                    else:
                                        reachablebox.append(q4)
                                i=0
                                while i<len(reachablebox):
                                    
                                    pi=be.index(crstr)
                                    ant=be[pi]
                                    be[pi]=reachablebox[i]
                                    
                                    lpl2=bkalake()
                                    if bk[0] in lpl2:
                                        if reachablebox[i] not in we+wq:                                
                                            reachablebox[i]=0

                                    be[pi]=ant
                                    i=i+1
                            

                                reachablebox=[i for i in reachablebox if i!=0]                                         
                                if found==1:
                                    
                                    drawrectfrompos(crstr)
                                    reachablebox=[i for i in reachablebox if i!='-1']

                                    for i in reachablebox:
                                        drawrectfrompos(i)

                                    black_pointer=crstr
                                else:
                                    for i in range(0, 8):
                                        for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                        black_pointer=-1                                  
                        elif crstr in bq:
                                found=1
                                x=int(crstr[0])
                                y=int(crstr[1])
                                x2=x
                                y2=y
                                x3=x
                                y3=y
                                x4=x
                                y4=y
                                while y<=7:
                                    y=y+1
                                    q=STR(x,y)
                                    if q in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif q in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(q)
                                        break
                                    else:
                                        reachablebox.append(q)
                                while y2>=0:
                                    y2=y2-1
                                    q2=STR(x2,y2)
                                    if q2 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif q2 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(q2)
                                        break
                                    else:
                                        reachablebox.append(q2)
                                while x3>=0:
                                    x3=x3-1
                                    q3=STR(x3,y3)
                                    if q3 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif q3 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(q3)
                                        break
                                    else:
                                        reachablebox.append(q3)
                                while x4<=7:
                                    x4=x4+1
                                    q4=STR(x4,y4)
                                    if q4 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif q4 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(q4)
                                        break
                                    else:
                                        reachablebox.append(q4)
                                # Assuming crstr is a list with at least two elements
                                x = int(crstr[0])
                                y = int(crstr[1])
                                r = STR(x, y)
                                r2 = r
                                x_positive_diagonal = x
                                y_positive_diagonal = y
                                x_negative_diagonal = x
                                y_negative_diagonal = y
                                x_horizontal_right = x
                                y_horizontal_right = y
                                x_horizontal_left = x
                                y_horizontal_left = y

                                while x_positive_diagonal >= 0 and y_positive_diagonal >= 0:
                                    x_positive_diagonal -= 1
                                    y_positive_diagonal -= 1
                                    o1 = STR(x_positive_diagonal, y_positive_diagonal)
                                    if o1 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif o1 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(o1)
                                        break
                                    else:
                                        reachablebox.append(o1)

                                while x_horizontal_right <= 7 and y_horizontal_right >= 0:
                                    x_horizontal_right += 1
                                    y_horizontal_right -= 1
                                    o1 = STR(x_horizontal_right, y_horizontal_right)
                                    if o1 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif o1 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(o1)
                                        break
                                    else:
                                        reachablebox.append(o1)

                                while x_negative_diagonal >= 0 and y_negative_diagonal <= 7:
                                    x_negative_diagonal -= 1
                                    y_negative_diagonal += 1
                                    o1 = STR(x_negative_diagonal, y_negative_diagonal)
                                    if o1 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif o1 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(o1)
                                        break
                                    else:
                                        reachablebox.append(o1)

                                while x_horizontal_left <= 7 and y_horizontal_left <= 7:
                                    x_horizontal_left += 1
                                    y_horizontal_left += 1
                                    o1 = STR(x_horizontal_left, y_horizontal_left)
                                    if o1 in bc+bh+bsl+be+bk+bq:
                                        break
                                    elif o1 in wc+wh+wsl+we+wk+wq+iw:
                                        reachablebox.append(o1)
                                        break
                                    else:
                                        reachablebox.append(o1)
                                i=0
                                while i<len(reachablebox):
                                    
                                    pi=bq.index(crstr)
                                    ant=bq[pi]
                                    bq[pi]=reachablebox[i]
                                    
                                    lpl2=bkalake()
                                    if bk[0] in lpl2:
                                        if reachablebox[i] not in we+wq+wc:                                
                                            reachablebox[i]=0

                                    bq[pi]=ant
                                    i=i+1
                                
                                reachablebox=[i for i in reachablebox if i!=0]                                        
                                if found==1:
                                    
                                    drawrectfrompos(crstr)
                                    reachablebox=[i for i in reachablebox if i!='-1']

                                    for i in reachablebox:
                                        drawrectfrompos(i)

                                    black_pointer=crstr
                                else:
                                    for i in range(0, 8):
                                        for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                        black_pointer=-1                                       
                        elif crstr in bk:
                                found=1
                                x=int(crstr[0])
                                y=int(crstr[1])

                                l=[STR(x-1,y-1),STR(x,y-1),STR(x+1,y-1),STR(x-1,y),STR(x+1,y),STR(x-1,y+1),STR(x,y+1),STR(x+1,y+1)]
                                l=[i for i in l if i not in bsl+bh+be+bq+bc]
                                reachablebox.extend(l)
                                for sol in reachablebox:
                                    nkr=bk[0]
                                    bk[0]=sol
                                    q=wchecker()
                                    if q==1:
                                        reachablebox.remove(sol)
                                    bk[0]=nkr
                                reachablebox=[i for i in reachablebox if i!='-1']
                                for i in reachablebox:
                                    k=checkwpower(i)
                                    if k==3:
                                        rm=wh.index(i)
                                        vrm=wh[rm]
                                        wh[rm]=0
                                        nkr=bk[0]
                                        bk[0]=i
                                        o=wwchecker(bk[0])
                                        if o==1:
                                            reachablebox.remove(i)
                                        wh[rm]=vrm
                                        bk[0]=nkr
                                    elif k==2:
                                        rm=wc.index(i)
                                        vrm=wc[rm]
                                        wc[rm]=0
                                        nkr=bk[0]
                                        bk[0]=i
                                        o=wwchecker(bk[0])
                                        if o==1:
                                            reachablebox.remove(i)
                                        wc[rm]=vrm
                                        bk[0]=nkr
                                    elif k==4:
                                        rm=we.index(i)
                                        vrm=we[rm]
                                        we[rm]=0
                                        nkr=bk[0]
                                        bk[0]=i
                                        o=wwchecker(bk[0])
                                        if o==1:
                                            reachablebox.remove(i)
                                        we[rm]=vrm
                                        bk[0]=nkr  
                                    elif k==5:
                                        rm=wq.index(i)
                                        vrm=wq[rm]
                                        wq[rm]=0
                                        nkr=bk[0]
                                        bk[0]=i
                                        o=wwchecker(bk[0])
                                        if o==1:
                                            reachablebox.remove(i)
                                        wq[rm]=vrm
                                        bk[0]=nkr    
                                    elif k==1:
                                        rm=wsl.index(i)
                                        vrm=wsl[rm]
                                        wsl[rm]=0
                                        nkr=bk[0]
                                        bk[0]=i
                                        o=wwchecker(bk[0])
                                        if o==1:
                                            reachablebox.remove(i)
                                        wsl[rm]=vrm
                                        bk[0]=nkr                                                                                                                                                               
                                    elif k==6:
                                        rm=wk.index(i)
                                        vrm=wk[rm]
                                        wk[rm]=0
                                        nkr=bk[0]
                                        bk[0]=i
                                        o=wwchecker(bk[0])
                                        if o==1:
                                            reachablebox.remove(i)
                                        wk[rm]=vrm
                                        bk[0]=nkr                                               

                                for i in we:
                                    j=elephantreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)

                                for i in wc:
                                    j=camelreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)                                        

                                for i in wh:
                                    j=horsereach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)  

                                for i in wk:
                                    j=wkingreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k) 
                                for i in wq:
                                    j=camelreach(i)
                                    for k in j:
                                        if k in reachablebox:
                                            reachablebox.remove(k)
                                    j2=elephantreach(i)                                              
                                    for k in j2:
                                        if k in reachablebox:
                                            reachablebox.remove(k)    
                                if blcastlepossible==1:
                                    reachablebox.append("00")
                                if brcastlepossible==1:
                                    reachablebox.append("70")          
                                            
                                             
                                if found==1:
                                    
                                    drawrectfrompos(crstr)
                                    
                                    for i in reachablebox:
                                        drawrectfrompos(i)



                                    black_pointer=crstr
                                else:
                                    for i in range(0, 8):
                                        for j in range(0, 8):
                                                i1 = 100 * i
                                                j1 = 100 * j
                                                if (i + j) % 2 == 0:
                                                    pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                                else:
                                                    pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                        black_pointer=-1           
            elif wcheck==1:
                pandit=0
                found=0
                asuran=bcheckedby[-1]
                possiblemoves={} #This is to find which can attack
                for i in bd:
                    if i not in bk:
                        l=bd[i]
                        for j in l:
                            if j==asuran:
                                possiblemoves[i]=[j]
                #This is to find which can block
                for i in bdwos:
                    if i not in bk:
                        l=bdwos[i]
                        
                        for j in l:
                            if int(j)>0 and j!='-1':
                                ib.append(j)
                                g=wchecker()
                                if g==0:
                                    if i not in possiblemoves:
                                        possiblemoves[i]=[j]
                                    else:
                                        possiblemoves[i].append(j)
                                ib=[]
                
                dust=bjf()
                for i in dust:
                    l=dust[i]
                    
                    for j in l:
                        if int(j)>=0 and j!='-1':
                            ib.append(j)
                            g=wchecker()
                            if g==0:
                                possiblemoves[i]=[j]
                            ib=[]    
                ad=bk[0]
                adr=bkingreach(ad) 
                                                                                           
                for i in adr:                                            
                    ntr2=bk[0]
                    bk[0]=i
                    og=wchecker()
                    if og==0:
                        if ntr2 not in possiblemoves:
                            possiblemoves[ntr2]=[i]
                        else:
                            possiblemoves[ntr2].append(i)

                    bk[0]=ntr2
                if bk[0] in possiblemoves:                    
                            for o in possiblemoves[bk[0]]:
                                smn=checkwpower(o)
                                if smn==3:
                                    h=wh.index(o)
                                    faz=wh[h]
                                    wh[h]=0

                                    ops=wwchecker(o)
                                    if ops==1:
                                        possiblemoves[bk[0]].remove(o)
                                    wh[h]=faz
                                elif smn==2:
                                    h=wc.index(o)
                                    faz=wc[h]
                                    wc[h]=0

                                    ops=wwchecker(o)
                                    if ops==1:
                                        possiblemoves[bk[0]].remove(o)
                                    wc[h]=faz
                                elif smn==4:
                                    h=we.index(o)
                                    faz=we[h]
                                    we[h]=0

                                    ops=wwchecker(o)
                                    if ops==1:
                                        possiblemoves[bk[0]].remove(o)
                                    we[h]=faz                                    
                                elif smn==5:
                                    h=wq.index(o)
                                    faz=wq[h]
                                    wq[h]=0

                                    ops=wwchecker(o)
                                    if ops==1:
                                        possiblemoves[bk[0]].remove(o)
                                    wq[h]=faz                                
                                elif smn==1:
                                    h=wsl.index(o)
                                    faz=wsl[h]
                                    wsl[h]=0

                                    ops=wwchecker(o)
                                    if ops==1:
                                        possiblemoves[bk[0]].remove(o)
                                    wsl[h]=faz 
                for i in possiblemoves:
                    if possiblemoves[i]!=[]:
                        pandit=pandit+1
                if pandit==0:
                    wpl=[]
                    bpl=[]
                    ws=[]
                    bs=[]
                    turn=2
                    

                    t=pygame.font.SysFont('calibri',48)
                    r1=t.render("WHITE WINS",True,black)
                    r11=r1.get_rect()
                    r11.center=(1000,50) 
                    ds.blit(r1,r11)                               
                if black_pointer != -1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        ucrstr1 = ucrstr
                        c1 = event.pos[0]
                        c2 = event.pos[1]
                        c = [c1, c2]
                        cr = boxonclicktocr(c)
                        ucrstr2 = str(cr[0]) + str(cr[1])

                        if ucrstr2 not in reachableboxc:
                            for i in range(0, 8):
                                for j in range(0, 8):
                                    i1 = 100 * i
                                    j1 = 100 * j
                                    if (i + j) % 2 == 0:
                                        pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                    else:
                                        pygame.draw.rect(ds, green, (i1, j1, 100, 100))

                        else:
                            if ucrstr in bsl:
                                try:
                                    ind = bsl.index(ucrstr1)
                                except ValueError:
                                    print("Error: crstr1 not found in bsl.")
                                    continue

                                bsl.remove(ucrstr1)
                                bsl.insert(ind, ucrstr2)
                                if ucrstr2 in wsl:
                                    bii=wsl.index(ucrstr2)
                                    wsl[bii]=0
                                    ws[bii]=[0,0]
                                elif ucrstr2 in wh:
                                    ii=wh.index(ucrstr2)
                                    wh[ii]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ii]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                              
                                elif ucrstr2 in wc:
                                    ic=wc.index(ucrstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c'] 
                                elif ucrstr2 in we:
                                    ic=we.index(ucrstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e']    
                                elif ucrstr2 in wq:
                                    ic=wq.index(ucrstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                          
                                bs[ind][1].center = fromcrtocenter(ucrstr2)
                                leo=bgivesinglediagnol(ucrstr2)
                                leo.pop()
                                if wk[0] in leo:
                                    wcheckedby.append(ucrstr2)
                            elif ucrstr in bh:
                                lak=[i for i in bpl if i[2]=="h"]

                                try:
                                    ind = bh.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bh[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2) 
                                lai=bhorsereach(ucrstr2)
                                if wk[0] in lai:
                                    wcheckedby.append(ucrstr2)
                                    

                                if ucrstr2 in wsl:
                                    ind2=wsl.index(ucrstr2)
                                    ws[ind2]=[0,0]          
                                    wsl[ind2]=0 
                                elif ucrstr2 in wh:
                                    ind=wh.index(ucrstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif ucrstr2 in wc:
                                    ic=wc.index(ucrstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c'] 
                                elif ucrstr2 in we:
                                    ic=we.index(ucrstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e']  
                                elif ucrstr2 in wq:
                                    ic=wq.index(ucrstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                           
                            elif ucrstr1 in bc:
                                lak=[i for i in bpl if i[2]=="c"]

                                try:
                                    ind = bc.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bc[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)   
                                lai=bcamelreach(ucrstr2)
                                if wk[0] in lai:
                                    wcheckedby.append(ucrstr2)                                                   
                                if ucrstr2 in wsl:
                                    ind2=wsl.index(ucrstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif ucrstr2 in wh:
                                    ind=wh.index(ucrstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif ucrstr2 in wc:
                                    ic=wc.index(ucrstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c']  
                                elif ucrstr2 in we:
                                    ic=we.index(ucrstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif ucrstr2 in wq:
                                    ic=wq.index(ucrstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                                                               
                            elif ucrstr1 in bq:
                                lak=[i for i in bpl if i[2]=="q"]

                                try:
                                    ind = bq.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bq[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)
                                lai=bcamelreach(ucrstr2)
                                lai2=belephantreach(ucrstr2)
                                if wk[0] in lai+lai2:
                                    wcheckedby.append(ucrstr2)
                                                        
                                if ucrstr2 in wsl:
                                    ind2=wsl.index(ucrstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif ucrstr2 in wh:
                                    ind=wh.index(ucrstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif ucrstr2 in wc:
                                    ic=wc.index(ucrstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c']  
                                elif ucrstr2 in we:
                                    ic=we.index(ucrstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif ucrstr2 in wq:
                                    ic=wq.index(ucrstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q'] 
                            elif ucrstr1 in bk:
                                lak=[i for i in bpl if i[2]=="k"]

                                try:
                                    ind = bk.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                bk[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2)                          
                                if ucrstr2 in wsl:
                                    ind2=wsl.index(ucrstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif ucrstr2 in wh:
                                    ind=wh.index(ucrstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif ucrstr2 in wc:
                                    ic=wc.index(ucrstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c']  
                                elif ucrstr2 in we:
                                    ic=we.index(ucrstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif ucrstr2 in wq:
                                    ic=wq.index(ucrstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q'] 
                            elif ucrstr1 in be:
                                lak=[i for i in bpl if i[2]=="e"]

                                try:
                                    ind = be.index(ucrstr1)
                                except ValueError:
                                    # Handle the case where crstr1 is not found in wsl
                                    print("Error: crstr1 not found in wsl.")
                                    continue  # Skip the rest of the loop  
                                be[ind]=ucrstr2
                                lak[ind][1].center = fromcrtocenter(ucrstr2) 
                                lai=belephantreach(ucrstr2)
                                if wk[0] in lai:
                                    wcheckedby.append(ucrstr2)                         
                                if ucrstr2 in wsl:
                                    ind2=wsl.index(ucrstr2)
                                    ws[ind2]=[0,0]
                                    wsl[ind2]=0
                                elif ucrstr2 in wh:
                                    ind=wh.index(ucrstr2)
                                    wh[ind]=0
                                    mo=[i for i in wpl if i[2]=="h"]
                                    illa=mo[ind]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'h']                 
                                elif ucrstr2 in wc:
                                    ic=wc.index(ucrstr2)
                                    wc[ic]=0
                                    mo=[i for i in wpl if i[2]=="c"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'c'] 
                                elif ucrstr2 in we:
                                    ic=we.index(ucrstr2)
                                    we[ic]=0
                                    mo=[i for i in wpl if i[2]=="e"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'e'] 
                                elif ucrstr2 in wq:
                                    ic=wq.index(ucrstr2)
                                    wq[ic]=0
                                    mo=[i for i in wpl if i[2]=="q"]
                                    illa=mo[ic]
                                    if illa in wpl:
                                        inde=wpl.index(illa)
                                        wpl[inde]=[0,0,'q']                                                                          
                            for i in range(0, 8):
                                for j in range(0, 8):
                                    i1 = 100 * i
                                    j1 = 100 * j
                                    if (i + j) % 2 == 0:
                                        pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                    else:
                                        pygame.draw.rect(ds, green, (i1, j1, 100, 100))

                            turn = 1

                        black_pointer = -1                                    
                else:   
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        reachableboxc=[]

                        u1=event.pos[0]
                        u2=event.pos[1]
                        u=[u1,u2]
                        ur=boxonclicktocr(u)
                        ucrstr=str(ur[0])+str(ur[1])       
                        if ucrstr in possiblemoves:
                            found=1
                            drawrectfrompos(ucrstr)
                            reachableboxc.extend(possiblemoves[ucrstr])
                            if found==1:
                                

                                for i in reachableboxc:
                                    drawrectfrompos(i) 
                                black_pointer=ucrstr 
                            else:

                                for i in range(0, 8):
                                    for j in range(0, 8):
                                        i1 = 100 * i
                                        j1 = 100 * j
                                        if (i + j) % 2 == 0:
                                            pygame.draw.rect(ds, white, (i1, j1, 100, 100))
                                        else:
                                            pygame.draw.rect(ds, green, (i1, j1, 100, 100))
                                black_pointer=-1


        pygame.display.update()
        for i in ws+bs+wpl+bpl:
            if i[0]!=0:
                ds.blit(i[0],i[1])
    
    

    pygame.display.update()

pygame.quit()


