
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:24:05 2019

@author: SCHOOL
"""

import tkinter
import random
import re


i1 = ['hi','hello','hey']
o1 = ['Hello There! What would you like to know about?','Hello! What would you like to know about?']
i2 = ['1','2','3','4','5','6']
prj = ["Apple","Google","Microsoft","Tesla","Uber"]
optn = {
        1:"Project IOP",
        2:"Project Manager",
        3:"Test Manager",
        4:"Service Assurance",
        5:"Project Go Live Date",
        6:"Current Phase",
        }

iop= ['7789','4456','9898','9099','8888']
prj_mngr = ['Tony Stark','Bruce Banner','Thor','Scarlet Witch','Alexa']
tst_mngr = ['Rambo','Batman','Spiderman','Vision','Superman']
service = ['Odin','Heimdal','Hela','Loki','Indiana Jones']
golive = ['07/05/2019','01/03/2019','18-03-2019','21-04-2019','11/08/2019']
phase = ['Prod','Plan','Plan','Dev','Prod']

dta = [iop,prj_mngr,tst_mngr,service,golive,phase]



box = tkinter.Tk()
box.title('iAssist')

chathis = []
    

def write(string):
    disp_list.config(state=tkinter.NORMAL)
    disp_list.insert("end", string + "\n")
    disp_list.see("end")
    disp_list.config(state=tkinter.DISABLED)
    


def chat(string):
    #write('\n hi')
    user_inp = inp_msg.get().lower()
    
    
    chathis.append(user_inp)
    
    
    
    print(chathis)
    x = re.search("^Apple$", user_inp,re.IGNORECASE)
    y = re.search("^Google$", user_inp,re.IGNORECASE)
    z = re.search("^Microsoft$", user_inp,re.IGNORECASE)
    a = re.search("^Tesla$", user_inp,re.IGNORECASE)
    b = re.search("^Property$", user_inp,re.IGNORECASE)
    user_inp.lower()
    print(user_inp)
    disp_list.insert(tkinter.END,user_inp )
    disp_list.see(tkinter.END)
    entry_field.delete(0, tkinter.END)
    entry_field.update()
    
    
    
    if user_inp in i1:
        disp_list.insert(tkinter.END," ")
        disp_list.insert(tkinter.END,random.choice(o1))
        disp_list.insert(tkinter.END," ")
        #disp_list.insert(tkinter.END,"What information would you want to know?")
        disp_list.insert(tkinter.END,"   1. Project IOP")
        disp_list.insert(tkinter.END,"   2. Project Manager")
        disp_list.insert(tkinter.END,"   3. Test Manager")
        disp_list.insert(tkinter.END,"   4. Service Assurance")
        disp_list.insert(tkinter.END,"   5. Project Go Live Date")
        disp_list.insert(tkinter.END,"   6. Current Phase")
        disp_list.insert(tkinter.END,"Please enter the respective number:   ")
        disp_list.insert(tkinter.END," ")
        disp_list.see(tkinter.END)
        
    elif user_inp in i2:
        disp_list.insert(tkinter.END," ")        
        disp_list.insert(tkinter.END,"What is your Project name?")
        disp_list.insert(tkinter.END," ")
        disp_list.see(tkinter.END)
    
    else:
        print(chathis[1])
        if(x):
            disp_list.insert(tkinter.END," ")
            disp_list.insert(tkinter.END,optn[int(chathis[1])],"-For Apple is : ",dta[int(chathis[1])-1][0])
            disp_list.insert(tkinter.END," ")
            disp_list.see(tkinter.END)
            chathis.clear()
        if(y):
            disp_list.insert(tkinter.END,optn[int(chathis[1])],"-For Google is : ",dta[int(chathis[1])-1][1])
            disp_list.insert(tkinter.END," ")
            disp_list.see(tkinter.END)
            chathis.clear()
        if(z):
            disp_list.insert(tkinter.END,optn[int(chathis[1])],"-For Microsoft is : ",dta[int(chathis[1])-1][2])
            disp_list.insert(tkinter.END," ")
            disp_list.see(tkinter.END)
            chathis.clear()
        if(a):
            disp_list.insert(tkinter.END,optn[int(chathis[1])],"-For Tesla is : ",dta[int(chathis[1])-1][3])
            disp_list.insert(tkinter.END," ")
            disp_list.see(tkinter.END)
            chathis.clear()
        if(b):
            disp_list.insert(tkinter.END,optn[int(chathis[1])],"-For Uber is : ",dta[int(chathis[1])-1][4])
            disp_list.insert(tkinter.END," ")
            disp_list.see(tkinter.END)
            chathis.clear()
            

    
'''Deletion of user input: Pending
    user_inp.delete("1.0","end-1c")
    user_inp.update()'''

frame = tkinter.Frame(box)
inp_msg = tkinter.StringVar()
#inp_msg.set("Type your messages here.")

scrollbar = tkinter.Scrollbar(frame)
# Following will contain the messages.
disp_list = tkinter.Listbox(frame,background = 'LightCyan2',height=20, width=50, font=('Fixed', 10),yscrollcommand=scrollbar.set)
# inp_list.insert(END, inp_msg)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
disp_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
disp_list.pack()
frame.pack()



# listbox attached to scrollbar

disp_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=disp_list.yview)

entry_field = tkinter.Entry(box,width=40,textvariable=inp_msg)
entry_field.bind("<Return>",chat)
entry_field.pack()

send_button = tkinter.Button(box, text="Send", command=chat)
send_button.pack()
#box.protocol("WM_DELETE_WINDOW", on_closing)
     
box.mainloop()
