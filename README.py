from tkinter import*

window = Tk()
window.configure(background="white")
window.geometry("1129x809")
window.title("ASRAR")
window.resizable(False,False)
Label(window,text="CALL DIALER📞",fg="green",bg="black",font=("",20)).place(x=5,y=10)
Entry=Entry(window,font=("Arial",25),bg="white").place(x=215,y=150)
def button():
    Label(window,text="+91 8122609079",fg="black",bg="gray",font=("",35)).place(x=215,y=60)
    Label(window,text="📞calling...",fg="black",bg="gray",font=("",15)).place(x=370,y=120)
Button(window,text="1",fg="black",bg="white",font=("",30),command=button).place(x=315,y=210)
Button(window,text="4",fg="black",bg="white",font=("",30),command=button).place(x=315,y=290)
Button(window,text="7",fg="black",bg="white",font=("",30),command=button).place(x=315,y=370)
Button(window,text="*",fg="black",bg="white",font=("",30),command=button).place(x=315,y=450)
#Button(window,text="5",fg="red",bg="gray",font=("",30),command=button).place(x=315,y=530)
Button(window,text="2",fg="black",bg="white",font=("",30),command=button).place(x=375,y=210)
Button(window,text="5",fg="black",bg="white",font=("",30),command=button).place(x=375,y=290)
Button(window,text="8",fg="black",bg="white",font=("",30),command=button).place(x=375,y=370)
Button(window,text="0",fg="black",bg="white",font=("",30),command=button).place(x=375,y=450)
#Button(window,text="4",fg="red",bg="gray",font=("",30),command=button).place(x=435,y=530)

Button(window,text="3",fg="black",bg="white",font=("",30),command=button).place(x=435,y=210)
Button(window,text="6",fg="black",bg="white",font=("",30),command=button).place(x=435,y=290)
Button(window,text="9",fg="black",bg="white",font=("",30),command=button).place(x=435,y=370)
Button(window,text="#",fg="black",bg="white",font=("",30),command=button).place(x=435,y=450)
#-----------------------------------------
#Button(window,text="1",fg="red",bg="gray",font=("",30),command=button).place(x=505,y=210)
Button(window,text="x",fg="black",bg="gray",font=("",30),command=button).place(x=435,y=530)
Button(window,text= ' 📞  ',fg="white",bg="green",font=("",30),command=button).place(x=325,y=530)

 
    

window.mainloop()
