import pygame as p

p.init()

# --- Professional Banking Palette ---
WHITE = (245, 245, 245)
BLACK = (10, 10, 15)        # Deepest Navy/Black
NAVY_DARK = (15, 25, 45)    # Top Gradient
NAVY_LIGHT = (30, 50, 85)   # Bottom Gradient
ACCENT_BLUE = (0, 120, 215) # For selected buttons
SOFT_BLUE = (40, 60, 100)   # For idle buttons
CYAN = (0, 255, 255)        # For headers
GOLD = (255, 215, 0)        # For balance

# Fonts
font_small = p.font.SysFont("Segoe UI", 25)
font_med = p.font.SysFont("Segoe UI", 30, bold=True)
font_large = p.font.SysFont("Segoe UI", 45, bold=True)
font_header = p.font.SysFont("Segoe UI", 55, bold=True)

# App State
app_locked = True
user_input, pass_input = "", ""
login_step = 1 

option = 1
opt = 1
b_opt = 1
t_opt = 1
main_selection = 0
banking_selection = 0
committee_selection = 0
transaction_selection = 0 

# Logic Variables
input_mode = False 
current_text = "" 
temp_comm_name = "" 
Total_balance = 10000 
committees = [] 
transactions = [] 
selected_comm_idx = -1

# --- FILE HANDLING ---
def save_all():
    with open("database.txt", "w") as f:
        for c in committees:
            mems = ",".join(c["members"])
            f.write(f"{c['name']}|{c['contribution']}|{mems}\n")
    with open("transactions.txt", "w") as f:
        for t in transactions:
            f.write(f"{t['type']}|{t['amount']}|{t['note']}\n")

def load_all():
    global committees, transactions
    try:
        with open("database.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    m_list = parts[2].split(",") if parts[2] else []
                    committees.append({"name": parts[0], "contribution": int(parts[1]), "members": m_list})
        with open("transactions.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    transactions.append({"type": parts[0], "amount": int(parts[1]), "note": parts[2]})
    except: pass 

load_all()

gd = p.display.set_mode((1100, 600))
p.display.set_caption("ART Online Banking")

def draw_gradient(surface, color_top, color_bottom):
    width, height = surface.get_size()
    for y in range(height):
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        p.draw.line(surface, (r, g, b), (0, y), (width, y))

def draw_button(x, y, w, h, text, is_selected):
    # Shadow
    p.draw.rect(gd, (5, 5, 10), (x+4, y+4, w, h), border_radius=12)
    # Button Surface
    color = ACCENT_BLUE if is_selected else SOFT_BLUE
    p.draw.rect(gd, color, (x, y, w, h), border_radius=12)
    # Border
    if is_selected: 
        p.draw.rect(gd, WHITE, (x, y, w, h), 2, border_radius=12)
    
    txt_surface = font_med.render(text, True, WHITE)
    gd.blit(txt_surface, txt_surface.get_rect(center=(x + w//2, y + h//2)))

# ----------------- COMMITTEE SECTION ----------------- #

def committee_ui(e=None):
    global opt, committee_selection, committees, current_text, input_mode, selected_comm_idx, temp_comm_name, main_selection
    if e and e.type == p.KEYDOWN:
        if committee_selection == 0:
            if e.key == p.K_UP and opt > 1: opt -= 1
            elif e.key == p.K_DOWN and opt < 4: opt += 1
            elif e.key == p.K_RETURN:
                if opt == 4:
                    main_selection = 0; return
                committee_selection = opt; current_text = ""; opt = 1 
        elif committee_selection == 1:
            if e.key == p.K_RETURN and current_text:
                temp_comm_name = current_text; committee_selection = 4; opt = 1 
            elif e.key == p.K_BACKSPACE: current_text = current_text[:-1]
            else: current_text += e.unicode
        elif committee_selection == 4:
            if e.key == p.K_UP and opt > 1: opt -= 1
            elif e.key == p.K_DOWN and opt < 3: opt += 1
            elif e.key == p.K_RETURN:
                amts = [1000, 2000, 5000]
                committees.append({"name": temp_comm_name, "contribution": amts[opt-1], "members": []})
                save_all(); committee_selection = 0; opt = 1
        elif committee_selection == 2:
            if committees:
                if e.key == p.K_UP and opt > 1: opt -= 1
                elif e.key == p.K_DOWN and opt < len(committees): opt += 1
                elif e.key == p.K_RETURN:
                    selected_comm_idx = opt - 1; committee_selection = 5; current_text = ""
        elif committee_selection == 5:
            if e.key == p.K_RETURN and current_text:
                committees[selected_comm_idx]["members"].append(current_text)
                save_all(); committee_selection = 0; opt = 2
            elif e.key == p.K_BACKSPACE: current_text = current_text[:-1]
            else: current_text += e.unicode

    draw_gradient(gd, NAVY_DARK, NAVY_LIGHT)
    if committee_selection == 0:
        items = ["Create Committee", "Add Member", "View Committees", "Back"]
        for i, item in enumerate(items, 1): draw_button(420, 170 + (i-1)*75, 260, 60, item, opt == i)
    elif committee_selection == 1:
        p.draw.rect(gd, WHITE, (250, 250, 600, 100), border_radius=15); gd.blit(font_med.render(f"Enter Name: {current_text}", True, BLACK), (270, 285))
    elif committee_selection == 4:
        gd.blit(font_med.render(f"Select Amount for {temp_comm_name}:", True, WHITE), (350, 100))
        for i, a in enumerate(["1000", "2000", "5000"], 1): draw_button(420, 170 + (i-1)*80, 260, 65, "Rs. "+a, opt == i)
    elif committee_selection == 2:
        p.draw.rect(gd, (0,0,0,100), (0, 110, 1100, 50))
        gd.blit(font_med.render("Select a Committee to Add Member", True, WHITE), (320, 115))
        for i, c in enumerate(committees, 1): draw_button(350, 180 + (i-1)*70, 400, 60, c['name'], opt == i)
    elif committee_selection == 5:
        p.draw.rect(gd, (0,0,0,100), (0, 110, 1100, 50))
        gd.blit(font_med.render(f"Adding to: {committees[selected_comm_idx]['name']}", True, WHITE), (350, 115))
        p.draw.rect(gd, WHITE, (250, 250, 600, 100), border_radius=15); gd.blit(font_med.render(f"Member Name: {current_text}", True, BLACK), (270, 285))
    elif committee_selection == 3:
        y = 130
        for c in committees:
            p.draw.rect(gd, (255,255,255,180), (200, y, 700, 75), border_radius=10)
            gd.blit(font_med.render(f"{c['name']} - Rs.{c['contribution']}", True, NAVY_DARK), (220, y + 5))
            gd.blit(font_small.render(f"Members: {', '.join(c['members'])}", True, (60,60,60)), (220, y + 38)); y += 90

# ----------------- BANKING & TRANSACTIONS ----------------- #

def transactions_ui(e=None):
    global t_opt, transaction_selection, transactions, main_selection
    if e and e.type == p.KEYDOWN:
        if transaction_selection == 0:
            if e.key == p.K_UP and t_opt > 1: t_opt -= 1
            elif e.key == p.K_DOWN and t_opt < 4: t_opt += 1
            elif e.key == p.K_RETURN:
                if t_opt == 4:
                    main_selection = 0; return 
                transaction_selection = t_opt
        elif e.key in [p.K_ESCAPE, p.K_BACKSPACE]:
            transaction_selection = 0

    draw_gradient(gd, BLACK, NAVY_DARK)
    if transaction_selection == 0:
        opts = ["Sent History", "Received History", "All History", "Back"]
        for i, o in enumerate(opts, 1): draw_button(420, 170 + (i-1)*75, 260, 60, o, t_opt == i)
    else:
        y, titles = 150, ["Sent History", "Received History", "Full Statement"]
        gd.blit(font_med.render(titles[transaction_selection-1], True, CYAN), (450, 90))
        filtered = transactions
        if transaction_selection == 1: filtered = [t for t in transactions if t['type'] == "Sent"]
        elif transaction_selection == 2: filtered = [t for t in transactions if t['type'] == "Recv"]
        if not filtered: gd.blit(font_med.render("No records found.", True, WHITE), (430, 280))
        else:
            for t in filtered[-6:]:
                color = (255, 100, 100) if t['type'] == "Sent" else (100, 255, 100)
                p.draw.rect(gd, (255,255,255,20), (200, y, 700, 50), border_radius=10)
                gd.blit(font_small.render(f"{t['type']} | Rs. {t['amount']} | {t['note']}", True, color), (220, y + 10)); y += 60

def send_money_ui(e=None):
    global banking_selection, Total_balance, b_opt, input_mode, current_text, transactions
    if e and e.type == p.KEYDOWN:
        if not input_mode:
            if e.key == p.K_UP and b_opt > 1: b_opt -= 1
            elif e.key == p.K_DOWN and b_opt < 5: b_opt += 1
            elif e.key == p.K_RETURN:
                if b_opt == 5:
                    banking_selection = 0; b_opt = 2; return
                amt = 0
                if b_opt == 1: amt = 500
                elif b_opt == 2: amt = 1000
                elif b_opt == 3: amt = 5000
                elif b_opt == 4: input_mode = True; current_text = ""
                if amt > 0 and Total_balance >= amt:
                    Total_balance -= amt
                    transactions.append({"type": "Sent", "amount": amt, "note": "Cash Transfer"}); save_all()
        else:
            if e.key == p.K_RETURN:
                val = int(current_text) if (current_text and current_text.isdigit()) else 0
                if 0 < val <= Total_balance:
                    Total_balance -= val
                    transactions.append({"type": "Sent", "amount": val, "note": "Custom Transfer"}); save_all()
                input_mode = False; current_text = ""
            elif e.key == p.K_BACKSPACE: current_text = current_text[:-1]
            elif e.unicode.isdigit(): current_text += e.unicode

    draw_gradient(gd, NAVY_DARK, BLACK)
    p.draw.rect(gd, (0,0,0,150), (0, 110, 1100, 55))
    bal_txt = font_med.render(f"Balance: Rs. {Total_balance}", True, GOLD)
    gd.blit(bal_txt, (1100//2 - bal_txt.get_width()//2, 118))
    for i, lbl in enumerate(["Send 500", "Send 1000", "Send 5000", "Custom: " + current_text if input_mode else "Custom", "Back"], 1):
        draw_button(400, 180 + (i-1)*70, 300, 60, lbl, b_opt == i)

# --- MAIN LOOP ---
while True:
    header = font_header.render("ART BANKING", True, WHITE)
    e = None
    for event in p.event.get():
        if event.type == p.QUIT: p.quit(); exit()
        if app_locked:
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    if login_step == 1: login_step = 2
                    else:
                        if user_input == "asadaziz" and pass_input == "123":
                            app_locked = False
                        else: user_input = ""; pass_input = ""; login_step = 1
                elif event.key == p.K_BACKSPACE:
                    if login_step == 1: user_input = user_input[:-1]
                    else: pass_input = pass_input[:-1]
                else:
                    if login_step == 1: user_input += event.unicode
                    else: pass_input += event.unicode
        else:
            if event.type == p.KEYDOWN:
                if event.key in [p.K_ESCAPE, p.K_BACKSPACE]:
                    if input_mode: input_mode = False
                    elif committee_selection: committee_selection = 0; opt = 2 
                    elif banking_selection: banking_selection = 0; b_opt = 1
                    elif transaction_selection: transaction_selection = 0; t_opt = 1
                    elif main_selection: main_selection = 0; option = 1
                
                if main_selection == 0:
                    if event.key == p.K_UP and option > 1: option -= 1
                    elif event.key == p.K_DOWN and option < 4: option += 1
                    elif event.key == p.K_RETURN:
                        if option == 4: p.quit(); exit()
                        main_selection = option; b_opt = 1; opt = 1; t_opt = 1
                else: e = event

    if not app_locked:
        if main_selection == 1:
            if banking_selection == 2: send_money_ui(e)
            else:
                draw_gradient(gd, NAVY_DARK, NAVY_LIGHT)
                for i, label in enumerate(["Check Balance", "Send Money", "Back"], 1):
                    txt = f"Bal: {Total_balance}" if (i==1 and banking_selection==1) else label
                    draw_button(420, 220 + (i-1)*95, 260, 65, txt, b_opt == i)
                if e and e.type == p.KEYDOWN:
                    if e.key == p.K_UP and b_opt > 1: b_opt -= 1
                    elif e.key == p.K_DOWN and b_opt < 3: b_opt += 1
                    elif e.key == p.K_RETURN:
                        if b_opt == 3: main_selection = 0; b_opt = 1
                        else: banking_selection = b_opt; b_opt = 1
        elif main_selection == 2: committee_ui(e)
        elif main_selection == 3: transactions_ui(e)
        elif main_selection == 0:
            draw_gradient(gd, NAVY_DARK, NAVY_LIGHT)
            items = ["Banking", "Committee", "Transactions", "Exit"]
            for i, item in enumerate(items, 1): draw_button(420, 160 + (i-1)*85, 260, 65, item, option == i)
    else:
        draw_gradient(gd, BLACK, NAVY_DARK)
        gd.blit(font_med.render("SECURE ACCESS", True, WHITE), (445, 180))
        p.draw.rect(gd, WHITE, (400, 240, 300, 50), 2, border_radius=8)
        gd.blit(font_small.render("User: " + user_input, True, CYAN), (410, 250))
        p.draw.rect(gd, WHITE, (400, 310, 300, 50), 2, border_radius=8)
        gd.blit(font_small.render("Pass: " + "*"*len(pass_input), True, CYAN), (410, 320))

    gd.blit(header, (gd.get_width()//2 - header.get_width()//2, 40))
    p.display.update()