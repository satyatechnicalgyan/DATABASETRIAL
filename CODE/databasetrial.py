from tkinter import *


class Resistor:
    def __init__(self,root):
        self.root=root
        self.root.title('Fill Information')
        self.root.geometry('350x250+0+0')

        #=======Resistor Frame
       
        # #=======Resistor Frame
        frame1=Frame(self.root,bg='darkgray')
        frame1.place(x=1,y=1,width=350,height=250)
        #====department name row1
        subjectname=Label(frame1,text="Subject's Name",bg='darkgrey',font=('times new roman',10,'bold'),fg='white').place(x=10,y=5)
        txtsubjectname=Entry(frame1,font=('times new roman',8,'bold'),bg='lightgray').place(x=140,y=5)
        #==ROW2
        vehicleNumber= Label(frame1, text='Vehicle Number', bg='darkgrey', font=('times new roman', 10, 'bold'),
                      fg='white').place(x=10, y=35)
        txtvehicleNumber= Entry(frame1, font=('times new roman', 8, 'bold'), bg='lightgray').place(x=140, y=35)
        #RPOW3
        licenceNumber=Label(frame1,text='licence Number',bg='darkgrey',font=('times new roman',10,'bold'),fg='white').place(x=10,y=65)
        txtlicenceNumber=Entry(frame1,font=('times new roman',8,'bold'),bg='lightgray').place(x=140,y=65)
        #############row4
        OfficersName= Label(frame1, text="Officer's Name'", bg='darkgrey', font=('times new roman', 10, 'bold'),
                      fg='white').place(x=10, y=95)
        txtOfficersName= Entry(frame1, font=('times new roman', 8, 'bold'), bg='lightgray').place(x=140, y=95)
        ###row5
        BadgeNumber= Label(frame1, text='Badge Number', bg='darkgrey', font=('times new roman', 10, 'bold'),
                       fg='white').place(x=10, y=125)
        txtBadgeNumber= Entry(frame1, font=('times new roman', 8, 'bold'), bg='lightgray').place(x=140, y=125)
        ####row6
        Department = Label(frame1, text='Department', bg='darkgrey', font=('times new roman', 10, 'bold'),
                       fg='white').place(x=10, y=155)
        txtDepartment= Entry(frame1, font=('times new roman', 8, 'bold'), bg='lightgray').place(x=140, y=155)
        #button
        home_btn=Button(frame1,text='Home',bg='lightgray').place(x=100,y=220,width=60,height=25)
        next_btn = Button(frame1, text='Next', bg='lightgray').place(x=160, y=220, width=60, height=25)

root=Tk()
abj=Resistor(root)
root.mainloop()
