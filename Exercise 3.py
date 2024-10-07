from tkinter import *

class MyWindow:
    def __init__(self, win):
        win.configure(bg="#7E60BF")

        # common widgets
        self.Label1 = Label(win, fg="Purple", text=" ୨⋆౨ৎ Calculator ˚⟡˖ ࣪",bg= "#FFE1FF", font= ("Lucida Console", 15))
        self.Label1.place(x=70, y=20)
        self.Label2 = Label(win, text="Number 1:", bg= "#FFE1FF", font= ("Lucida Console", 10))
        self.Label2.place(x=50, y=80)
        self.Entry1 = Entry(win, bd=2)
        self.Entry1.place(x=150, y=80)

        self.Label3 = Label(win, text="Number 2:",bg= "#FFE1FF", font= ("Lucida Console", 10))
        self.Label3.place(x=50, y=130)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=150, y=130)

        self.Label4 = Label(win, text="Result:",bg= "#FFE1FF",  font= ("Lucida Console", 10))
        self.Label4.place(x=50, y=180)
        self.Entry3 = Entry(win, bd=2)
        self.Entry3.place(x=150, y=180)

        self.Button1 = Button(win, fg="Blue", text="Add",font= ("Lucida Console", 10))
        self.Button1.place(x=60, y=250)
        self.Button1.bind('<Button-1>', self.add)

        self.Button2 = Button(win, fg="Blue", text="Sub", font= ("Lucida Console", 10))
        self.Button2.place(x=120, y=250)
        self.Button2.bind('<Button-1>', self.subtract)

        self.Button3 = Button(win, fg="Blue", text="Mul", font= ("Lucida Console", 10))
        self.Button3.place(x=180, y=250)
        self.Button3.bind('<Button-1>', self.multiply)

        self.Button4 = Button(win, fg="Blue", text="Div",  font= ("Lucida Console", 10))
        self.Button4.place(x=240, y=250)
        self.Button4.bind('<Button-1>', self.divide)

    def add(self, event):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def subtract(self, event):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multiply(self, event):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def divide(self, event):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error"
        self.Entry3.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.title('Standard Calculator')
window.geometry("400x400+10+10")
window.mainloop()
