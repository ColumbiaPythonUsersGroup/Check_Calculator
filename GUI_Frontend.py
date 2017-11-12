from Tkinter import *
import Backend

root = Tk()
root.geometry("300x200")
root.title("Check Calculator")



def set_var():
    payfreq = (e1_value.get())  # Will get string from the entry box
    filing_status = (e2_value.get())
    ftc = (e3_value.get())
    Backend.status(payfreq, filing_status, ftc)
    var = Backend.status(payfreq, filing_status, ftc)
    t1.insert(END, var)

#  Submenu line at top of application
menuLine = Menu(root)
root.config(menu=menuLine)

subMenu = Menu(menuLine)
menuLine.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label='Exit', command=root.quit)


l1 = Label(root, text="Pay Frequency").pack(padx=5)

e1_value = StringVar()
e1 = Entry(root, bd=2, textvariable=e1_value).pack(padx=5)

l2 = Label(root, text="Filing Status").pack(padx=5)

e2_value = StringVar()
e2 = Entry(root, bd=2, textvariable=e2_value).pack(padx=5)

l3 = Label(root, text="Taxable Comp Amount").pack(padx=5)

e3_value = IntVar()
e3 = Entry(root, bd=2, textvariable=e3_value).pack(padx=5)

l4 = Label(root, text="FIT Amount").pack(padx=5)

t1 = Text(root, bd=2, height=1, width=15)
t1.pack(padx=5)

b1 = Button(root, text="Calc", command=set_var).pack()

root.mainloop()
