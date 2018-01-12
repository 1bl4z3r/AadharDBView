import Tkinter
import mysql.connector

cnx=mysql.connector.connect(user='****',password='****',host='localhost',database='***"')
cur=cnx.cursor()

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter Aadhar No")
        
        button = Tkinter.Button(self,text=u"Find",command=self.OnButtonClick)
        button.grid(column=0,row=1,columnspan=2,sticky='EW')
        
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w",fg="white",bg="black")        
        label.grid(column=0,row=3,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Enter Aadhar No.")
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        number=self.entryVariable.get()
        num=int(number)
        z = self.find(num)
        
        self.labelVariable.set(z)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

        
    def OnPressEnter(self,event):
        number=self.entryVariable.get()
        num=int(number)
        y = self.find(num) 
        
        self.labelVariable.set(y)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def find(self,num):
        cur.execute("select * from data where number='%s'" %num)
        for row in cur.fetchall():
            return ("Name: %s   UID: %s    Connections Active: %s" %(row[0],row[1],row[2]))
        

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Aadhar')
    app.mainloop()
    cur.close()
