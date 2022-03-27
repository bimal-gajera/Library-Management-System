from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from datetime import date


database="library"
database_pass = "mysql@root"

books_table="books"
bookissue_table="bookissued"


def issue():

    mydb = pymysql.connect(host="localhost",user="root",password=database_pass,database=database)
    mycursor = mydb.cursor()

    bid = bookInfo1.get()
    issueto = bookUser
    today = str(date.today())

    allBid=[]
    
    try:
        extractBid = "select bid from "+books_table
        mycursor.execute(extractBid)
        
        for i in mycursor:
            allBid.append(i[0])
            
        if bid in allBid:
            checkAvail = "select book_status from "+books_table+" where bid=%s"
            mycursor.execute(checkAvail,(bid,))
            
            for i in mycursor:
                check = i[0]
            if check == 'available':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID is not present in database")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")

    try:
        if bid in allBid and status == True:
            mycursor.execute("insert into "+bookissue_table+" values(%s,%s,%s)",(bid,issueto,today))
            mydb.commit()

            mycursor.execute("update "+books_table+" set book_status = 'issued' where bid = '"+bid+"'")
            mydb.commit()
            messagebox.showinfo("Success","Book Issued Successfully")
        else:
            allBid.clear()
            messagebox.showinfo("Message","Book Already Issued")
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")



def clear():
    root.destroy()
    issueBook(bookUser)


def checkBook():
    # Add your own database name and password here to reflect in the code
    book_id = bookInfo1.get()

    try:

        mydb = pymysql.connect(host="localhost",user="root",password=database_pass,database=database)
        mycursor= mydb.cursor()

        q1 = "SELECT * FROM books WHERE bid=%s"
        mycursor.execute(q1,(book_id,))
        record = mycursor.fetchone()

        bookInfo2.insert(END,record[1])
        bookInfo3.insert(END,record[2])
        bookInfo4.insert(END,record[3])
        bookInfo5.insert(END,record[4])
    except:
        messagebox.showinfo("Error","Please check Book ID")
        bookInfo1.delete(0,END)


def issueBook(bookuserid): 
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,Canvas1,con,cur,bookTable,root,bookUser
    bookUser=bookuserid
    root = Tk()
    root.title("Library")
    root.geometry("600x500+20+20")
    root.configure(bg = "#f27333")
    

    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('aerial',15,"bold italic"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4) 

    # Book ID to 
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
    lb5 = Label(labelFrame,text="Status : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    bookInfo5 = Text(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.09)
    

    clearBtn = Button(root,text="Clear",bg='#d1ccc0', fg='black',command=clear)
    clearBtn.place(relx=0.05,rely=0.75, relwidth=0.18,relheight=0.08)

    checkBtn = Button(root,text="Check",bg='#d1ccc0', fg='black',command=checkBook)
    checkBtn.place(relx=0.8,rely=0.75, relwidth=0.18,relheight=0.08)


    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

