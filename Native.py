from tkinter import *
from tkinter.font import Font
from PIL import Image,ImageTk
import AddEmployee
class employee:
    def native(self):
        #Create Window Object Here
        native=Tk(className="Employee Management system")
        native.geometry('800x500')
        native.configure(bg="#FFC300")

        #Initilazitation Font Here
        myfont=Font(size=15)
        second=Font(size=15)
        #Crete Top Frame Here
        top=Frame(native,width='800',height='50',bg='#DAF7A6')
        top.place(x=0,y=0)

        hedding=Label(top,text="Sahara Employee Management system",bg='#DAF7A6',font=myfont)
        hedding.place(x=50,y=10)

        admin=Button(top,text="Admin",bg="#FFC300")
        admin.place(x=730,y=12)

        #Display Iamge Here
        load = Image.open("employee.png")
        res = load.resize((350, 400), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(res)
        img = Label(native, image=render,bg="#FFC300")
        img.image = render
        img.place(x=20, y=50)

        #List Of Button
        buttons=Frame(native,bg="#FFC300",width="360",height="400")
        buttons.place(x=420,y=75)

        lbl=Label(buttons,text="Manage Employee Details",bg='#FFC300',font=second)
        lbl.place(x=70,y=10)

        addemp=Button(buttons,text="Add Employee",bg="#DAF7A6",width="15",command=lambda:AddEmployee.addemp("",native))
        addemp.place(x=140,y=100)

        viewemp=Button(buttons,text="View Employees",bg="#DAF7A6",width="15",command=lambda:self.viewemp(native))
        viewemp.place(x=140,y=150)

        sendmsg=Button(buttons,text="Send Message",bg="#DAF7A6",width="15")
        sendmsg.place(x=140,y=200)

        #Footer Here
        footer=Frame(native,width="800",height="50",bg="#DAF7A6")
        footer.place(x=0,y=450)

        footerlbl=Label(footer,text="This is sahara management system used to manage employee details!!!",bg="#DAF7A6",font=second)
        footerlbl.place(x=95,y=10)
        #btn=Button(native,text="click",command=lambda:self.clk(native)).pack()
        native.mainloop()

if __name__ == "__main__":
    obj=employee()
    obj.native()
    
        