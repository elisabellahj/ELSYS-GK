#import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import sqlite3 
import time
import pyautogui
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
def menu(abcdefgh):
    global menu 
    menu = Tk()
    
    
# HAR ENDRET HER ------ Elisabella 23.nov 17:20
    menu.title('GAMMELT NYTT')
    menu.focus_force()
    
    menu_canvas = Canvas(menu,width=1920,height=1080)
    menu_canvas.pack()

    img = PhotoImage(file= "C:\\elsys_files\\forsidebakgrunn1.png" )

    label123 = Label(menu,image = img)
    label123.place(relx=0, rely=0,relwidth=1, relheight=1)

    menu_frame = Frame(menu_canvas)
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    abcdefgh='Velkommen! '
    level34 = Label(menu_frame,text='',bg="black",font="Verdana 30",fg="white")
    level34.place(relx=0.17,rely=0.15)

    

    level = Label(label123,text='Spiller 1 velger vanskelighetsgrad:',bg="orange",font="Verdana 30")
    level.place(relx=0.5,rely=0.37, anchor=CENTER)
    #var=IntVar()

    def callback1(event):
        easy()

    def callback2(event):
        medium()
    
    def callback3(event):
        difficult()

    easyR = Button(label123,text='Lett',bg="#FD7802",font="calibri 30")
    easyR.place(relx=0.5,rely=0.48, anchor=CENTER)
    easyR.config(height = 1, width = 12)
    menu.bind('1', callback1)

    
    mediumR = Button(label123,text='Middels',bg="#9F30E2",font="calibri 30"   )
    mediumR.place(relx=0.5,rely=0.60, anchor=CENTER)
    mediumR.config(height = 1, width = 12)
    menu.bind('2', callback2)


    hardR = Button(label123,text='Vanskelig',bg="#2F77F8",font="calibri 30")
    hardR.place(relx=0.5,rely=0.72, anchor=CENTER)
    hardR.config(height = 1, width = 12)
    menu.bind('3', callback3)
    menu.overrideredirect(True)
    menu.overrideredirect(False)
    menu.attributes('-fullscreen', True)

    
    menu.mainloop()

def easy():
    global e
    global x
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    easyQ = [
                 [
                     "C:\\elsys_files\\ord_frem_til\\Q10.png",
                     "C:\\elsys_files\\ord_frem_til\\Q10A1.png",
                     "C:\\elsys_files\\ord_frem_til\\Q10A2.png",
                     "C:\\elsys_files\\ord_frem_til\\Q10A3.png",
                     "C:\\elsys_files\\ord_frem_til\\Q10A4.png"
                 ] ,
                 [
                     "C:\\elsys_files\\ord_frem_til\\Q11.png",
                     "C:\\elsys_files\\ord_frem_til\\Q11A1.png",
                     "C:\\elsys_files\\ord_frem_til\\Q11A2.png",
                     "C:\\elsys_files\\ord_frem_til\\Q11A3.png",
                     "C:\\elsys_files\\ord_frem_til\\Q11A4.png"
                 ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ]
            ]
    e = Toplevel()
    global bg
    e.title('Gammelt Nytt - Lett nivå')
    e.focus_force()
    e.overrideredirect(True)
    e.overrideredirect(False)
    e.attributes('-fullscreen', True)
    bg = PhotoImage(file=easyQ[x][0])
    easy_canvas = Canvas(e,width=3840,height=2160)
    easy_canvas.pack(fill = "both", expand = True)
    easy_canvas.create_image(0, 0, image = bg, anchor = "nw")
        
    
    global score1
    global score2
    score1 = 0
    score2 = 0
    
    
    
    answer = [
                "C:\\elsys_files\\Mammut.gif",
                "C:\\elsys_files\\Mammut.gif",
                "C:\\elsys_files\\Mammut.gif",
                "C:\\elsys_files\\Mammut.gif",
                "C:\\elsys_files\\Mammut.gif"
             ]

    global var1
    global var2
    var1 = StringVar()
    var2 = StringVar()

    def reset_color():
        a.configure(bg = '#FD7802')
        c.configure(bg = '#2F77F8')
        b.configure(bg = '#9F30E2')
        d.configure(bg = '#3ECD03')


    def callback1(event):
        global x
        assignValP1(easyQ[x][1])
        a.configure(bg = '#ffffff', borderwidth = 35)

    def callback5(event):
        global x
        assignValP2(easyQ[x][1])
        a.configure(bg = '#000000', borderwidth = 35)
    
    def callback2(event):
        global x
        assignValP1(easyQ[x][2])
        b.configure(bg = '#ffffff', borderwidth = 35)

    def callback6(event):
        global x
        assignValP2(easyQ[x][2])
        b.configure(bg = '#000000', borderwidth = 35)
    
    def callback3(event):
        global x
        assignValP1(easyQ[x][3])
        c.configure(bg = '#ffffff', borderwidth = 35)
    
    def callback7(event):
        global x
        assignValP2(easyQ[x][3])
        c.configure(bg = '#000000', borderwidth = 35)

    def callback4(event):
        global x
        assignValP1(easyQ[x][4])
        d.configure(bg = '#ffffff', borderwidth = 35)

    def callback8(event):
        global x
        assignValP2(easyQ[x][4])
        d.configure(bg = '#000000', borderwidth = 35)


    def assignValP1(val1):
        global var1
        var1 = val1
        print(val1)
    def assignValP2(val2):
        global var2
        var2 = val2
        print(var2)
    A1 = PhotoImage(file=easyQ[x][1])
    A2 = PhotoImage(file=easyQ[x][2])
    A3 = PhotoImage(file=easyQ[x][3])
    A4 = PhotoImage(file=easyQ[x][4])

    a = Button(easy_canvas, bg = '#FD7802', image = A1, borderwidth = 35)
    a.place(x = 300, y = 1700)
    e.bind('1', callback1)
    e.bind('5', callback5)

    b = Button(easy_canvas, bg = '#9F30E2', image = A3, borderwidth = 35)
    b.place(x = 1800,y=1700)
    e.bind('3', callback2)
    e.bind('7', callback6)

    c = Button(easy_canvas, bg = '#2F77F8', image = A2, borderwidth = 35)
    c.place(x = 1050,y=1700)
    e.bind('2', callback3)
    e.bind('6', callback7)

    d = Button(easy_canvas, bg = '#3ECD03', image = A4, borderwidth = 35)
    d.place(x = 2550,y=1700)
    e.bind('4', callback4)
    e.bind('8', callback8)
    


    timer = Label(e)
    timer.place(relx=0.98,rely=0.95,anchor=CENTER)
    
    def calc1():
        global score1
        global var1

        if var1 in answer:
            score1+=1
        print(score1)

    def calc2():
        global score2
        global var2
        if var2 in answer:
            score2+=1
        print(score2)

    def countDown():
        check = 0
        for k in range(10, 0, -1):
            reset_color()
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0

    def display():
        #if easyQ[x][0] == placeholder or easyQ[x][0] == placeholder
        #    a.place 

        global bg
        if len(li) == 1:
                e.destroy()
                showMark(score1, score2)
        if len(li) == 2:
            nextQuestion.configure(text='Siste spørsmål',command= lambda:[calc1(), calc2()])
                
        if li:
            global x
            x = random.choice(li[1:])

            A1.configure(file = easyQ[x][1])
            A2.configure(file = easyQ[x][2])
            A3.configure(file = easyQ[x][3])
            A4.configure(file = easyQ[x][4])
            
            a.configure(image = A1)
            
            b.configure(image = A2)
      
            c.configure(image = A3)
      
            d.configure(image = A4)

            bg.configure(file = easyQ[x][0])
            easy_canvas.update()

            calc1()
            calc2()
            li.remove(x)
            y = countDown()
            if y == -1:
                display()
    
    nextQuestion = Button(easy_canvas,command=display,text="Tid til neste", fg="white", bg="black")
    nextQuestion.place(relx=0.95,rely=0.95,anchor=CENTER)
            
        
    
    #submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
    #submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
      
    
def medium():
    global m
    global x
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    mediumQ = [
                 [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                 ] ,
                 [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                 ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ]
            ]
    m = Toplevel()
    global bg
    m.title('Gammelt Nytt - Middels nivå')
    m.focus_force()
    m.overrideredirect(True)
    m.overrideredirect(False)
    m.attributes('-fullscreen', True)
    bg = PhotoImage(file=mediumQ[x][0])
    medium_canvas = Canvas(m,width=3840,height=2160)
    medium_canvas.pack(fill = "both", expand = True)
    medium_canvas.create_image(0, 0, image = bg, anchor = "nw")
        
    global score1
    global score2
    score1 = 0
    score2 = 0
    
    
    
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^"
             ]

    global var1
    global var2
    var1 = StringVar()
    var2 = StringVar()
    def reset_color():
        a.configure(bg = '#FD7802')
        b.configure(bg = '#2F77F8')
        c.configure(bg = '#9F30E2')
        d.configure(bg = '#3ECD03')


    def callback1(event):
        global x
        assignValP1(mediumQ[x][1])
        a.configure(bg = '#ffffff', borderwidth = 35)

    def callback5(event):
        global x
        assignValP2(mediumQ[x][1])
        a.configure(bg = '#000000', borderwidth = 35)
    
    def callback2(event):
        global x
        assignValP1(mediumQ[x][2])
        b.configure(bg = '#ffffff', borderwidth = 35)

    def callback6(event):
        global x
        assignValP2(mediumQ[x][2])
        b.configure(bg = '#000000', borderwidth = 35)
    
    def callback3(event):
        global x
        assignValP1(mediumQ[x][3])
        c.configure(bg = '#ffffff', borderwidth = 35)
    
    def callback7(event):
        global x
        assignValP2(mediumQ[x][3])
        c.configure(bg = '#000000', borderwidth = 35)

    def callback4(event):
        global x
        assignValP1(mediumQ[x][4])
        d.configure(bg = '#ffffff', borderwidth = 35)

    def callback8(event):
        global x
        assignValP2(mediumQ[x][4])
        d.configure(bg = '#000000', borderwidth = 35)

    def assignValP1(val1):
        global var1
        var1 = val1
        print(val1)
    def assignValP2(val2):
        global var2
        var2 = val2
        print(var2)

    A1 = PhotoImage(file=mediumQ[x][1])
    A2 = PhotoImage(file=mediumQ[x][2])
    A3 = PhotoImage(file=mediumQ[x][3])
    A4 = PhotoImage(file=mediumQ[x][4])

    a = Button(medium_canvas, bg = '#FD7802', image = A1, borderwidth = 35)
    a.place(x = 384, y = 223)
    m.bind('1', callback1)
    m.bind('5', callback5)

    b = Button(medium_canvas, bg = '#2F77F8', image = A2, borderwidth = 35)
    b.place(x=384,y=1124)
    m.bind('3', callback2)
    m.bind('7', callback6)

    c = Button(medium_canvas, bg = '#9F30E2', image = A3, borderwidth = 35)
    c.place(x=1781,y=223)
    m.bind('2', callback3)
    m.bind('6', callback7)

    d = Button(medium_canvas, bg = '#3ECD03', image = A4, borderwidth = 35)
    d.place(x=1781,y=1124)
    m.bind('4', callback4)
    m.bind('8', callback8)
    

    timer = Label(m)
    timer.place(relx=0.98,rely=0.95,anchor=CENTER)
    
    def calc1():
        global score1
        global var1
        if var1 in answer:
            score1+=1
        print(score1)

    def calc2():
        global score2
        global var2
        if var2 in answer:
            score2+=1
        print(score2)

    def countDown():
        check = 0
        for k in range(10, 0, -1):
            reset_color()
            if k == 1:
                check=-1
            timer.configure(text=k)
            medium_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0

    def display():
        global bg
        if len(li) == 1:
                m.destroy()
                showMark(score1, score2)
        if len(li) == 2:
            nextQuestion.configure(text='Siste spørsmål',command= lambda:[calc1(), calc2()])
                
        if li:
            global x
            x = random.choice(li[1:])

            A1.configure(file = mediumQ[x][1])
            A2.configure(file = mediumQ[x][2])
            A3.configure(file = mediumQ[x][3])
            A4.configure(file = mediumQ[x][4])
            
            a.configure(image = A1)
            
            b.configure(image = A2)
      
            c.configure(image = A3)
      
            d.configure(image = A4)

            bg.configure(file = mediumQ[x][0])
            medium_canvas.update()

            calc1()
            calc2()
            li.remove(x)
            y = countDown()
            if y == -1:
                display()
    
    nextQuestion = Button(medium_canvas,command=display,text="Tid til neste", fg="white", bg="black")
    nextQuestion.place(relx=0.95,rely=0.95,anchor=CENTER)
            
        
    
    #submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
    #submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
    
      
    
def difficult():
    global h
    li = ['',0,1,2,3,4]
    global x
    x = random.choice(li[1:])
    hardQ = [
                 [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                 ] ,
                 [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                 ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ],
                [
                     "C:\\elsys_files\\Bakgrunn14k.png",
                     "C:\\elsys_files\\Mammut.gif",
                     "C:\\elsys_files\\Neshornet.gif",
                     "C:\\elsys_files\\Pukkellaks.gif",
                     "C:\\elsys_files\\Spy.gif"
                ]
            ]
    h = Toplevel()
    global bg
    h.title('Gammelt Nytt - Middels nivå')
    h.focus_force()
    h.overrideredirect(True)
    h.overrideredirect(False)
    h.attributes('-fullscreen', True)
    bg = PhotoImage(file=hardQ[x][0])
    hard_canvas = Canvas(h,width=3840,height=2160)
    hard_canvas.pack(fill = "both", expand = True)
    hard_canvas.create_image(0, 0, image = bg, anchor = "nw")
        
    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score1
    global score2
    score1 = 0
    score2 = 0
    
    
    
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^"
             ]

    global var1
    global var2
    var1 = StringVar()
    var2 = StringVar()
    def reset_color():
        a.configure(bg = '#FD7802')
        b.configure(bg = '#2F77F8')
        c.configure(bg = '#9F30E2')
        d.configure(bg = '#3ECD03')

    def callback1(event):
        global x
        assignValP1(hardQ[x][1])
        a.configure(bg = '#ffffff', borderwidth = 35)

    def callback5(event):
        global x
        assignValP2(hardQ[x][1])
        a.configure(bg = '#000000', borderwidth = 35)
    
    def callback2(event):
        global x
        assignValP1(hardQ[x][2])
        b.configure(bg = '#ffffff', borderwidth = 35)

    def callback6(event):
        global x
        assignValP2(hardQ[x][2])
        b.configure(bg = '#000000', borderwidth = 35)
    
    def callback3(event):
        global x
        assignValP1(hardQ[x][3])
        c.configure(bg = '#ffffff', borderwidth = 35)
    
    def callback7(event):
        global x
        assignValP2(hardQ[x][3])
        c.configure(bg = '#000000', borderwidth = 35)

    def callback4(event):
        global x
        assignValP1(hardQ[x][4])
        d.configure(bg = '#ffffff', borderwidth = 35)

    def callback8(event):
        global x
        assignValP2(hardQ[x][4])
        d.configure(bg = '#000000', borderwidth = 35)

    def assignValP1(val1):
        global var1
        var1 = val1
        print(val1)
    def assignValP2(val2):
        global var2
        var2 = val2
        print(var2)
    A1 = PhotoImage(file=hardQ[x][1])
    A2 = PhotoImage(file=hardQ[x][2])
    A3 = PhotoImage(file=hardQ[x][3])
    A4 = PhotoImage(file=hardQ[x][4])

    a = Button(hard_canvas, bg = '#FD7802', image = A1, borderwidth = 35)
    a.place(x = 384, y = 223)
    h.bind('1', callback1)
    h.bind('5', callback5)

    b = Button(hard_canvas, bg = '#2F77F8', image = A2, borderwidth = 35)
    b.place(x=384,y=1124)
    h.bind('3', callback2)
    h.bind('7', callback6)

    c = Button(hard_canvas, bg = '#9F30E2', image = A3, borderwidth = 35)
    c.place(x=1781,y=223)
    h.bind('2', callback3)
    h.bind('6', callback7)

    d = Button(hard_canvas, bg = '#3ECD03', image = A4, borderwidth = 35)
    d.place(x=1781,y=1124)
    h.bind('4', callback4)
    h.bind('8', callback8)
    

    timer = Label(h)
    timer.place(relx=0.98,rely=0.95,anchor=CENTER)
    
    def calc1():
        global score1
        global var1
        if var1 in answer:
            score1+=1
        print(score1)

    def calc2():
        global score2
        global var2
        if var2 in answer:
            score2+=1
        print(score2)

    def countDown():
        check = 0
        for k in range(10, 0, -1):
            reset_color()
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0

    def display():
        global bg
        if len(li) == 1:
                h.destroy()
                showMark(score1, score2)
        if len(li) == 2:
            nextQuestion.configure(text='Siste spørsmål',command= lambda:[calc1(), calc2()])
                
        if li:
            global x
            x = random.choice(li[1:])

            A1.configure(file = hardQ[x][1])
            A2.configure(file = hardQ[x][2])
            A3.configure(file = hardQ[x][3])
            A4.configure(file = hardQ[x][4])
            
            a.configure(image = A1)
            
            b.configure(image = A2)
      
            c.configure(image = A3)
      
            d.configure(image = A4)
            reset_color()
            bg.configure(file = hardQ[x][0])
            hard_canvas.update()

            calc1()
            calc2()
            li.remove(x)
            y = countDown()
            if y == -1:
                display()
    
    nextQuestion = Button(hard_canvas,command=display,text="Tid til neste", fg="white", bg="black")
    nextQuestion.place(relx=0.95,rely=0.95,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()
    
      
    

def showMark(score1, score2):

    data1 = {'Spiller': ['Spiller 1','Spiller 2'],
                'Score': [score1, score2]
                }
    df1 = DataFrame(data1,columns=['Spiller','Score'])

    root= Tk() 
    button1 = Button(root, text="Spiller 1: Trykk på oransje for å prøve på nytt!", )
    button1.place(x=1, y=1)
    figure1 = plt.Figure(figsize=(16,9), dpi=100)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    root.after(1500, lambda: root.focus_force())
    
    def callback(event):
        root.destroy()
    root.bind('1', callback)
    
    figure1 = plt.Figure(figsize=(16,9), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    df1 = df1[['Spiller','Score']].groupby('Spiller').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Spiller 1: Trykk på oransje for å gå videre!')



menu(" ")
