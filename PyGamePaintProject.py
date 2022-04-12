# PyGamePaintProject
from pygame import *
import pygame
from tkinter import*
from tkinter import filedialog
root=Tk()
root.withdraw()#hides small window
pygame.init()
width, height = 1400, 800
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
pencilicon = transform.scale((image.load("assets/graphics/pencil.png")), (35, 35))
erasericon = transform.scale((image.load("assets/graphics/eraser.png")), (35, 35))
paintIcon = transform.scale((image.load("assets/graphics/paint.png")), (35, 35))
vstamp = transform.scale((image.load("assets/graphics/vlogo.png")), (70, 50))
ostamp = transform.scale((image.load("assets/graphics/Omen_icon.png")), (40, 40))
jstamp = transform.scale((image.load("assets/graphics/Jett_icon.png")), (40, 40))
kstamp = transform.scale((image.load("assets/graphics/KAYO_icon.png")), (40, 40))
rstamp = transform.scale((image.load("assets/graphics/Reyna_icon.png")), (40, 40))
filledRecticon = transform.scale((image.load("assets/graphics/filledRect.png")), (40, 40))
unfilledRecticon = transform.scale((image.load("assets/graphics/unfilledRect.png")), (36, 36))
filledEllipseicon = transform.scale((image.load("assets/graphics/filledEllipse.png")), (40, 40))
unfilledEllipseicon = transform.scale((image.load("assets/graphics/unfilledEllipse.png")), (40, 40))
saveIcon = transform.scale((image.load("assets/graphics/save.png")), (55, 55))
loadIcon = transform.scale((image.load("assets/graphics/load.png")), (45, 45))
undoIcon = transform.scale((image.load("assets/graphics/undo.png")), (40, 40))
redoIcon = transform.scale((image.load("assets/graphics/redo.png")), (40, 40))
logo = transform.scale((image.load("assets/graphics/logo.png")), (50, 50))
palette = transform.scale((image.load("assets/graphics/palette.jpg")), (600, 41))
lineIcon = transform.scale((image.load("assets/graphics/line.png")),(33,33))
screen.blit(saveIcon, (880, 40))
screen.blit(loadIcon, (945, 45))
screen.blit(undoIcon, undoRect)
screen.blit(redoIcon, redoRect)
screen.blit(logo, (15, 40))  # app logo
pygame.display.set_icon(logo)
pygame.display.set_caption('ValPaint')
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

tools = [pencilRect, eraserRect, paintRect, filledRect, unfilledRect, filledEllipse,
         unfilledEllipse, stampOne, stampTwo, stampThree, stampFour, stampFive, lineRect]
running = True
tool = ""
col = BLACK
bgcol = WHITE
radius = 10
draw.rect(screen, WHITE, canvasRect)
screenCap = screen.subsurface(canvasRect).copy()
thickness = 5
while running:
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
    draw.rect(screen, VALBLUE, textRect,0,50)
    font = pygame.font.SysFont('Tahoma', 24, False, False)
    screen.blit((font.render(str(thickness), True, BLACK)), (25, 755))
    if evt.type == MOUSEBUTTONDOWN:
        if evt.button == 1:  # left click
            sx, sy = evt.pos  # getting the STARTING x and y pos
            myRect = Rect(sx, sy, mx-sx, my-sy)
        # if evt.type==
    if evt.type == MOUSEBUTTONUP:
        if tool == "pencil":
            screen.set_clip(canvasRect)
            draw.line(screen, col, (oldmx, oldmy), (mx, my))
            screenCap = screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
        if tool == "eraser":
            screen.set_clip(canvasRect)
            draw.circle(screen, bgcol, (mx, my), radius)
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
    if mb[0] and loadRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        fname=filedialog.askopenfilename()
        screen.blit((image.load(fname)),canvasRect)
        screenCap = screen.subsurface(canvasRect).copy()
        screen.set_clip(None)
    # drawing all tools
    for rects in range(len(tools)):
        draw.rect(screen, VALBLUE, tools[rects],0,10)
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
    #when tool is selected
    toolList = ["pencil","eraser","paintbucket","filledRect","unfilledRect","filledEllipse","unfilledEllipse","stampOne","stampTwo","stampThree","stampFour","stampFive","line"]
    try: draw.rect(screen,GREEN,tools[toolList.index(tool)],2,10)
    except: pass
    # use the tool
    if canvasRect.collidepoint(mx, my) and mb[0]:
        screen.set_clip(canvasRect)
        if tool == "pencil":
            draw.line(screen, col, (oldmx, oldmy), (mx, my))
        if tool == "eraser":
            draw.circle(screen, bgcol, (mx, my), radius)
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

        screen.set_clip(None)  # only the canvas area can be 'updated'
    print("tool=", tool)

    # select (change) colour
    if paletteRect.collidepoint(mx, my) and mb[0]:
        col = screen.get_at((mx, my))
    oldmx, oldmy = mx, my  # oldmx oldmy is the location of the mouse in the PREVIOUS FRAME
    if mb[0] and saveRect.collidepoint(mx,my):
        fname=filedialog.asksaveasfilename(initialfile = 'My Drawing.png', defaultextension=".png", filetypes=[("All Files","*.*"),("Image Files","*.png")])
        
        
    if mb[0] and loadRect.collidepoint(mx,my):
        fname=filedialog.askopenfilename()
##        if fname is None:
##            return
        screen.blit((image.load(fname)),canvasRect)
    display.flip()

quit()
