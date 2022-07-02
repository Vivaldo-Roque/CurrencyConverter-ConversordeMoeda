from .currencyapi import *
from .usefulfuctions import *
from tkinter import Tk, messagebox, ttk
from tkinter import *
from PIL import ImageTk, Image
import copy
import sys # Module referring to system commands / Modulo referênte aos comandos do sistema
import main as myMain
import os

def run():

    def clear():

        value.delete(0, END)
        result['text'] = ""
        cmb1.set('')
        cmb2.set('')
        cmb1List = copy.deepcopy(currency)
        cmb2List = copy.deepcopy(currency)
        cmb1['values'] = (cmb1List)
        cmb2['values'] = (cmb2List)

    def updateCmb1List(*args):
        sel = cmb1.get()
        cmb2List = copy.deepcopy(currency)
        cmb2List.remove(sel)
        cmb2.config(values=cmb2List)

    def updateCmb2List(*args):
        sel = cmb2.get()
        cmb1List = copy.deepcopy(currency)
        cmb1List.remove(sel)
        cmb1.config(values=cmb1List)

    languages = loadLanguage() # Get language / Pegar linguagem

    # Colors
    whiteColor = "#eeeeee"
    greyColor = "#1e1e1e"

    # Window setting
    window = Tk()
    window.geometry('300x380')
    window.title(languages["info_1"])
    window.configure(bg=whiteColor)
    window.resizable(height= False, width=False)

    if(not is_connected()):
        msg = messagebox.showerror("NET", languages["net_error"])
        if msg == "OK":
            window.destroy()
            sys.exit()

    # Frames
    top = Frame(window, width= 300, height= 60, bg=whiteColor)
    top.grid(row=0, column=0)

    main = Frame(window, width=300, height=280, bg=whiteColor)
    main.grid(row=1, column=0)

        #Top frame
    icon = Image.open(myMain.mydir+'/app/icon.png')

    mycwd = os.getcwd()
    os.chdir("..")
    #do stuff in parent directory
    os.chdir(mycwd) 
    
    icon = icon.resize((40, 40))
    icon = ImageTk.PhotoImage(icon)
    app_name = Label(top, image=icon, compound=LEFT, text=languages["info_1"], height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=whiteColor, foreground=greyColor)
    app_name.place(x=0, y=0)

    # Main frame
    result = Label(main, text=" ", width=16, height=2, pady=7, relief=SOLID, anchor=CENTER, font=('Ivy 15 bold'), bg=whiteColor, foreground=greyColor)
    result.place(x=50,y=10)

    currency = loadCurrencys()

    cmb1List = copy.deepcopy(currency)
    cmb2List = copy.deepcopy(currency)

    myFrom = Label(main, text=languages["info_2"], width=8, height=1, pady=0, padx=0, relief=FLAT, anchor=NW, font=('Ivy 10 bold'), bg=whiteColor, foreground=greyColor)
    myFrom.place(x=48, y=90)
    cmb1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
    cmb1['values'] = (cmb1List)
    cmb1.bind("<<ComboboxSelected>>", updateCmb1List)
    cmb1.place(x=50, y=115)

    myTo = Label(main, text=languages["info_3"], width=8, height=1, pady=0, padx=0, relief=FLAT, anchor=NW, font=('Ivy 10 bold'), bg=whiteColor, foreground=greyColor)
    myTo.place(x=158, y=90)
    cmb2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
    cmb2['values'] = (cmb2List)
    cmb2.bind("<<ComboboxSelected>>", updateCmb2List)
    cmb2.place(x=160, y=115)

    value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
    value.place(x=50, y=155)

    button1 = Button(main, text=languages["info_4"], width=19, padx=5, height=1, bg=greyColor, fg=whiteColor, font=("Ivy 12 bold"), command= lambda: convert(cmb1, cmb2, value, result))
    button1.place(x=50, y=210)

    button2 = Button(main, text=languages["info_5"], width=19, padx=5, height=1, bg=greyColor, fg=whiteColor, font=("Ivy 12 bold"), command= lambda: clear())
    button2.place(x=50, y=250)

    window.mainloop()