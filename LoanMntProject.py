from tkinter import*
from tkinter import ttk,messagebox
import pymysql

class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Loan Management System,")
        self.root.geometry("1350x720+0+0")
        title=Label(self.root,text="Loan Management System",font=("times new romman",40,'bold'),bd=10,relief=GROOVE,bg='yellow',fg='red')
        title.pack(side=TOP,fill=X)

#=======================Variable==========================
        self.loalId=StringVar()
        self.name=StringVar()
        self.mob=StringVar()
        self.aadhar=StringVar()
        self.add=StringVar()
        self.pin=StringVar()
        self.amount=StringVar()
        self.year=StringVar()
        self.rate=StringVar()
        self.mpay=StringVar()
        self.tpay=StringVar()


#=====================Details of Customer=====================
        Detail_F = Frame(self.root, bd=4, relief=RIDGE,bg='powderblue')
        Detail_F.place(x=10, y=90, width=520, height=620)

        lbl_id = Label(Detail_F, text="Loan Id",font=("times new romman", 18, 'bold'))
        lbl_id.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        txt_id = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3,relief=GROOVE,textvariable=self.loalId)
        txt_id.grid(row=0, column=1, pady=10, sticky="w")

        lbl_name = Label(Detail_F, text="Full Name",font=("times new romman", 18, 'bold'))
        lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3,relief=GROOVE,textvariable=self.name)
        txt_name.grid(row=1, column=1, pady=10, sticky="w")

        lbl_mob = Label(Detail_F, text="Mobile No.",font=("times new romman", 18, 'bold'))
        lbl_mob.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_mob = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3,relief=GROOVE,textvariable=self.mob)
        txt_mob.grid(row=2, column=1, pady=10, sticky="w")

        lbl_aa = Label(Detail_F, text="Aadhar No.",font=("times new romman", 18, 'bold'))
        lbl_aa.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_aa = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3,relief=GROOVE,textvariable=self.aadhar)
        txt_aa.grid(row=3, column=1, pady=10, sticky="w")

        lbl_add = Label(Detail_F, text="Address", font=("times new romman", 18, 'bold'))
        lbl_add.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_add = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,textvariable=self.add)
        txt_add.grid(row=4, column=1, pady=10, sticky="w")

        lbl_pin = Label(Detail_F, text="PinCode", font=("times new romman", 18, 'bold'))
        lbl_pin.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_pin = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,textvariable=self.pin)
        txt_pin.grid(row=5, column=1, pady=10, sticky="w")

        lbl_amount = Label(Detail_F, text="Amount of Loan", font=("times new romman", 18, 'bold'))
        lbl_amount.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_amount = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,textvariable=self.amount)
        txt_amount.grid(row=6, column=1, pady=10, sticky="w")

        lbl_time = Label(Detail_F, text="Number of years", font=("times new romman", 18, 'bold'))
        lbl_time.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_time = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,textvariable=self.year)
        txt_time.grid(row=7, column=1, pady=10, sticky="w")

        lbl_rate = Label(Detail_F, text="Interest Rate", font=("times new romman", 18, 'bold'))
        lbl_rate.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        txt_rate = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,textvariable=self.rate)
        txt_rate.grid(row=8, column=1, pady=10, sticky="w")

        lbl_Mp = Label(Detail_F, text="Monthly Payment", font=("times new romman", 18, 'bold'))
        lbl_Mp.grid(row=9, column=0, pady=10, padx=20, sticky="w")
        txt_Mp = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,state=DISABLED,textvariable=self.mpay)
        txt_Mp.grid(row=9, column=1, pady=10, sticky="w")

        lbl_tp = Label(Detail_F, text="Total Payment", font=("times new romman", 18, 'bold'))
        lbl_tp.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        txt_tp = Entry(Detail_F, font=("times new rommon", 15, 'bold'), bd=3, relief=GROOVE,state=DISABLED,textvariable=self.tpay)
        txt_tp.grid(row=10, column=1, pady=10, sticky="w")
#=========================Employee Record======================
        recordFrame = Frame(self.root, bd=5, relief=RIDGE)
        recordFrame.place(x=535, y=100, width=810, height=530)

        yscroll = Scrollbar(recordFrame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(recordFrame, columns=("empId","name","years","rate","Mpayment","Tpayment","mobile")
                                          , yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.employee_table.yview)
        self.employee_table.heading("empId", text="Employee Id")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("years", text="Number of Years")
        self.employee_table.heading("rate", text="Interest Rate")
        self.employee_table.heading("Mpayment", text="Monthly Payment")
        self.employee_table.heading("Tpayment", text="Total Payment")
        self.employee_table.heading("mobile", text="Mobile No.")

        self.employee_table['show'] = 'headings'

        self.employee_table.column("empId", width=100)
        self.employee_table.column("name", width=100)
        self.employee_table.column("years", width=100)
        self.employee_table.column("rate", width=100)
        self.employee_table.column("Mpayment", width=110)
        self.employee_table.column("Tpayment", width=100)
        self.employee_table.column("mobile", width=100)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.fatch_data()
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)

        #======================Buttons================================
        btnFrame=Frame(self.root,bd=5,relief=RIDGE)
        btnFrame.place(x=535,y=630,width=810,height=80)

        btn1 = Button(btnFrame, text='Add record', font='arial 18 bold', bg='lime', fg='crimson', width=9,command=self.addrecord)
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = Button(btnFrame, text='Update', font='arial 18 bold', bg='lime', fg='crimson', width=9,command=self.update)
        btn2.grid(row=0, column=1, padx=8, pady=10)

        btn3 = Button(btnFrame, text='Delete', font='arial 18 bold', bg='lime', fg='crimson', width=9,command=self.delete)
        btn3.grid(row=0, column=2, padx=8, pady=10)

        btn4 = Button(btnFrame, text='Reset', font='arial 18 bold', bg='lime', fg='crimson', width=9,command=self.reset)
        btn4.grid(row=0, column=3, padx=8, pady=10)

        btn5 = Button(btnFrame, text='Exit', font='arial 18 bold', bg='lime', fg='crimson', width=9,command=self.exit)
        btn5.grid(row=0, column=4, padx=7, pady=10)


#=============================Functions================================
    def total(self):
        p=int(self.amount.get())
        r=int(self.rate.get())
        n=int(self.year.get())
        t=(p*r*n*12)/100
        m=(p+t)/(n*12)
        self.mpay.set(str(round(m,2)))
        self.tpay.set(str(t+p))

    def addrecord(self):
        if self.loalId.get() == '' or self.name.get() == '' or self.mob.get() == '' or self.aadhar.get() == '' or self.add.get() == '' or self.pin.get()=='':
            messagebox.showerror('Error', 'Customers Details are must ?')
        else:
            self.total()
            con = pymysql.connect(host="localhost", user="root", password="", database="emp")
            cur = con.cursor()
            cur.execute("Select * from employee")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == self.loalId.get():
                    messagebox.showerror('Error', 'Duplicate entry not allowed')
                    return
            cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.loalId.get(),
                self.name.get(),
                self.year.get(),
                self.rate.get(),
                self.mpay.get(),
                self.tpay.get(),
                self.mob.get(),
                self.aadhar.get(),
                self.add.get(),
                self.pin.get(),
                self.amount.get()))
            con.commit()
            self.fatch_data()
            con.close()

    def fatch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="emp")
        cur = con.cursor()
        cur.execute("Select * from employee")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
        con.commit()
        con.close()

    def update(self):
        if self.loalId.get()=='':
            messagebox.showerror('Error','Input Information to Update!!')
        else:
            self.total()
            con = pymysql.connect(host="localhost", user="root", password="", database="emp")
            cur = con.cursor()
            # cur.execute("update employee set Name=%s,Years=%s,Interest_Rate=%s,Mobile_No.=%s,Aadhar_No.=%s,Address=%s,Pincode=%s,Amount_of_loan=%s where Employee_Id=%s",(self.name.get(),
            cur.execute("update employee set Name=%s,Years=%s,Interest_Rate=%s,Monthly_Payment=%s,Total_Payment=%s,Mobile_No= %s ,Aadhar_No=%s,Address=%s,Pincode=%s,Amount_of_loan=%s where Employee_Id=%s",(self.name.get(),
                                                                                                                                                                         self.year.get(),
                                                                                                                                                                        self.rate.get(),
                                                                                                                                                                        self.mpay.get(),
                                                                                                                                                                        self.tpay.get(),
                                                                                                                                                                           self.mob.get(),
                                                                                                                                                                          self.aadhar.get(),
                                                                                                                                                                          self.add.get(),
                                                                                                                                                                          self.pin.get(),
                                                                                                                                                                          self.amount.get(),
                                                                                                                                                                         self.loalId.get()))

            messagebox.showinfo('Info',f'Record {self.loalId.get()} Updated Successfully')
            con.commit()
            con.close()
            self.fatch_data()
            self.reset()

    def delete(self):
        if self.loalId.get()=='':
            messagebox.showerror('Error','Please enter Employee ID to delete the records')
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="emp")
            cur = con.cursor()
            cur.execute("delete from employee where Employee_Id=%s",self.loalId.get())
            con.commit()
            con.close()
            self.fatch_data()
            self.reset()

    def reset(self):
        self.loalId.set('')
        self.name.set('')
        self.mob.set('')
        self.aadhar.set('')
        self.add.set('')
        self.pin.set('')
        self.amount.set('')
        self.year.set('')
        self.rate.set('')
        self.mpay.set('')
        self.tpay.set('')

    def exit(self):
        if messagebox.askyesno('Exit',"Do you really want to Exit ?"):
            root.destroy()

    def get_cursor(self,ev):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        row=content['values']
        self.loalId.set(row[0])
        self.name.set(row[1])
        self.year.set(row[2])
        self.rate.set(row[3])
        self.mpay.set(row[4])
        self.tpay.set(row[5])
        self.mob.set(row[6])
        self.aadhar.set(row[7])
        self.add.set(row[8])
        self.pin.set(row[9])
        self.amount.set(row[10])


root=Tk()
obj=Customer(root)
root.mainloop()