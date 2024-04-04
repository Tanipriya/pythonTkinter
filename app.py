from tkinter import*
class Student:
    def __init__(self, root):
        self.root= root
        self.root.title("Student Management System")
        self.root.geometry('550x550+0+0')

        title= Label(self.root, text="Student Management System", bd=8, relief=GROOVE, font= ("times new roman", 30, "bold"), bg= "yellow" )
        title.pack(side=TOP, fill=X)

        frame1= Frame(self.root, bd=4, relief=RIDGE, bg= "crimson")
        frame1.place(x=20, y=75, width=450, height=560)

        frame2= Frame(self.root, bd=4, relief=RIDGE, bg= "crimson")
        frame2.place(x=500, y=75, width=750, height=560)

        m_title= Label(frame1, text="Manage Student", bg="crimson", fg="white", font=("times_new_roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        s_title= Label(frame2, text="Details Manage", bg="crimson", fg="white", font= ("times_new_roman", 20, "bold") )
        s_title.grid(row=0, columnspan=2, pady=20)

        

root= Tk()
ob= Student(root)
root.mainloop()