from tkinter import *
from tkinter.font import Font
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import Native

#For Closing Curent Window
def close(win):
    win.destroy()
    obj=Native.employee()
    obj.native()
#For Select Using Combobox
def state(event):
    sates=event.widget.get()
    print(sates)
#Main Function
def addemp(self,win):
        win.destroy()
        addemp=Tk()
        addemp.geometry('800x500')
        addemp.configure(bg="#FFC300")

        #Initilazitation Font Here
        myfont=Font(size=15)
        second=Font(size=15)

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

        namelbl=Label(body,text="Enter Name",bg="#FFC300")
        namelbl.place(x=50,y=60)
        nameent=Entry(body,width="20")
        nameent.place(x=130,y=60)

        lastnamelbl=Label(body,text="Enter Last Name",bg="#FFC300")
        lastnamelbl.place(x=260,y=60)
        lastnameent=Entry(body,width="20")
        lastnameent.place(x=360,y=60)

        sirnamelbl=Label(body,text="Enter Last Name",bg="#FFC300")
        sirnamelbl.place(x=490,y=60)
        sirnameent=Entry(body,width="20")
        sirnameent.place(x=590,y=60)

        monlbl=Label(body,text="Enter Mobile No",bg="#FFC300")
        monlbl.place(x=50,y=130)
        monent=Entry(body,width="20")
        monent.place(x=150,y=130)

        emaillbl=Label(body,text="Enter E-Mail",bg="#FFC300")
        emaillbl.place(x=280,y=130)
        emailent=Entry(body,width="58")
        emailent.place(x=360,y=130)

        disc=["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
        "Chandigarh","Chhattisgarh","Gujrat"]
        state = Combobox(body,values=disc)
        state.place(x=50,y=200)
        state.bind("<<ComboboxSelected>>", state)
        addemp.mainloop()

if __name__ == "__main__":
    addemp()
