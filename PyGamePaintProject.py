# PyGamePaintProject
from pygame import *
from math import*
import pygame
import webbrowser #to open links
from tkinter import* #for saving and loading
from tkinter import filedialog
from tkinter import messagebox
from tkinter import messagebox as mb
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('ValPaint v0.8 - Beta Warning','ValPaint is in Beta and not fully functional.\nProgram can crash unexpectedly.')
mixer.init() #initialize music player
root=Tk()
root.withdraw()#hides small window
pygame.init() #initializes pygame (used for window settings such as icon and window text)
width, height = 1400, 800
state=0 #variable to determine if screen is fullscreen
res=mb.askquestion("Window Size","Start ValPaint in fullscreen? (Work in Progress)\n(Must have minimum resolution of 1400x800)")
mouse.set_cursor((43,43), transform.scale(image.load("assets/graphics/cursor.png"), (100,100)))
if res == 'yes' :
    screen = display.set_mode((0,0),pygame.FULLSCREEN)
    state=1
else :
    screen = display.set_mode((width, height))
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)
VALBLUE = (71,21,21)
bg = transform.scale((image.load("assets/graphics/bg.jpg")),(1920,1080))
screen.blit(bg, (-20, -100))
draw.rect(screen,VALBLUE,(20,100,40,645),0,25)
saveRect = draw.rect(screen, VALBLUE, (880, 40, 55, 55),0,27)
loadRect = draw.rect(screen, VALBLUE, (880+55+5, 40, 55, 55),0,25)
draw.rect(screen, VALBLUE, (75, 40, 705, 55),0,25)
blackRect = draw.rect(screen, BLACK, (80+60, 50, 20, 20),0,10)
undoRect = draw.rect(screen, VALBLUE, (785, 50, 40, 40),0,10)
redoRect = draw.rect(screen, VALBLUE, (830, 50, 40, 40),0,10)
whiteRect = draw.rect(screen, WHITE, (80+60, 70, 20, 20),0,10)
# image loading - optimized (transformation and loading within one line)
pencilicon = image.load("assets/graphics/pencil.png")
erasericon = image.load("assets/graphics/eraser.png")
paintIcon = image.load("assets/graphics/paint.png")
vstamp = transform.scale((image.load("assets/graphics/vlogo.png")), (70, 50))
ostamp = transform.scale((image.load("assets/graphics/Omen_icon.png")), (40, 40))
jstamp = transform.scale((image.load("assets/graphics/Jett_icon.png")), (40, 40))
kstamp = transform.scale((image.load("assets/graphics/KAYO_icon.png")), (40, 40))
rstamp = transform.scale((image.load("assets/graphics/Reyna_icon.png")), (40, 40))
filledRecticon = image.load("assets/graphics/filledRect.png")
unfilledRecticon = image.load("assets/graphics/unfilledRect.png")
filledEllipseicon = image.load("assets/graphics/filledEllipse.png")
unfilledEllipseicon = image.load("assets/graphics/unfilledEllipse.png")
saveIcon = image.load("assets/graphics/save.png")
loadIcon = image.load("assets/graphics/load.png")
undoIcon = image.load("assets/graphics/undo.png")
redoIcon = image.load("assets/graphics/redo.png")
logo = transform.scale((image.load("assets/graphics/logo.png")), (50, 50))
palette = transform.scale((image.load("assets/graphics/palette.png")), (600, 41))
lineIcon = image.load("assets/graphics/line.png")
valpaint=transform.scale((image.load("assets/graphics/valpaint.png")),(760,480))
playicon = image.load("assets/graphics/play.png")
pauseicon = image.load("assets/graphics/pause.png")
powericon= image.load("assets/graphics/start.png")
plus = image.load("assets/graphics/plus.png")
minus = image.load("assets/graphics/minus.png")
valdownload = transform.scale((image.load("assets/graphics/vallogo.png")),(50,50))
nextsong = transform.scale((image.load("assets/graphics/next.png")),(20,20))
previous = transform.scale((image.load("assets/graphics/previous.png")),(20,20))
screen.blit(valpaint,(847,-190))
screen.blit(saveIcon, (880, 40))
screen.blit(loadIcon, (945, 45))
screen.blit(undoIcon, undoRect)
screen.blit(redoIcon, redoRect)
screen.blit(logo, (15, 40))  # app logo
downloadRect = Rect(1080,190,310,65)
pygame.display.set_icon(logo)
pygame.display.set_caption('ValPaint')

#music loading
volume=0.5
mixer.music.set_volume(volume)
playlist1 = ["assets/audio/aud.mp3",'assets/audio/aud1.mp3','assets/audio/aud2.mp3','assets/audio/aud3.mp3','assets/audio/aud4.mp3','assets/audio/aud5.mp3','assets/audio/aud6.mp3','assets/audio/aud7.mp3']
# rect loading ----- convert to >>for i in range<< for code efficiency

pencilRect = Rect(20, 100, 40, 40)
eraserRect = Rect(20, 150, 40, 40)
paintRect = Rect(20, 200, 40, 40)
canvasRect = Rect(75, 100, 1000, 675)
paletteRect = Rect(100+65, 45, 600, 40)  # 3*20=60 width
screen.blit(palette, paletteRect)
filledRect = Rect(20, 250, 40, 40)
unfilledRect = Rect(20, 300, 40, 40)
filledEllipse = Rect(20, 350, 40, 40)
unfilledEllipse = Rect(20, 400, 40, 40)
stampOne = Rect(20, 450, 40, 40)
stampTwo = Rect(20, 500, 40, 40)
stampThree = Rect(20, 550, 40, 40)
stampFour = Rect(20, 600, 40, 40)
stampFive = Rect(20, 650, 40, 40)
lineRect = Rect(20, 700, 40, 40)
startRect = Rect(1100,120,40,40)
playRect = Rect(1150,120,40,40)
pauseRect = Rect(1200,120,40,40)
musicRect = Rect(1080,100,310,80)
volumeUpRect = Rect(1250,120,40,40)
volumeDownRect = Rect(1300,120,40,40)
tooltipRect = Rect(1080,265,310,100)
thicknessRect = Rect(1080,380,310,130)
mastersRect = Rect(1080,520,310,250)
nextRect = Rect(1350,120,20,20)
previousRect = Rect(1350,140,20,20)

tools = [pencilRect, eraserRect, paintRect, filledRect, unfilledRect, filledEllipse,
         unfilledEllipse, stampOne, stampTwo, stampThree, stampFour, stampFive, lineRect,undoRect,redoRect,nextRect,previousRect]
running = True
songPos=0
mixer.music.load(playlist1[songPos])
tool = ""
col = BLACK
bgcol = WHITE
radius = 10
draw.rect(screen, WHITE, canvasRect)
screenCap = screen.subsurface(canvasRect).copy()
thickness = 5
link_font = pygame.font.SysFont('Tahoma', 20)
link_color = WHITE    
while running:
    click=False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == KEYDOWN:
            keys = key.get_pressed()
            if keys[K_UP]:
                thickness += 1
            if keys[K_DOWN]:
                thickness -= 1
            if keys[K_LEFT]:
                thickness -= 2
            if keys[K_RIGHT]:
                thickness += 2
    textRect = draw.rect(screen, VALBLUE, (20, 750, 40, 40),0,50)
    draw.rect(screen,VALBLUE,(thicknessRect),0,25)
    draw.rect(screen,RED,(1090,390,50,25),0,25)
    screen.blit((link_font.render(str(thickness)+"      <- Thickness (px)", True, link_color)), (1100, 390))
    screen.blit((link_font.render("To Adjust:", True, link_color)), (1100, 410))
    screen.blit((link_font.render("Up/Down Arrow = +/- 1", True, link_color)), (1100, 430))
    screen.blit((link_font.render("Left/Right Arrow = +/- 2 ", True, link_color)), (1100, 450))
    screen.blit((link_font.render("Automatically applied to tools.", True, link_color)), (1100, 470))


    if evt.type == MOUSEBUTTONDOWN:
        if evt.button == 1:  # left click
            sx, sy = evt.pos  # getting the STARTING x and y pos
            myRect = Rect(sx, sy, mx-sx, my-sy)
            click=True
    
    if evt.type == MOUSEBUTTONUP:
        if mb[0]:
            if downloadRect.collidepoint(mx,my):
                webbrowser.open(r"https://playvalorant.com/")
                messagebox.showinfo('ValPaint v0.8','Download link opened in browser!')
            if mastersRect.collidepoint(mx,my):
                webbrowser.open(r"https://www.twitch.tv/VALORANT/")
                messagebox.showinfo('ValPaint v0.8','VALORANT Masters Live Twitch link opened!')
        if state==1:              
            if mb[0] and updateRect.collidepoint(mx,my):
                webbrowser.open(r"https://github.com/x-plane11-git/PyPaint")

        if tool == "pencil":
            screen.set_clip(canvasRect)
            draw.line(screen, col, (oldmx, oldmy), (mx, my))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "eraser":
            screen.set_clip(canvasRect)
            draw.circle(screen, bgcol, (mx, my), thickness)
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "paintbucket":
            screen.set_clip(canvasRect)
##            screen.fill(col, canvasRect)
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "stampOne":
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            screen.blit(vstamp, (mx-20, my-20))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "stampTwo":
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            screen.blit(jstamp, (mx-20, my-20))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "stampThree":
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            screen.blit(rstamp, (mx-20, my-20))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "stampFour":
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            screen.blit(ostamp, (mx-20, my-20))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "stampFive":
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            screen.blit(kstamp, (mx-20, my-20))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "filledRect":
            myRect.normalize()
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            draw.rect(screen, col, (myRect))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "unfilledRect":
            myRect.normalize()
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            draw.rect(screen, col, (myRect), thickness)
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "filledEllipse":
            myRect.normalize()
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            draw.ellipse(screen, col, myRect)
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "unfilledEllipse":
            myRect.normalize()
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            draw.ellipse(screen, col, myRect, thickness)
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "line":
            screen.set_clip(canvasRect)
            screen.blit(screenCap, canvasRect)
            draw.line(screen, col, (sx, sy), (mx, my), thickness)
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)

    mx, my = mouse.get_pos()  # getting the current mx and my
    mb = mouse.get_pressed()
    #for fullscreen users
    if state==1:
        screen.blit((pygame.font.SysFont('Tahoma', 15)).render("Programmed By Taksh Unnithan on Pygame",True,WHITE),(25,825))
        draw.rect(screen,VALBLUE,(1400,100,130,675),0,20)
        git=transform.scale((image.load("assets/graphics/github.png")),(100,100))
        updateRect=draw.rect(screen,VALBLUE,(1415,120,100,100))
        screen.blit(git,(1415,120))
        if updateRect.collidepoint(mx,my):
                draw.rect(screen,GREEN,updateRect,2,20)  
    # drawing all tools
    for rects in range(len(tools)):
        draw.rect(screen, VALBLUE, tools[rects],0,10)
    draw.rect(screen,VALBLUE,downloadRect,0,20)
    screen.blit(valdownload, (1095,200))
    screen.blit(link_font.render("Download Valorant>>>", True, link_color), (1150, 210))
    draw.rect(screen,VALBLUE,mastersRect,0,25)
    masterlive = transform.scale((image.load("assets/graphics/mastersnews.jpg")), (290, 190))
    screen.blit(masterlive,(1090,530))
    screen.blit((pygame.font.SysFont('Tahoma', 15)).render("Watch VALORANT Masters Live on Twitch>",True,WHITE),(1090,730))
    draw.rect(screen,VALBLUE,tooltipRect,0,25)
    draw.rect(screen,BLUE,startRect,0,20)
    draw.rect(screen,VALBLUE,musicRect,0,25)
    draw.rect(screen, BLUE, playRect,0,20)
    draw.rect(screen,BLUE, pauseRect,0,20)
    draw.rect(screen,BLUE, volumeUpRect,0,20)
    draw.rect(screen,BLUE, volumeDownRect,0,20)
    saveRect = draw.rect(screen, VALBLUE, (880, 40, 55, 55),0,27)
    loadRect = draw.rect(screen, VALBLUE, (880+55+5, 40, 55, 55),0,25)
    screen.blit(pencilicon, (22, 103))
    screen.blit(erasericon, (22, 152))
    draw.rect(screen, col, (20+75, 47, 40, 40))  # colour picker preview
    draw.rect(screen, BLACK, (20+75, 47, 40, 40), 2)  # outline for preview
    screen.blit(paintIcon,(23, 203, 40, 40))
    screen.blit(vstamp, (5, 445, 40, 40))
    screen.blit(filledRecticon, (filledRect))
    screen.blit(unfilledRecticon, (22, 302, 40, 40))
    screen.blit(filledEllipseicon, (filledEllipse))
    screen.blit(unfilledEllipseicon, (unfilledEllipse))
    screen.blit(jstamp, (stampTwo))
    screen.blit(rstamp, (stampThree))
    screen.blit(ostamp, (stampFour))
    screen.blit(kstamp, (stampFive))
    screen.blit(lineIcon, (23, 703, 40, 40))
    screen.blit(playicon, playRect)
    screen.blit(pauseicon, pauseRect)
    screen.blit(powericon, startRect)
    screen.blit(plus, volumeUpRect)
    screen.blit(minus, volumeDownRect)
    screen.blit(nextsong, nextRect)
    screen.blit(previous, previousRect)

    # selecting the tools
    if mb[0]:
        if blackRect.collidepoint(mx, my):
            col = BLACK
        if whiteRect.collidepoint(mx, my):
            col = WHITE
        if pencilRect.collidepoint(mx, my):
            tool = "pencil"
        if eraserRect.collidepoint(mx, my):
            tool = "eraser"
        if paintRect.collidepoint(mx, my):
            tool = "paintbucket"
        if filledRect.collidepoint(mx, my):
            tool = "filledRect"
        if unfilledRect.collidepoint(mx, my):
            tool = "unfilledRect"
        if filledEllipse.collidepoint(mx, my):
            tool = "filledEllipse"
        if unfilledEllipse.collidepoint(mx, my):
            tool = "unfilledEllipse"
        if stampOne.collidepoint(mx, my):
            tool = "stampOne"
        if stampTwo.collidepoint(mx, my):
            tool = "stampTwo"
        if stampThree.collidepoint(mx, my):
            tool = "stampThree"
        if stampFour.collidepoint(mx, my):
            tool = "stampFour"
        if stampFive.collidepoint(mx, my):
            tool = "stampFive"
        if lineRect.collidepoint(mx, my):
            tool = "line"
    if mb[0] and playRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,playRect,2,20)
        mixer.music.unpause()
    if mb[0] and pauseRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,pauseRect,2,20)
        mixer.music.pause()
    ############### work in progress #####################
    if click and startRect.collidepoint(mx,my):
        print("hii")
        draw.rect(screen,BLUE,startRect,2,20)
        mixer.music.play()

    if click and nextRect.collidepoint(mx,my):
        songPos=(songPos+1)%len(playlist1)
        mixer.music.load(playlist1[songPos])
        mixer.music.play()
    if click and previousRect.collidepoint(mx,my):
        songPos=(songPos-1+(len(playlist1)))%len(playlist1)
        mixer.music.load(playlist1[songPos])
        mixer.music.play()   
    ################### work in progress #################
    if mb[0] and volumeDownRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,volumeDownRect,2,20)
        volume-=0.1
        mixer.music.set_volume(volume)
    if mb[0] and volumeUpRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,volumeUpRect,2,20)
        volume+=0.1
        mixer.music.set_volume(volume)
    if mb[2] and startRect.collidepoint(mx,my):
        mixer.music.stop()

    # collidepoint visuals
    for i in range(len(tools)):
        if tools[i].collidepoint(mx, my):
            draw.rect(screen, RED, tools[i], 2,10)
    saveRect = draw.rect(screen, VALBLUE, (880, 40, 55, 55),0,27)
    loadRect = draw.rect(screen, VALBLUE, (880+55+5, 40, 55, 55),0,25)
    screen.blit(saveIcon, (880, 40))
    screen.blit(loadIcon, (945, 45))
    screen.blit(undoIcon, undoRect)
    screen.blit(redoIcon, redoRect)
    if saveRect.collidepoint(mx, my):
            draw.rect(screen, RED, saveRect, 2,25)
    if loadRect.collidepoint(mx, my):
            draw.rect(screen, RED, loadRect, 2,25)
    if pauseRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,pauseRect,2,20)
    if playRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,playRect,2,20)
    if startRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,startRect,2,20)
    if mastersRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,mastersRect,2,25)
    if downloadRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,downloadRect,2,25)
    #when tool is selected
    toolList = ["pencil","eraser","paintbucket","filledRect","unfilledRect","filledEllipse","unfilledEllipse","stampOne","stampTwo","stampThree","stampFour","stampFive","line"]
    stamps=["stampOne","stampTwo","stampThree","stampFour","stampFive"]
    try: draw.rect(screen,GREEN,tools[toolList.index(tool)],2,10)
    except: pass
    #ToolTip Text Rendering
    if tool == "pencil":
        screen.blit(link_font.render("Pencil Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click and Drag to draw.", True, link_color), (1100, 290))
    if tool == "eraser":
        screen.blit(link_font.render("Eraser Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click and Drag to erase.", True, link_color), (1100, 290))
    if tool == "paintbucket":
        screen.blit(link_font.render("Paint Bucket Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Fill the entire screen with", True, link_color), (1100, 290))
        screen.blit(link_font.render("your selected colour.", True, link_color), (1100, 310))
    if tool == "filledRect":
        screen.blit(link_font.render("Filled Rectangle:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click and Drag to draw", True, link_color), (1100, 290))
        screen.blit(link_font.render("a rectangle (filled).", True, link_color), (1100, 310))
    if tool == "unfilledRect":
        screen.blit(link_font.render("Unfilled Rectangle Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click and Drag to draw", True, link_color), (1100, 290))
        screen.blit(link_font.render("a rectangle. Adjust thickness", True, link_color), (1100, 310))
        screen.blit(link_font.render("with up or down arrow keys.", True, link_color), (1100, 330))
    if tool == "filledEllipse":
        screen.blit(link_font.render("Ellipse Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click and Drag to draw a", True, link_color), (1100, 290))
        screen.blit(link_font.render("filled Ellipse.", True, link_color), (1100, 310))
    if tool == "unfilledEllipse":
        screen.blit(link_font.render("Unfilled Ellipse Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click and Drag to draw Ellipse.", True, link_color), (1100, 290))
        screen.blit(link_font.render("Adjust thickness with up or", True, link_color), (1100, 310))
        screen.blit(link_font.render("down arrow keys.", True, link_color), (1100, 330))
    if tool == "line":
        screen.blit(link_font.render("Line Tool:", True, link_color), (1100, 270))
        screen.blit(link_font.render("Click for start point and drag.", True, link_color), (1100, 290))
        screen.blit(link_font.render("Release at desired end point.", True, link_color), (1100, 310))
    for stamp in stamps:
        if tool == stamp:
            screen.blit(link_font.render("Stamp Selected:", True, link_color), (1100, 270))
            screen.blit(link_font.render("Click and release to place.", True, link_color), (1100, 290))
            screen.blit(link_font.render("You may drag until satisfied", True, link_color), (1100, 310))
            screen.blit(link_font.render("then release.", True, link_color), (1100, 330))
    #Utilise the tool on the Canvas
    if canvasRect.collidepoint(mx, my) and mb[0]:
        screen.set_clip(canvasRect)
        if tool == "pencil":
            draw.line(screen, col, (oldmx, oldmy), (mx, my))
        if tool == "eraser":
            dx=mx-oldmx
            dy=my-oldmy
            dist=sqrt(dx**2+dy**2)
            for d in range(1,int(dist),1):
                dotX=d*dx/dist+oldmx
                dotY=d*dy/dist+oldmy
                draw.circle(screen,bgcol,(int(dotX),int(dotY)),thickness)
            draw.circle(screen, bgcol, (mx, my), thickness)
        if tool == "paintbucket":
            screen.fill(col, canvasRect)
        if tool == "filledRect":
            myRect = Rect(sx, sy, mx-sx, my-sy)
            myRect.normalize()
            screen.blit(screenCap, canvasRect)
            draw.rect(screen, col, myRect)
        if tool == "unfilledRect":
            myRect = Rect(sx, sy, mx-sx, my-sy)
            myRect.normalize()
            screen.blit(screenCap, canvasRect)
            draw.rect(screen, col, myRect, thickness)
        if tool == "filledEllipse":
            myRect = Rect(sx, sy, mx-sx, my-sy)
            myRect.normalize()
            screen.blit(screenCap, canvasRect)
            draw.ellipse(screen, col, myRect)
        if tool == "unfilledEllipse":
            myRect = Rect(sx, sy, mx-sx, my-sy)
            myRect.normalize()
            screen.blit(screenCap, canvasRect)
            draw.ellipse(screen, col, myRect, thickness)
        if tool == "stampOne":
            screen.blit(vstamp, (mx-35, my-20))
        if tool == "stampTwo":
            screen.blit(jstamp, (mx-20, my-20))
        if tool == "stampThree":
            screen.blit(rstamp, (mx-20, my-20))
        if tool == "stampFour":
            screen.blit(ostamp, (mx-20, my-20))
        if tool == "stampFive":
            screen.blit(kstamp, (mx-20, my-20))
        if tool == "line":
            screen.blit(screenCap, canvasRect)
            draw.line(screen, col, (sx, sy), (mx, my), thickness)

        screen.set_clip(None)  # only the canvas area can be updated
        
    # Customize colour
    if paletteRect.collidepoint(mx, my) and mb[0]:
        col = screen.get_at((mx, my))
    oldmx, oldmy = mx, my  # oldmx,oldmy is the mouse position in the previous frame
    #Saving and Loading
    if mb[0] and saveRect.collidepoint(mx,my):
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        if fname!="":
            image.save(screenCap,fname)
    if mb[0] and loadRect.collidepoint(mx,my):
        fname=filedialog.askopenfilename()
        if fname!="":
            screen.set_clip(canvasRect)
            fname=filedialog.askopenfilename()
            loadpic=image.load(fname)
            w2=loadpic.get_width()
            h2=loadpic.get_height()
            if w2<=1000 and h2<=675:
                screen.blit(loadpic,(75,100))
                screenCap=screen.subsurface(canvasRect).copy()
            else:
                loadpic2=transform.scale(loadpic,(w2//2,h2//2))
                screen.blit(loadpic2,(75,100))
                screenCap=screen.subsurface(canvasRect).copy()
        else:
            exit
    display.flip()
#end program
quit()
