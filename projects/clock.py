import tkinter 
from time import strftime
root=tkinter.Tk()
root.title("Clock")
root.geometry('580x400')
def time():
    mytext=strftime("%H:%M:%S")
    label.config(text=mytext)
    label.after(1000,time)
label= tkinter.Label(root,text="",font=('Arial',72),fg='white',bg='black')
label.pack()
time()
root.mainloop()