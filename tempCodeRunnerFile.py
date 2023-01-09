from tkinter import*
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System | by - Aarya , Sheen , Raghuvendra")
        title=Label(self.root,text="Inventory Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="white").place(x=0,y=0,relwidth=1,height=70)

root=Tk()
obj=IMS(root)
root.mainloop()