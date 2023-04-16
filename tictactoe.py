from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Tic-Tac-Toe")
root.geometry("500x500")
root.configure(background="light seagreen")

player=1
label_player=Label(root,text="Player "+str(player),fg="white",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",20,"bold"))
label_player.place(relx=0.5,rely=0.05,anchor=CENTER)

separator1=ttk.Separator(root,orient="vertical")
separator1.place(relx=0.375,rely=0.455,relwidth=0.007,relheight=0.75,anchor=CENTER)

separator2=ttk.Separator(root,orient="vertical")
separator2.place(relx=0.622,rely=0.455,relwidth=0.005,relheight=0.75,anchor=CENTER)

separator3=ttk.Separator(root,orient="horizontal")
separator3.place(relx=0.502,rely=0.576,relwidth=0.75,relheight=0.005,anchor=CENTER)

separator4=ttk.Separator(root,orient="horizontal")
separator4.place(relx=0.502,rely=0.33,relwidth=0.75,relheight=0.005,anchor=CENTER)

title=Label(root,text="Tic-Tac-Toe",font=("Segoe Print",25,"bold","italic","underline"),bg="light seagreen",fg="white")
title.place(relx=0.5,rely=0.9,anchor=CENTER)

btn1_text=""
btn2_text=""
btn3_text=""
btn4_text=""
btn5_text=""
btn6_text=""
btn7_text=""
btn8_text=""
btn9_text=""

row1x=0
row1o=0
row2x=0
row2o=0
row3x=0
row3o=0
col1x=0
col1o=0
col2x=0
col2o=0
col3o=0
col3x=0
slant1x=0
slant1o=0
slant2x=0
slant2o=0
buttons=0
win=0

def btn1_function():
    global player
    global btn1_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 1")
    __btn1=""
    if (player==1):
        __btn1="❌" 
        btn1["text"]=__btn1
        player=2 
        label_player["text"]="Player "+str(player)
        print(btn1_text)
        row1x=row1x+1
        print(row1x)
        btn1["state"]="disabled"

        if (row1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col1x=col1x+1
        print(col1x)
        if (col1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        slant1x=slant1x+1
        print(slant1x)
        if (slant1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
    elif (player==2):
        __btn1="⭕"
        btn1["text"]=__btn1
        btn1_text=btn1.cget('text')
        player=1
        label_player["text"]="Player "+str(player)
        print(btn1_text)
        row1o=row1o+1
        print(row1o)
        btn1["state"]="disabled"
        if (row1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
            
        col1o=col1o+1
        print(col1o)
        if (col1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        slant1o=slant1o+1
        print(slant1o)
        if (slant1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn2_function():
    global player
    global btn2_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 2")
    if (player==1):
        __btn2="❌"
        btn2["text"]=__btn2
        player=2
        label_player["text"]="Player "+str(player)
        btn2_text=btn2.cget('text')
        print(btn2_text)
        row1x=row1x+1
        print(row1x)
        btn2["state"]="disabled"
        if (row1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col2x=col2x+1
        print(col2x)
        if (col2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
    elif (player==2):
        __btn2="⭕"
        btn2["text"]=__btn2
        player=1
        label_player["text"]="Player "+str(player)
        btn2_text=btn2.cget('text')
        print(btn2_text)
        row1o=row1o+1
        print(row1o)
        btn2["state"]="disabled"
        if (row1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col2o=col2o+1
        print(col2o)
        if (col2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn3_function():
    global player
    global btn3_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 3")
    if (player==1):
        __btn3="❌"
        btn3["text"]=__btn3
        player=2
        label_player["text"]="Player "+str(player)
        btn3_text=btn3.cget('text')
        print(btn3_text)
        row1x=row1x+1
        print(row1x)
        btn3["state"]="disabled"
        if (row1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col3x=col3x+1
        print(col3x)
        if (col3x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant2x=slant2x+1
        print(slant2x)
        if (slant2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
    elif (player==2):
        __btn3="⭕"
        btn3["text"]=__btn3
        player=1
        label_player["text"]="Player "+str(player)
        btn3_text=btn3.cget('text')
        print(btn3_text)
        row1o=row1o+1
        print(row1o)
        btn3["state"]="disabled"
        if (row1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col3o=col3o+1
        print(col2x)
        if (col3o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant2o=slant2o+1
        print(slant2o)
        if (slant2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn4_function():
    global player
    global btn4_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 4")
    if (player==1):
        __btn4="❌"
        btn4["text"]=__btn4
        player=2
        label_player["text"]="Player "+str(player)
        btn4_text=btn4.cget('text')
        print(btn4_text)
        row2x=row2x+1
        print(row2x)
        btn4["state"]="disabled"
        if (row2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col1x=col1x+1
        print(col1x)
        if (col1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
    elif (player==2):
        __btn4="⭕"
        btn4["text"]=__btn4
        player=1
        label_player["text"]="Player "+str(player)
        btn4_text=btn4.cget('text')
        print(btn4_text)
        row2o=row2o+1
        print(row2o)
        btn4["state"]="disabled"
        if (row2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col1o=col1o+1
        print(col1o)
        if (col1o==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn5_function():
    global player
    global btn5_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 5")
    if (player==1):
        __btn5="❌"
        btn5["text"]=__btn5
        player=2
        label_player["text"]="Player "+str(player)
        btn5_text=btn5.cget('text')
        print(btn5_text)
        row2x=row2x+1
        print(row2x)
        btn5["state"]="disabled"
        if (row2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col2x=col2x+1
        print(col2x)
        if (col2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant1x=slant1x+1
        print(slant1x)
        if (slant1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant2x=slant2x+1
        print(slant2x)
        if (slant2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
    elif (player==2):
        __btn5="⭕"
        btn5["text"]=__btn5
        player=1
        label_player["text"]="Player "+str(player)
        btn5_text=btn5.cget('text')
        print(btn5_text)
        row2o=row2o+1
        print(row2o)
        btn5["state"]="disabled"
        if (row2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col2o=col2o+1
        print(col2o)
        if (col2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant1o=slant1o+1
        print(slant1o)
        if (slant1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant2o=slant2o+1
        print(slant2o)
        if (slant2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn6_function():
    global player
    global btn6_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 6")
    if (player==1):
        __btn6="❌"
        btn6["text"]=__btn6
        player=2
        label_player["text"]="Player "+str(player)
        btn6_text=btn6.cget('text')
        print(btn6_text)
        row2x=row2x+1
        print(row2x)
        btn6["state"]="disabled"
        if (row2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col3x=col3x+1
        print(col3x)
        if (col3x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
    elif (player==2):
        __btn6="⭕"
        btn6["text"]=__btn6
        player=1
        label_player["text"]="Player "+str(player)
        btn6_text=btn6.cget('text')
        print(btn6_text)
        row2o=row2o+1
        print(row2o)
        btn6["state"]="disabled"
        if (row2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col3o=col3o+1
        print(col3o)
        if (col3o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn7_function():
    global player
    global btn7_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 7")
    if (player==1):
        __btn7="❌"
        btn7["text"]=__btn7
        player=2
        label_player["text"]="Player "+str(player)
        btn7_text=btn7.cget('text')
        print(btn7_text)
        row3x=row3x+1
        print(row3x)
        btn7["state"]="disabled"
        if (row3x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col1x=col1x+1
        print(col1x)
        if (col1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        slant2x=slant2x+1
        print(slant2x)
        if (slant2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
        
    elif (player==2):
        __btn7="⭕"
        btn7["text"]=__btn7
        player=1
        label_player["text"]="Player "+str(player)
        btn7_text=btn7.cget('text')
        print(btn7_text)
        row3o=row3o+1
        print(row3o)
        btn7["state"]="disabled"
        if (row3o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col1o=col1o+1
        print(col1o)
        if (col1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        slant2o=slant2o+1
        print(slant2o)
        if (slant2o==3):
            label_winner["text"]=" ⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn8_function():
    global player
    global btn8_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 8")
    if (player==1):
        __btn8="❌"
        btn8["text"]=__btn8
        player=2
        label_player["text"]="Player "+str(player)
        btn8_text=btn8.cget('text')
        print(btn8_text)
        row3x=row3x+1
        print(row3x)
        btn8["state"]="disabled"
        if (row3x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col2x=col2x+1
        print(col2x)
        if (col2x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
    elif (player==2):
        __btn8="⭕"
        btn8["text"]=__btn8
        player=1
        label_player["text"]="Player "+str(player)
        btn8_text=btn8.cget('text')
        print(btn8_text)
        row3o=row3o+1
        print(row3o)
        btn8["state"]="disabled"
        if (row3o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col2o=col2o+1
        print(col2o)
        if (col2o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
def btn9_function():
    global player
    global btn9_text
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    print("Button 9")
    if (player==1):
        __btn9="❌"
        btn9["text"]=__btn9
        player=2
        label_player["text"]="Player "+str(player)
        btn9_text=btn9.cget('text')
        print(btn9_text)
        row3x=row3x+1
        print(row3x)
        btn9["state"]="disabled"
        if (row3x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("❌ Wins")
            win=1
        col3x=col3x+1
        print(col3x)
        if (col3x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant1x=slant1x+1
        print(slant1x)
        if (slant1x==3):
            label_winner["text"]="❌ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons)
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
        
    elif (player==2):
        __btn9="⭕"
        btn9["text"]=__btn9
        player=1
        label_player["text"]="Player "+str(player)
        btn9_text=btn9.cget('text')
        print(btn9_text)
        row3o=row3o+1
        print(row3o)
        btn9["state"]="disabled"
        if (row3o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            print("⭕ Wins")
            win=1
        col3o=col3o+1
        print(col2x)
        if (col3o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        slant1o=slant1o+1
        print(slant1o)
        if (slant1o==3):
            label_winner["text"]="⭕ Wins"
            label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
            btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
            win=1
        buttons=buttons+1
        print(buttons) 
        if (buttons==9):
            if (win==0):
                print("TIE")
                label_winner["text"]="It's a tie!"
                label_winner.place(relx=0.5,rely=0.5,anchor=CENTER)
                btn_restart.place(relx=0.5,rely=0.7,anchor=CENTER)
                
def restart():
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""
    label_winner.place_forget()
    btn_restart.place_forget()
    global row1x
    global row1o
    global row2x
    global row2o
    global row3o
    global row3x
    global col1x
    global col1o
    global col2x
    global col2o
    global col3o
    global col3x
    global slant1x
    global slant1o
    global slant2o
    global slant2x
    global buttons
    global win
    row1x=0
    row1o=0
    row2x=0
    row2o=0
    row3o=0
    row3x=0
    col1x=0
    col1o=0
    col2x=0
    col2o=0
    col3x=0
    col3o=0
    slant1x=0
    slant1o=0
    slant2x=0
    slant2o=0
    buttons=0
    win=0
    btn1["state"]="normal"
    btn2["state"]="normal"
    btn3["state"]="normal"
    btn4["state"]="normal"
    btn5["state"]="normal"
    btn6["state"]="normal"
    btn7["state"]="normal"
    btn8["state"]="normal"
    btn9["state"]="normal"

btn1=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn1_function,relief=FLAT)
btn1.place(relx=0.15,rely=0.1)

btn2=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn2_function,relief=FLAT)
btn2.place(relx=0.4,rely=0.1)

btn3=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn3_function,relief=FLAT)
btn3.place(relx=0.65,rely=0.1)

btn4=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn4_function,relief=FLAT)
btn4.place(relx=0.15,rely=0.35)

btn5=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn5_function,relief=FLAT)
btn5.place(relx=0.4,rely=0.35)

btn6=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn6_function,relief=FLAT)
btn6.place(relx=0.65,rely=0.35)

btn7=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn7_function,relief=FLAT)
btn7.place(relx=0.15,rely=0.6)

btn8=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn8_function,relief=FLAT)
btn8.place(relx=0.4,rely=0.6)

btn9=Button(root,text="",fg="black",bg="light seagreen",font=("Bahnschrift SemiBold Condensed",17,"bold"),width=10,height=3,command=btn9_function,relief=FLAT)
btn9.place(relx=0.65,rely=0.6)

label_winner=Label(root,font=("segoe Print",80),bg="light seagreen")
label_winner.pack_forget()

btn_restart=Button(root,text="RESTART ↻",command=restart)
btn_restart.pack_forget()
  
root.mainloop()