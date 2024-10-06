from tkinter import *
class emi_calc:
    def __init__(self):
        self.root = Tk()
        self.root.title('EMI Calculator')
        self.root.geometry("550x380")
        self.root.minsize(550,380)
        self.root.maxsize(550,380)
        self.root.configure(bg="lightgrey")
        self.clr = "lightgrey"
        self.clr_lblack = "#474747"
        self.text_writing()

        self.creating_button()
        self.entry()
        self.setting_position()
        self.root.bind('<Return>', self.Calculate)
        self.root.mainloop()
#.....................................................Calculating the Interest of the amount..........................................................
    def Calculate(self,event=None):
        try:
            self.pricip = float(self.pricipalentry.get())
            self.rat = float(self.rateentry.get()) / 1200
            self.tim = float(self.timeentry.get()) * 12
        except ValueError:
            self.Emi.config(text="Error:",font='Times 15', fg="red")
            self.Tot.config(text=" Invalid Input ",font='Times 15',fg="red")
            return
#........................................................Calculate EMI..................................................................................
        EMI = self.pricip * self.rat * (1 + self.rat) ** self.tim / ((1 + self.rat) ** self.tim - 1)
        total_amount = EMI * self.tim

        self.Emi.config(text="{:.2f}".format(EMI), fg="black")
        self.Tot.config(text="{:.2f}".format(total_amount), fg="black")
#.......................................................Here we write the text that we want to display on the screen.................................
    def text_writing(self):
        self.name = Label(self.root,text="****-----EMI Calculator-----****",font="Times 15 bold",bg=self.clr_lblack,fg="White",relief=SUNKEN,border=8,pady=10,borderwidth=8)
        self.pricipal = Label(self.root,text="Principal Amount(Rs):",font="Times 15",bg=self.clr)
        self.Rate = Label(self.root,text="Rate of interest(%):",font="Times 15",bg=self.clr)
        self.Time_period= Label(self.root,text="Loan tenure(yr):",font="Times 15",bg=self.clr)
        self.frame = Frame(self.root,width=200,height=130,bg=self.clr_lblack,border=8,borderwidth=8,relief=SUNKEN).pack(side=BOTTOM,fill=X)
        self.interest = Label(self.root, text="Monthly EMI :", font="Times 15",bg=self.clr_lblack,fg="White")
        self.total = Label(self.root,text="Total amount(Rs) :",font="Times 15",bg=self.clr_lblack,fg="White")
        self.enter_value()
#.............................................................Talking entry...........................................................................
    def entry(self):
        self.pricipalentry = Entry(self.root, textvariable=self.pricipalvalue, font="Times 15", width=10,border=5,bg="white")
        self.rateentry = Entry(self.root, textvariable=self.ratevalue, font="Times 15", width=10,border=5,bg="white")
        self.timeentry = Entry(self.root, textvariable=self.Timevalue, font="Times 15", width=10,border=5,bg="white")
#............................................................. Here we set up the box for taking the input from the user..............................
    def setting_position(self):
        self.name.pack(side=TOP,fill=X)
        self.pricipal.place(x=30,y= 70)
        self.Rate.place(x=30,y= 130)
        self.Time_period.place(x=30,y=200 )
        self.pricipalentry.place(x=240, y=70)
        self.rateentry.place(x = 240,y = 130)
        self.timeentry.place(x = 240,y = 200)
        self.interest.place(x=30, y=270)
        self.total.place(x = 30,y = 330)
        self.Emi.place(x=240, y=270)
        self.Tot.place(x=240, y=330)
#.................................................................Entering Values......................................................................
    def enter_value(self):
        self.pricipalvalue = StringVar()
        self.ratevalue = StringVar()
        self.Timevalue = StringVar()
        self.Emi = Label(self.root, text="", font="Times 15",width=9,border=5,borderwidth=5,relief=SUNKEN,bg=self.clr)
        self.Tot = Label(self.root, text="", font="Times 15",width=9,border=5,borderwidth=5,relief=SUNKEN,bg=self.clr)
#...............................................................Clear the entries.......................................................................
    def clear_entry(self):
        self.pricipalentry.delete(0,END)
        self.rateentry.delete(0, END)
        self.timeentry.delete(0, END)
        self.Emi.config(text="")
        self.Tot.config(text="")
#.............................................................Creating calculate and exit button.........................................................
    def creating_button(self):
        Button(text="Calculate EMI", font="Times 10 ", command=self.Calculate,border=5,bg=self.clr_lblack,fg="White",padx=3).place(x=420, y=190)
        Button(text="Exit",command=lambda:exit(),font="Times 10",padx=30,border=5,bg=self.clr_lblack,fg="white").place(x = 420,y = 70)
        Button(text="Clear",command=self.clear_entry,font="Times 10",border=5,bg=self.clr_lblack,fg="white",padx=27).place(x=420,y = 130)

emi_calc()
