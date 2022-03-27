from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

database="library"
database_pass = "mysql@root"


mydb = pymysql.connect(host="localhost",user="root",password=database_pass,database=database)
mycursor = mydb.cursor()

books_table = "books"



def view_frame():

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#5ceb49")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    hFrame1 = Frame(root,bg="white",bd=5)
    hFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    hLabel = Label(hFrame1, text="Search Books", bg='black', fg='white', font=('Courier',15))
    hLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    returnBtn = Button(root,text="Return to\nsearch menu",bg='#f7f1e3', fg='black',command=call_searchmenu)
    returnBtn.place(relx=0.15,rely=0.9, relwidth=0.18,relheight=0.08)


    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.7,rely=0.9, relwidth=0.18,relheight=0.08)
    
    global tree
    tree = ttk.Treeview(root, column=('BID','Title','Author','Category','Status'), show='headings')

    tree.column("#1", anchor=CENTER,width=60)
    tree.heading("#1", text="Bid")

    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="Title")

    tree.column("#3", anchor=CENTER,width=180)
    tree.heading("#3", text="Author")

    tree.column("#4", anchor=CENTER,width=150)
    tree.heading("#4", text="Category")

    tree.column("#5", anchor=CENTER,width=100)
    tree.heading("#5", text="Status")
    tree.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)



def view_all_books():
    try:
        mycursor.execute("select * from "+books_table)
        rows = mycursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")



def view_available():
    try:
        mycursor.execute("select * from "+books_table+" where book_status='available'")
        rows = mycursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")



def search_bookid():
    global w1
    w1 = Tk()
    w1.title("Library Search")
    w1.geometry('400x300')
    w1.configure(bg='white')
    
    hf1 = Frame(w1,bg='green')
    hf1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
        
    l1 = Label(hf1,text="Book ID : ", bg='white', fg='black', font=('Courier',10))
    l1.place(relx=0.1,rely=0.5, relwidth=0.3, relheight=0.1)

    global id_book
    id_book = Entry(hf1)
    id_book.place(relx=0.4,rely=0.5, relwidth=0.5, relheight=0.1)

    SubmitBtn = Button(w1,text="Enter",bg='#ede6d6', fg='black',command=search_bookid_data)
    SubmitBtn.place(relx=0.4,rely=0.8, relwidth=0.18,relheight=0.08)


def search_bookid_data():
    id_search=id_book.get()
    try:
        q1="select * from "+books_table+" where bid=%s"
        mycursor.execute(q1,(id_search,))
        rows = mycursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
        w1.destroy()
        
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")

    tryBtn1 = Button(root,text="Search again",bg='#f7f1e3', fg='black',command=srchagain)
    tryBtn1.place(relx=0.45,rely=0.85, relwidth=0.11,relheight=0.08)



def srchagain():
    for item in tree.get_children():
        tree.delete(item)
    search_bookid()
    


def category_search():
    all_ctgry=[]

    global w2
    w2 = Tk()
    w2.title("Library Search")
    w2.geometry('400x500')    
    mycursor.execute("SELECT DISTINCT category FROM "+books_table)

    for i in mycursor:
        all_ctgry.append(i[0])

    l1=ttk.Label(w2,text="Search by Category",background='green',foreground="white",font=("Times New Roman",15))
    l1.place(relx=0.35,rely=0.1)

    l2=ttk.Label(w2,text="Select Category:",font=("Times New Roman", 10))
    l2.place(relx=0.15,rely=0.3)

    n = StringVar()
    global cat_choosen
    cat_choosen= ttk.Combobox(w2, width = 27, textvariable = n)

    cat_choosen['values']=tuple(all_ctgry)
    cat_choosen.place(relx=0.4,rely=0.3)
    cat_choosen.current()

    entrBtn = Button(w2,text="Enter",bg='#f7f1e3', fg='black',command=cat_search_get)
    entrBtn.place(relx=0.45,rely=0.85, relwidth=0.11,relheight=0.08)


def cat_search_get():
    a=cat_choosen.get()

    try:
        cquery="select * from "+books_table+" where category=%s"
        mycursor.execute(cquery,(a,))
        rows = mycursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
        w2.destroy()
        
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")
    
    tryBtn2 = Button(root,text="Try again",bg='#f7f1e3', fg='black',command=cat_newsrch)
    tryBtn2.place(relx=0.45,rely=0.85, relwidth=0.11,relheight=0.08)


def cat_newsrch():
    for item in tree.get_children():
        tree.delete(item)
    category_search()





def title_search():
    global w3
    w3 = Tk()
    w3.title("Library Search")
    w3.geometry('400x500')

    l1=Label(w3,text="Search by Title",bg='green',fg="white",font=("Times New Roman",15))
    l1.place(relx=0.35,rely=0.1)

    l2 = Label(w3,text="Title : ", font=('Courier',10))
    l2.place(relx=0.1,rely=0.5, relwidth=0.3, relheight=0.1)

    global t_search
    t_search=Entry(w3)
    t_search.place(relx=0.4,rely=0.5, relwidth=0.5, relheight=0.08)

    SubmitBtn = Button(w3,text="Enter",bg='#ede6d6',fg='black',command=search_title_data)
    SubmitBtn.place(relx=0.4,rely=0.8, relwidth=0.18,relheight=0.08)


def search_title_data():
    tid=t_search.get()
    try:
        tquery="select * from "+books_table+" where title=%s"
        mycursor.execute(tquery,(tid,))
        rows = mycursor.fetchall()
        for row in rows:
            tree.insert("", END, values=row)
        w3.destroy()
        
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")
    
    tryBtn2 = Button(root,text="Try again",bg='#f7f1e3', fg='black',command=title_newsrch)
    tryBtn2.place(relx=0.45,rely=0.85, relwidth=0.11,relheight=0.08)



def title_newsrch():
    for item in tree.get_children():
        tree.delete(item)
    title_search()



def call_searchmenu():
    root.destroy()
    searchmenu()



def searchmenu():

    global root

    root = Tk()
    root.title("Library")
    root.geometry("1000x700+10+10")
    root.configure(bg = "#f27333")

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Library book search", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="View all books",bg='black', fg='white',command=lambda:[view_frame(),view_all_books()])
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="View all available books",bg='black', fg='white',command=lambda:[view_frame(),view_available()])
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="Search book by book ID",bg='black', fg='white',command=lambda:[view_frame(),search_bookid()])
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Search book by category",bg='black', fg='white',command=lambda:[view_frame(),category_search()])
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Search Book by title",bg='black', fg='white',command=lambda:[view_frame(),title_search()])
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)


    returnBtn = Button(root,text="Return to\nsearch menu",bg='#f7f1e3', fg='black',command=call_searchmenu)
    returnBtn.place(relx=0.15,rely=0.9, relwidth=0.18,relheight=0.08)


    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.7,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
