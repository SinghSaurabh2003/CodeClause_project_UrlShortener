#Importing all modules
import pyshorteners
from tkinter import *
#creating window of perticular size and colour
window=Tk()
window.title("URL Shortener")
window.geometry("400x300")
window.configure(bg="red")
#Function to short
ip=StringVar()
a=StringVar()
op_url=StringVar()

def shorturl():
    a=ip.get()
    pys=pyshorteners.Shortener().tinyurl.short(a)
    op_url.set(pys)
#Heading
Label(window,text="Enter Your URL",font="impack 17 bold",bg="black",fg="white").pack(fill="x")
#Input URL BOX
Entry(window,textvariable=ip,font="10",bd=4,width=40).pack(pady="25")
#Enter Button
Button(window,text="Enter",font="impack 17 bold",bg="black",fg="white",command=shorturl).pack()
Entry(window,textvariable=op_url,font="impack 12 bold",bg="red",bd=0,width=25).pack(pady="25")
mainloop()

