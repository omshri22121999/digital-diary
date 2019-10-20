from tkinter import *
import tkinter.messagebox
import json



login_screen = Tk()  
entries = []

def add_entry(f,user,esc):
    entries.append(f)
    g = open(user+".json","w")
    g.write(json.dumps(entries))
    esc.destroy()
    entry(user)


def entry(user):
    global entries
    entry_screen = Tk()
    entry_screen.title("Digital Diary")

    Label(text="Please add an entry", width="40", height="5", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    print("User",user)
    f = open(user+".json","a+")
    f.seek(0)
    data = f.read()

    if(data == ""):
        data = []
    else:
        data = json.loads(data)
        entries = data
    for d in entries:
        Label(text=d ,font=("Calibri", 10)).pack() 
        Label(text="").pack() 

    # create Login Button 
    e = Entry(master = entry_screen)
    e.pack()    
    Label(text="").pack() 


    # create a register button
    Button(text="Add Entry", height="2", width="10",command=lambda:add_entry(e.get(),user,entry_screen)).pack()
    


def get_user(u):
    if(u==""):
        tkinter.messagebox.showerror("Error","Please enter your name")
    else:
        login_screen.destroy()
        entry(u)


def main():
    login_screen.title("Digital Diary")
    Label(text="Enter Your Name", width="40", height="5", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    
    # create Login Button 
    e = Entry(master = login_screen)
    e.pack()    
    Label(text="").pack() 


    # create a register button
    Button(text="Enter", height="2", width="10",command=lambda:get_user(e.get())).pack()

    login_screen.mainloop()

main()