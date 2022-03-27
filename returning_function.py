from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


database="library"
database_pass = "mysql@root"

books_table="books"
bookissue_table="bookissued"


mydb = pymysql.connect(host="localhost",user="root",password=database_pass,database=database)
mycursor = mydb.cursor()

bookissue_table = "bookissued" 
books_table = "books" 


allBid = []



def book_return():
    
    global status
    
    b_id = bookInfo1.get()
    u_id = bookUser
    #try:
    extractBid = "select book_id from "+bookissue_table+" where issuedto = %s"
    mycursor.execute(extractBid,(u_id,))

    for i in mycursor:
        allBid.append(i[0])
    
    if b_id in allBid:
        mycursor.execute("select book_status from "+books_table+" where bid = "+b_id)

        for i in mycursor:
            check = i[0]
            
        if check == 'issued':
            status = True
        else:
            status = False
    else:
        messagebox.showinfo("Error","You have not issued book of entered ID")
    #except:
        #messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    try:
        if b_id in allBid and status == True:
            q1="delete from "+bookissue_table+" where book_id=%s and issuedto=%s"
            mycursor.execute(q1,(b_id,u_id,))
            mydb.commit()
            mycursor.execute("update "+books_table+" set book_status = 'available' where bid = "+b_id)
            mydb.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBid.clear()
    





def returnBook(bookuserid): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame,lb1,bookUser
    bookUser=bookuserid
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500+20+20")

    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#a9f558")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=book_return)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

