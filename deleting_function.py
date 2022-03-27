from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

database="library"
database_pass = "mysql@root"

books_table = "books"


def checkBook():
    book_id = bookInfo1.get()

    try:
        if book_id=="":
            messagebox.showinfo("Error","Please enter Book ID")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password=database_pass,database=database)
            mycursor= mydb.cursor()

            q1 = "SELECT * FROM "+books_table+" WHERE bid=%s"
            mycursor.execute(q1,(book_id,))
            record = mycursor.fetchone()

            bookInfo2.insert(END,record[1])
            bookInfo3.insert(END,record[2])
            bookInfo4.insert(END,record[3])
            bookInfo5.insert(END,record[4])
    except:
        messagebox.showinfo("Error","Please check Book ID")
        bookInfo1.delete(0,END)


def delete_book():
    book_id = bookInfo1.get()
    
    try:

        mydb = mysql.connector.connect(host="localhost",user="root",password=database_pass,database=database)
        mycursor= mydb.cursor()

        q2 = "SELECT * FROM "+books_table+" WHERE bid=%s"
        mycursor.execute(q2,(book_id,))
        record1 = mycursor.fetchone()

        if record1[4]=="issued":
            messagebox.showinfo("Error","Data can't be deleted\nBook is issued to user")
            clear()
        else:
            q3 = "DELETE FROM "+books_table+" WHERE bid = %s"
            mycursor.execute(q3,(book_id,))
            mydb.commit()
            messagebox.showinfo("Book-Deletion","Record deleted successfully")
            clear()
    except:
        messagebox.showinfo("Error","Please check Book ID")
        bookInfo1.delete(0,END)



def clear():
    root.destroy()
    delete()



def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.geometry("600x500+10+10")
    root.configure(bg = "#f23030")

    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('aerial',15,"bold italic"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.09)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Text(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.09)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Text(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.09)

    # Book category
    lb4 = Label(labelFrame,text="Category: ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Text(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.09)


    # Book Status
    lb5 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    bookInfo5 = Text(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.09)


    clearBtn = Button(root,text="Clear",bg='#d1ccc0', fg='black',command=clear)
    clearBtn.place(relx=0.05,rely=0.75, relwidth=0.18,relheight=0.08)

    checkBtn = Button(root,text="Check",bg='#d1ccc0', fg='black',command=checkBook)
    checkBtn.place(relx=0.8,rely=0.75, relwidth=0.18,relheight=0.08)


    #Submit Button
    deleteBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',command=delete_book)
    deleteBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
