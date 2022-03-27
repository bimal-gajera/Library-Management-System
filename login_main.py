from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql
import re
import os
import adding_function
import deleting_function
import issuing_function
import returning_function
import searching_function

lib_database="library"
database_pass="mysql@root"


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Library : Login and Registration")
        self.root.geometry("1366x700+70+70")
        self.root.resizable(False,False)
        self.loginform()
    
    
    def loginform(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg1.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        frame_input=Frame(self.root,bg='white')
        frame_input.place(x=320,y=130,height=450,width=350)
        label1=Label(frame_input,text="Library Login",font=('impact',32,'bold'),bg='white',fg="black")
        label1.place(x=50,y=20)

        label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='#fa5e1b',bg='white')
        label2.place(x=30,y=95)
        self.user_name=Entry(frame_input,font=("times new roman",15,"bold"), bg='lightgray')
        self.user_name.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='#fa5e1b',bg='white')
        label3.place(x=30,y=195)
        self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.password.place(x=30,y=245,width=270,height=35)

        btn1=Button(frame_input,text="forgot password?",command=self.forgot_password,cursor='hand2',font=('calibri',10),bg='white',fg='blue',width=15,height=1,bd=0)
        btn1.place(x=110,y=305)

        btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",width=15,height=1,bd=0)
        btn2.place(x=95,y=340)

        btn3=Button(frame_input,command=self.Register,text="Not Registered? register",cursor="hand2",font=("calibri",10),bg='white',fg="blue",width=20,height=1,bd=0)
        btn3.place(x=100,y=390)
        
        
        
    def login(self):
        if self.user_name.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password=database_pass,database=lib_database)
                cur=con.cursor()
                cur.execute('select * from members where username=%s and securityKey=%s',(self.user_name.get(),self.password.get()))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror('Error','Invalid Username or Password',parent=self.root)
                    self.loginclear()
                    self.user_name.focus()
                else:
                    self.libmenu()
                    con.close()
            except Exception as es:
                messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)
                

    def forgot_password(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg1.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

        frame_input=Frame(self.root,bg='white')
        frame_input.place(x=320,y=130,height=450,width=350)
        label1=Label(frame_input,text="Library Login",font=('impact',32,'bold'),bg='white',fg="black")
        label1.place(x=50,y=20)

        f1=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='#fa5e1b',bg='white')
        f1.place(x=30,y=95)
        self.f_username=Entry(frame_input,font=("times new roman",15,"bold"), bg='lightgray')
        self.f_username.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input,text="Email",font=("Goudy old style",20,"bold"),fg='#fa5e1b',bg='white')
        label3.place(x=30,y=195)
        self.f_email=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
        self.f_email.place(x=30,y=245,width=270,height=35)

        fbtn1=Button(frame_input,text="Get Password",command=self.fpass_get,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",width=15,height=1,bd=0)
        fbtn1.place(x=95,y=340)

        fbtn2=Button(frame_input,command=self.loginform,text="Login",cursor="hand2",font=("calibri",10),bg='white',fg="blue",bd=0)
        fbtn2.place(x=160,y=390)





    def fpass_get(self):
        if self.f_username.get()=="" or self.f_email.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password=database_pass,database=lib_database)
                cur=con.cursor()
                cur.execute('select securityKey from members where username=%s and email=%s',(self.f_username.get(),self.f_email.get()))
                fkey=cur.fetchone()

                if fkey==None:
                    messagebox.showerror('Error','Invalid Username or Password',parent=self.root)
                    self.forgot_pass_clear()
                    self.f_username.focus()
                else:
                    Frame_login=Frame(self.root,bg="white")
                    Frame_login.place(x=0,y=0,height=700,width=1366)
                    self.img=ImageTk.PhotoImage(file="bg1.jpg")
                    img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)

                    frame_input=Frame(self.root,bg='white')
                    frame_input.place(x=320,y=130,height=450,width=350)
                    label1=Label(frame_input,text="forgot password",font=('impact',32,'bold'),bg='white',fg="black")
                    label1.place(x=40,y=20)

                    f1=Label(frame_input,text="Password:",font=("Goudy old style",20,"bold"),fg='black',bg='white')
                    f1.place(x=30,y=95)
                    f1=Label(frame_input,text=fkey,font=("Goudy old style",20,"bold"),fg='#fa5e1b',bg='white')
                    f1.place(x=50,y=150)

                    fbtn1=Button(frame_input,text="Login",command=self.loginform,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",width=15,height=1,bd=0)
                    fbtn1.place(x=90,y=340)


            except Exception as es:
                messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)



    def forgot_pass_clear(self):
        self.f_username.delete(0,END)
        self.f_email.delete(0,END)





    def Register(self):
        Frame_login1=Frame(self.root,bg="white")
        Frame_login1.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg1.jpg")
        img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

        frame_input2=Frame(self.root,bg='white')
        frame_input2.place(x=320,y=130,height=450,width=630)

        label1=Label(frame_input2,text="Library Registration",font=('impact',32,'bold'),fg="black",bg='white')
        label1.place(x=45,y=20)

        label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        label2.place(x=30,y=95)
        self.entry1=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry1.place(x=30,y=145,width=270,height=35)

        label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        label3.place(x=30,y=195)
        self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry2.place(x=30,y=245,width=270,height=35)

        label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        label4.place(x=330,y=95)
        self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
        self.entry3.place(x=330,y=145,width=270,height=35)

        label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
        label5.place(x=330,y=195)
        self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"), bg='lightgray')
        self.entry4.place(x=330,y=245,width=270,height=35)

        btn1=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn1.place(x=90,y=340)
        
        btn2=Button(frame_input2,command=self.loginform,text="Already Registered? Login",cursor="hand2",font=("calibri",10),bg='white',fg="blue",bd=0)
        btn2.place(x=110,y=390)
    

    def register(self):
        regex = '/^[a-zA-Z0-9]+[@]gmail.com$/'
        if self.entry1.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)
        elif (re.match(regex,self.entry3.get())==False):
            messagebox.showerror("Error! Please enetr a valid email")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password=database_pass,database=lib_database)
                cur=con.cursor()
                cur.execute("select * from members where username=%s",self.entry1.get())
                row=cur.fetchone()
                
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
                    self.regclear()
                    self.entry1.focus()
                else:
                    cur.execute("insert into members values(%s,%s,%s)",(self.entry1.get(),self.entry3.get(),self.entry2.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Succesfull",parent=self.root)
                    self.regclear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    
    
    def regclear(self):
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)  
    
    def loginclear(self):
        self.user_name.delete(0,END)
        self.password.delete(0,END)
    
    
    def libmenu(self):
        Frame_menu=Frame(self.root,bg="white")
        Frame_menu.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg1.jpg")
        img=Label(Frame_menu,image=self.img).place(x=0,y=0,width=1366,height=700)

        headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to Library", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        btn1 = Button(root,text="Add Book to Database",bg='black', fg='white',command=adding_function.addBook)
        btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

        btn2 = Button(root,text="Delete Book from Database",bg='black', fg='white',command=deleting_function.delete)
        btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

        btn3 = Button(root,text="Search Book",bg='black', fg='white',command=searching_function.searchmenu)
        btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

        btn4 = Button(root,text="Issue Book",bg='black', fg='white',command=self.book_issue_call)
        btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

        btn5 = Button(root,text="Return Book",bg='black', fg='white',command=self.book_return_call)
        btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

        btn2=Button(Frame_menu,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",width=15,height=1,bd=0)
        btn2.place(x=1000,y=10)


    def book_issue_call(self):
        issuing_function.issueBook(self.user_name)

    def book_return_call(self):
        returning_function.returnBook(self.user_name)
        


root=Tk()

ob=Login(root)

root.mainloop()
