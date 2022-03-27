from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

#database name and password
database="library"
database_pass = "mysql@root"

books_table = "books" # Book Table

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    category = bookInfo4.get()
    status ="available"


    if bid=="" or title=="" or author=="" or category=="" or status=="":
        messagebox.showerror("Error","All Fields Are Required",parent=root)
    else:
        try:

            mydb = pymysql.connect(host="localhost",user="root",password=database_pass,database=database)
            mycursor = mydb.cursor()


            mycursor.execute("insert into "+books_table+" values(%s,%s,%s,%s,%s)",(bid,title,author,category,status))
            mydb.commit()
            messagebox.showinfo('Success',"Book added successfully")
            add_data_clear()
        except:
            messagebox.showinfo("Error","Can't add data into Database")
            add_data_clear()



def add_data_clear():
    bookInfo1.delete(0,END)
    bookInfo2.delete(0,END)
    bookInfo3.delete(0,END)
    bookInfo4.delete(0,END)

    


def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.geometry("600x500+10+10")
    root.configure(bg="#b198fa")


    headingFrame1 = Frame(root,bg="#f38fa9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # Book category
    lb4 = Label(labelFrame,text="Category: ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#ede6d6', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#ede6d6', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()



