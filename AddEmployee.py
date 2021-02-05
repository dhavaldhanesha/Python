from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkcalendar import Calendar
import Native
import mysql.connector
def state(event):
        sates = event.widget.get()
        print(sates)
#For Closing Curent Window
def close(win):
    win.destroy()
    obj=Native.employee()
    obj.native()
#For Select Using Combobox

#Main Function
def addemp(self,win):
        def getstate(e):
                gujrat = ["Amreli", "Anand", "Aravalli", "Banaskantha (Palanpur)", "Bharuch", "Bhavnagar", "Botad",
                          "Chhota Udepur", "Dahod", "Dangs (Ahwa)", "Devbhoomi Dwarka", "Gandhinagar", "Gir Somnath",
                          "Jamnagar", "Junagadh", "Kachchh", "Kheda (Nadiad)", "Mahisagar", "Mehsana", "Morbi",
                          "Narmada (Rajpipla)", "Navsari", "Panchmahal (Godhra)", "Patan", "Porbandar", "Rajkot",
                          "Sabarkantha (Himmatnagar)", "Surat", "Surendranag"]
                non = []
                global state
                state = e.widget.get()

                if state == "Gujrat":
                        dis['values'] = gujrat
                else:
                        dis['values'] = non
        def getdistrict(d):
                global dis
                dis = d.widget.get()
        def getdate(c, d):
                global date
                date = c.get_date()
                dobent['text'] = date
                SelectDate['state'] = NORMAL
                d.destroy()
        def SelectDate():
                SelectDate['state'] = DISABLED
                date = Tk()
                date.title("Date Picker")
                cal = Calendar(date, selectmode='day',
                               year=2020, month=5,
                               day=22)
                cal.pack(pady=20)
                Button(date, text="Set_Date", command=lambda: getdate(cal, date)).pack()
                date.mainloop()
        def Upload_Details():
                con = mysql.connector.connect(host="localhost", user="root", password="", database="employee")
                mycur = con.cursor()
                val = (fname.get(),mname.get(),lname.get(),mno.get(),email.get(),state.get(),dis.get(),date)
                sql = "insert into details(name,middle,last,mobile,email,state,district,dob) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                mycur.execute(sql,val)
                con.commit()
                fname.set("")
                mname.set("")
                lname.set("")
                mno.set("")
                email.set("")
                state.set("")
                dis.set("")
                dobent['text'] = ""

        win.destroy()
        addemp = Tk()
        addemp.geometry('800x500')
        addemp.configure(bg="#FFC300")

        #Initilazitation Font Here
        myfont=Font(size=15)
        second = Font(size=15)

        #Crete Top Frame Here
        top=Frame(addemp,width='800',height='50',bg='#DAF7A6')
        top.place(x=0,y=0)

        #Write Hedding
        hedding=Label(top,text="Insert Employees Details Here",bg='#DAF7A6',font=myfont)
        hedding.place(x=50,y=10)

        #Creating Back Button
        back=Button(top,text="Back",bg="#FFC300",command=lambda:close(addemp))
        back.place(x=730,y=12)

        #Window Body
        body=Frame(addemp,width="800",height="450",bg="#FFC300")
        body.place(x=0,y=50)
        fname = StringVar()
        mname = StringVar()
        lname = StringVar()
        mno = IntVar()
        email = StringVar()

        namelbl=Label(body,text="Enter First Name",bg="#FFC300")
        namelbl.place(x=50,y=30)
        nameent=Entry(body,width="20",textvariable=fname)
        nameent.place(x=150,y=30)

        lastnamelbl = Label(body, text="Enter Midle Name", bg="#FFC300")
        lastnamelbl.place(x=50,y=70)
        lastnameent = Entry(body, width="20",textvariable=mname)
        lastnameent.place(x=150,y=70)

        sirnamelbl = Label(body, text="Enter Last Name", bg="#FFC300")
        sirnamelbl.place(x=50,y=110)
        sirnameent = Entry(body, width="20",textvariable=lname)
        sirnameent.place(x=150,y=110)

        monlbl = Label(body, text="Enter Mobile No", bg="#FFC300")
        monlbl.place(x=50,y=150)
        monent = Entry(body, width="20",textvariable=mno)
        monent.place(x=150,y=150)

        emaillbl = Label(body, text="Enter E-Mail", bg="#FFC300")
        emaillbl.place(x=50,y=190)
        emailent = Entry(body, width="40",textvariable=email)
        emailent.place(x=150,y=190)

        Label(body, text="Select State", bg="#FFC300").place(x=50,y=230)

        disc = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
                "Chandigarh", "Chhattisgarh", "Gujrat"]
        state = Combobox(body, values=disc)
        state.place(x=150,y=230)
        state.bind("<<ComboboxSelected>>", getstate)

        Label(body, text="Select Districts", bg="#FFC300").place(x=50,y=270)
        dis = []
        dis = Combobox(body, values=dis)
        dis.bind("<<ComboboxSelected>>",getdistrict)
        dis.place(x=150,y=270)

        SelectDate = Button(body, text="Select DOB", command=SelectDate,width=12)
        SelectDate.place(x=50,y=310)

        dobent = Label(body, width="20",text="")
        dobent.place(x=150, y=310)

        Submit=Button(body,text="Upload",command=Upload_Details)
        Submit.place(x=50,y=350)
        addemp.mainloop()
if __name__ == "__main__":
    addemp()
