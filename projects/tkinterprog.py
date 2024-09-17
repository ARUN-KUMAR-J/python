from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry('400x580+100+200')
window.config(background="#456")
window.resizable(False,False)
equation=""
def show(values):
    global equation
    equation+=values
    label.config(text=equation)
def clear():
    global equation
    equation=""
    label.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label.config(text=result)
label=Label(window,text="",height=2,width=25,font=('arial',30))
label.pack()
Button(window,text="C",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(window,text="%",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("%")).place(x=110,y=100)
Button(window,text="+",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("+")).place(x=210,y=100)
Button(window,text="/",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("/")).place(x=310,y=100)
Button(window,text="7",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("7")).place(x=10,y=200)
Button(window,text="8",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("8")).place(x=110,y=200)
Button(window,text="9",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("9")).place(x=210,y=200)
Button(window,text="x",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("*")).place(x=310,y=200)
Button(window,text="4",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("4")).place(x=10,y=300)
Button(window,text="5",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("5")).place(x=110,y=300)
Button(window,text="6",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("6")).place(x=210,y=300)
Button(window,text="-",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("-")).place(x=310,y=300)
Button(window,text="1",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("1")).place(x=10,y=400)
Button(window,text="2",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("2")).place(x=110,y=400)
Button(window,text="3",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("3")).place(x=210,y=400)

Button(window,text="0",width=3,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show("0")).place(x=10,y=490)
Button(window,text=".",width=7,height=1,font=('arial',30,"bold"),bd=1,fg="#fff",bg="grey",command=lambda:show(".")).place(x=110,y=490)
Button(window,text="=",width=3,height=3,font=('arial',30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=310,y=400)
window.mainloop()