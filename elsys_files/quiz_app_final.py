#import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
import pyautogui
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="orange")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="white",bg="orange")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Quiz App')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Quiz App SignUp",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='white',bg='black')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='white',bg='black')
    clabel.place(relx=0.217,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()"""

def menu(abcdefgh):
    global menu 
    menu = Tk()
    
    
# HAR ENDRET HER ------ Elisabella 23.nov 17:20
    menu.title('GAMMELT NYTT')
    menu.focus_force()
    
    menu_canvas = Canvas(menu,width=1920,height=1080)
    menu_canvas.pack()

    img = PhotoImage(file= "C:\\elsys_files\\forsidebakgrunn1.png" )
    img = img.zoom(9)
    img = img.subsample(5)

    label123 = Label(menu,image = img)
    label123.place(relx=0, rely=0,relwidth=1, relheight=1)

    #wel = Label(label123,fg="white",bg="orange") 
    #wel.config(font=('Arva 30'))
    #wel.place(relx=0.1,rely=0.02)

    

    menu_frame = Frame(menu_canvas)
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    '''wel = Label(menu_canvas,text=' Velkommen til Gammelt Nytt! ',fg="white",bg="orange") 
    wel.config(font=('Arva 30'))
    wel.place(relx=0.1,rely=0.02)'''
    
    abcdefgh='Velkommen! '
    level34 = Label(menu_frame,text='',bg="black",font="Verdana 30",fg="white")
    level34.place(relx=0.17,rely=0.15)

    

    level = Label(label123,text='Spiller 1 velger vanskelighetsgrad:',bg="orange",font="Verdana 30")
    level.place(relx=0.5,rely=0.37, anchor=CENTER)
    #var=IntVar()

    """def changeVal(value):
        global var
        print("Denne kjø1rer")
        var = value
        return var"""
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
# Endret til hit ------------

    """print(var)
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass"""

    """letsgo = Button(menu_frame,text="Let's Go",bg="black",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)"""
    menu.mainloop()
"""def easy():
    
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')
    
    easy_canvas = Canvas(e,width=1920,height=1080,bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="#00FF00")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQ = [
                 [
                     "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
                     "[1, 0, 2, ‘hello’, '', []]",
                     "Error",
                     "[1, 2, ‘hello’]",
                     "[1, 0, 2, 0, ‘hello’, '', []]" 
                 ] ,
                 [
                     "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"
                     
                 ],
                [
                    "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10" ,
                    "30.8",
                    "27.2",
                    "28.4",
                    "30.0"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ]
            ]
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2)
    
    

    var1 = StringVar()
    var2 = StringVar()
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()


    def calc(var):
        global score
        if (var in answer):
            score+=1
        display()
    
    a = Button(easy_frame,text=easyQ[x][1],font="calibri 10", bg="#00FF00", command=calc(easyQ[x][1]))
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    a = Button(easy_frame,text=easyQ[x][2],font="calibri 10", bg="#00FF00", command=calc(easyQ[x][2]))
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    c = Button(easy_frame,text=easyQ[x][3],font="calibri 10", bg="#00FF00", command=calc(easyQ[x][3]))
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    a = Button(easy_frame,text=easyQ[x][4],font="calibri 10", bg="#00FF00", command=calc(easyQ[x][4]))
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
"""
def easy():
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')
    e.focus_force()
    easy_canvas = Canvas(e,width=1920,height=1080,bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="#BADA55")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        
    
    def countDown():
        check = 0
        for k in range(2, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
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
    
    
    easyQ = [
                 [
                     "Spørsmål 1 \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
                     "[1, 0, 2, ‘hello’, '', []]",
                     "Error",
                     "[1, 2, ‘hello’]",
                     "[1, 0, 2, 0, ‘hello’, '', []]",

                 ] ,
                 [
                     "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"
                     
                 ],
                [
                    "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10" ,
                    "30.8",
                    "27.2",
                    "28.4",
                    "30.0"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ]
            ]
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    ques = Label(easy_frame,text=easyQ[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
    global var1
    global var2
    var1 = StringVar()
    var2 = StringVar()


    def callback1(event):
        global x
        assignValP1(easyQ[x][1])
    
    def callback5(event):
        global x
        assignValP2(easyQ[x][1])
    
    def callback2(event):
        global x
        assignValP1(easyQ[x][2])
    
    def callback6(event):
        global x
        assignValP2(easyQ[x][2])
    
    def callback3(event):
        global x
        assignValP1(easyQ[x][3])
    
    def callback7(event):
        global x
        assignValP2(easyQ[x][3])
    
    def callback4(event):
        global x
        assignValP1(easyQ[x][4])

    def callback8(event):
        global x
        assignValP2(easyQ[x][4])


    def assignValP1(val1):
        global var1
        var1 = val1
        print(val1)
    def assignValP2(val2):
        global var2
        var2 = val2
        print(var2)


    a = Button(easy_frame,text=easyQ[x][1],font="calibri 10", bg="#00FF00")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)
    e.bind('1', callback1)
    e.bind('5', callback5)

    b = Button(easy_frame,text=easyQ[x][2],font="calibri 10", bg="#00FF00")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)
    e.bind('2', callback2)
    e.bind('6', callback6)

    c = Button(easy_frame,text=easyQ[x][3],font="calibri 10", bg="#00FF00")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 
    e.bind('3', callback3)
    e.bind('7', callback7)

    d = Button(easy_frame,text=easyQ[x][4],font="calibri 10", bg="#00FF00")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    e.bind('4', callback4)
    e.bind('8', callback8)
    

    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    def calc1():
        global score1
        global var1
        print(f"Dette er var1{var1}")
        print(f"Dette er listen{answer}")

        if var1 in answer:
            score1+=1
        print(score1)

    def calc2():
        global score2
        global var2
        if var2 in answer:
            score2+=1
        print(score2)


    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score1, score2)
        if len(li) == 2:
            nextQuestion.configure(text='End',command= lambda:[calc1(), calc2()])
                
        if li:
            global x
            x = random.choice(li[1:])
            #print(x)
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1])
            
            b.configure(text=easyQ[x][2])
      
            c.configure(text=easyQ[x][3])
      
            d.configure(text=easyQ[x][4])

            calc1()
            calc2()
            li.remove(x)
            y = countDown()
            if y == -1:
                display()
    
    nextQuestion = Button(easy_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
            
        
    
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
    m = Tk()
    m.title('Quiz App - Medium Level')
    m.focus_force()
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="#A1A100")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
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
    
    mediumQ = [
                [
                    "Which of the following is not an exception handling keyword in Python?",
                     "accept",
                     "finally",
                     "except",
                     "try"
                ],
                [
                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
                    "3",
                    "5",
                    "25",
                    "1"
                ],
                [
                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
                    "Error",
                    "None",
                    "25",
                    "2"
                ],
                [
                    "print(0xA + 0xB + 0xC):",
                    "0xA0xB0xC",
                    "Error",
                    "0x22",
                    "33"
                ],
                [
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ], 
            ]
    answer = [
            "accept",
            "1",
            "25",
            "33",
            "none of the mentioned"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    ques = Label(med_frame,text=mediumQ[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
    global var1
    global var2
    var1 = StringVar()
    var2 = StringVar()


    def callback1(event):
        global x
        assignValP1(mediumQ[x][1])
    
    def callback5(event):
        global x
        assignValP2(mediumQ[x][1])
    
    def callback2(event):
        global x
        assignValP1(mediumQ[x][2])
    
    def callback6(event):
        global x
        assignValP2(mediumQ[x][2])
    
    def callback3(event):
        global x
        assignValP1(mediumQ[x][3])
    
    def callback7(event):
        global x
        assignValP2(mediumQ[x][3])
    
    def callback4(event):
        global x
        assignValP1(mediumQ[x][4])

    def callback8(event):
        global x
        assignValP2(mediumQ[x][4])


    def assignValP1(val1):
        global var1
        var1 = val1
        print(val1)
    def assignValP2(val2):
        global var2
        var2 = val2
        print(var2)


    a = Button(med_frame,text=mediumQ[x][1],font="calibri 10", bg="#00FF00")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)
    m.bind('1', callback1)
    m.bind('5', callback5)

    b = Button(med_frame,text=mediumQ[x][2],font="calibri 10", bg="#00FF00")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)
    m.bind('2', callback2)
    m.bind('6', callback6)

    c = Button(med_frame,text=mediumQ[x][3],font="calibri 10", bg="#00FF00")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 
    m.bind('3', callback3)
    m.bind('7', callback7)

    d = Button(med_frame,text=mediumQ[x][4],font="calibri 10", bg="#00FF00")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    m.bind('4', callback4)
    m.bind('8', callback8)
    

    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    def calc1():
        global score1
        global var1
        print(f"Dette er var1{var1}")
        print(f"Dette er listen{answer}")

        if var1 in answer:
            score1+=1
        print(score1)

    def calc2():
        global score2
        global var2
        if var2 in answer:
            score2+=1
        print(score2)


    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score1)
                #showMark(score2)
        if len(li) == 2:
            nextQuestion.configure(text='End',command= lambda:[calc1(), calc2()])
                
        if li:
            global x
            x = random.choice(li[1:])
            #print(x)
            ques.configure(text=mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1])
            
            b.configure(text=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4])

            calc1()
            calc2()
            li.remove(x)
            y = countDown()
            if y == -1:
                display()
    
    nextQuestion = Button(med_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
            
        
    
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
    count=0
    h = Tk()
    h.title('Quiz App - Hard Level')
    h.focus_force()
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="#008080")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
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

    hardQ = [
                [
       "All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],
    [
        "Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],
    [
     "Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"   
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ] 
            
]
    answer = [
            "None of the mentioned",
            "in",
            "(1,2,3)",
            "4",
            "error"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    ques = Label(hard_frame,text=hardQ[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)
    global var1
    global var2
    var1 = StringVar()
    var2 = StringVar()


    def callback1(event):
        global x
        assignValP1(hardQ[x][1])
    
    def callback5(event):
        global x
        assignValP2(hardQ[x][1])
    
    def callback2(event):
        global x
        assignValP1(hardQ[x][2])
    
    def callback6(event):
        global x
        assignValP2(hardQ[x][2])
    
    def callback3(event):
        global x
        assignValP1(hardQ[x][3])
    
    def callback7(event):
        global x
        assignValP2(hardQ[x][3])
    
    def callback4(event):
        global x
        assignValP1(hardQ[x][4])

    def callback8(event):
        global x
        assignValP2(hardQ[x][4])


    def assignValP1(val1):
        global var1
        var1 = val1
        print(val1)
    def assignValP2(val2):
        global var2
        var2 = val2
        print(var2)


    a = Button(hard_frame,text=hardQ[x][1],font="calibri 10", bg="#00FF00")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)
    h.bind('1', callback1)
    h.bind('5', callback5)

    b = Button(hard_frame,text=hardQ[x][2],font="calibri 10", bg="#00FF00")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)
    h.bind('2', callback2)
    hard_frame.bind('6', callback6)

    c = Button(hard_frame,text=hardQ[x][3],font="calibri 10", bg="#00FF00")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 
    h.bind('3', callback3)
    h.bind('7', callback7)

    d = Button(hard_frame,text=hardQ[x][4],font="calibri 10", bg="#00FF00")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    h.bind('4', callback4)
    h.bind('8', callback8)
    

    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    def calc1():
        global score1
        global var1
        print(f"Dette er var1{var1}")
        print(f"Dette er listen{answer}")

        if var1 in answer:
            score1+=1
        print(score1)

    def calc2():
        global score2
        global var2
        if var2 in answer:
            score2+=1
        print(score2)


    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score1)
                #showMark(score2)
        if len(li) == 2:
            nextQuestion.configure(text='End',command= lambda:[calc1(), calc2()])
                
        if li:
            global x
            x = random.choice(li[1:])
            #print(x)
            ques.configure(text=hardQ[x][0])
            
            a.configure(text=hardQ[x][1])
            
            b.configure(text=hardQ[x][2])
      
            c.configure(text=hardQ[x][3])
      
            d.configure(text=hardQ[x][4])

            calc1()
            calc2()
            li.remove(x)
            y = countDown()
            if y == -1:
                display()
    
    nextQuestion = Button(hard_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
            
        
    
    #submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
    #submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(score1, score2):

    tempList = [['Spiller 1', str(score1)],['Spiller 2', str(score2)]]
    tempList.sort(key=lambda e: e[1], reverse=True)
    
    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, score))


cols = ('Position', 'Name', 'Score')
listBox = ttk.Treeview(scores, columns=cols, show='headings')
# set column headings


scores = Tk() 
label = Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
scores.after(1000, lambda: sh.focus_force())
    # set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(scores, text="Show scores", width=15, command=showHighScore).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)
    
"""def callback68(event):
        sh.destroy()
        menu
        time.sleep(2)
        pyautogui.press("tab")

    
    b24=Button(text="Oransje for nytt forsøk", bg="black", fg="white")
    b24.pack()
    sh.bind('1', callback68)
"""
def score_chart(score1, score2):

        data1 = {'Spiller': ['Spiller1','Spiller2'],
                'Score': [points1, points2]
                }
        df1 = DataFrame(data1,columns=['Spiller','Score'])

        
        root= Tk() 
        
        figure1 = plt.Figure(figsize=(6,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1 = df1[['Spiller','Score']].groupby('Spiller').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Spiller Vs. Score')


"""def start():
    global root 
    root = Tk()
    root.title('Welcome To Quiz App')
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')   
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="C:\\Users\\andre\\Desktop\\Quiz-App-master\\output-onlinepngtools.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage,bg="red",fg="yellow") 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    """
while True:
    if __name__=='__main__':
        menu(" ")
