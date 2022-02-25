from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
rep = 0
cd = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global rep
    window.after_cancel(cd)
    rep = 0
    canvas.itemconfig(timer, text='25:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global rep
    rep += 1

    l_b_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    s_b_sec = SHORT_BREAK_MIN * 60

    if rep in [1,3,5,7]:
        countdown(work_sec)
        title.config(text='WORK', fg=GREEN)
    elif rep in [2,4,6]:
        countdown(s_b_sec)
        title.config(text='BREAK', fg=PINK)
    elif rep == 8:
        countdown(l_b_sec)
        title.config(text='BREAK', fg=RED)
        rep = 0 
        check['text'] == ''
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global rep
    global cd
    minutes = count//60
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{seconds}'

    if count > 0:
        canvas.itemconfig(timer, text=f'{minutes}:{seconds}')
        cd = window.after(1000, countdown, count-1)
    else:
        window.focus_force()
        start()
        if not rep % 2:
            check['text'] += CHECKMARK
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


#Timer
title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
title.grid(column=1, row=0)

#Tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="25:00", fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1, row=1)

#Start button
start_b = Button(text='Start', command=start, highlightthickness=0)
start_b.grid(column=0, row=2)

#Reset button
reset_b = Button(text='Reset', command=reset, highlightthickness=0)
reset_b.grid(column=3, row=2)

#Checkmarks
check = Label(text="", fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)

window.mainloop()