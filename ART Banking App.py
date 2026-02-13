import pygame as p
p.init()

slidercolor = (139, 0, 0)
font_small = p.font.SysFont(None, 25)
option = 1
opt = 1
selected = 0

gd = p.display.set_mode((1100, 600))
def draw_gradient(surface, color_top, color_bottom):
    """Draw a vertical gradient background"""
    width, height = surface.get_size()
    for y in range(height):
        # Calculate blend ratio between top and bottom color
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        p.draw.line(surface, (r, g, b), (0, y), (width, y))

def menu(option):
    global font_small
    draw_gradient(gd, (255, 0, 40), (0, 204, 204))   
    font = p.font.SysFont(None, 30)
    if option == 1:
        p.draw.rect(gd, slidercolor, (420, 170, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 170, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 175, 250, 50), border_radius = 10)
    text = font.render("Start Analysing", True, (0, 0, 0))
    gd.blit(text, (470, 190))
    
    if option == 2:
        p.draw.rect(gd, slidercolor, (420, 245, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 245, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 250, 250, 50), border_radius = 10)
    text = font.render("About", True, (0, 0, 0))
    gd.blit(text, (513, 265))
    
    if option == 3:
        p.draw.rect(gd, slidercolor, (420, 320, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 320, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 325, 250, 50), border_radius = 10)
    text = font.render("Exit", True, (0, 0, 0))
    gd.blit(text, (520, 340))
    
    # --- Footer ---
    footer = font_small.render("Version 1.0 | © 2026 ART Online Banking App", True, (128, 0, 0))
    gd.blit(footer, (365, 520))

def committee(e = None):
    global font_small, opt

    # Queries Input Managment
    if e.key == p.K_UP:
        opt = 3 - opt
    elif e.key == p.K_DOWN:
        opt = 3 - opt

        # elif e.key == p.K_RETURN:
            
    draw_gradient(gd, (255, 0, 40), (0, 204, 204))   
    font = p.font.SysFont(None, 30)
    if opt == 1:
        p.draw.rect(gd, slidercolor, (420, 170, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 170, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 175, 250, 50), border_radius = 10)
    text = font.render("Create Committee", True, (0, 0, 0))
    gd.blit(text, (470, 190))
    
    if opt == 2:
        p.draw.rect(gd, slidercolor, (420, 245, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 245, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 250, 250, 50), border_radius = 10)
    text = font.render("Add a Member", True, (0, 0, 0))
    gd.blit(text, (513, 265))
    
    if opt == 3:
        p.draw.rect(gd, slidercolor, (420, 320, 260, 60), border_radius = 15)
    else:
        p.draw.rect(gd, (128, 0, 0), (420, 320, 260, 60), border_radius = 15)
        p.draw.rect(gd, (165, 42, 42), (425, 325, 250, 50), border_radius = 10)
    text = font.render("View Committies", True, (0, 0, 0))
    gd.blit(text, (520, 340))
    
    # --- Footer ---
    footer = font_small.render("Version 1.0 | © 2026 ART Online Banking App", True, (128, 0, 0))
    gd.blit(footer, (365, 520))    
 
while True:
    
    if selected == 0:
        menu(option)

    font = p.font.SysFont('Comic Sans MS', 40)
    header = font.render("ART Banking App", True, (40, 200, 200))
    gd.blit(header, (260, 55))
    e = None
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        elif event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE or event.key == p.K_BACKSPACE:
                if selected == 1 or selected == 2:
                    gd.fill((220,240,255))
                    selected = 0
                elif selected == -1:
                    gd.fill((220,240,255))
                    score = 0
                    age = 20
                    weight = 50
                    r = 100
                    query = 1
                    barout = 1
                    pred_active = 0
                    selected = 0
                else:
                    p.quit()
                    exit()
            if selected == 0:
                if event.key == p.K_UP and option > 1:
                    option -= 1
                elif event.key == p.K_DOWN and option < 3:
                    option += 1
                elif event.key == p.K_RETURN:
                    if selected == -1:
                        selected = 0
                    if option == 1:
                        selected = 1
                    elif option == 2:
                        selected = 2
                    elif option == 3:
                        p.quit()
                        exit()
            else:
                e = event
    if selected == 1:
        committee(e)
    # if selected == 2:
    #     about()
    
    
    p.display.update()


p.quit()