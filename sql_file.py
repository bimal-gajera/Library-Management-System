import pymysql
import csv


def sql_data():
    mydb = pymysql.connect(host = 'localhost', user = 'root', password = 'mysql@root')
    mycursor = mydb.cursor()

    q0="DROP DATABASE IF EXISTS library;"
    mycursor.execute(q0)

    create_db = "CREATE DATABASE library"
    mycursor.execute(create_db)

    mycursor.execute("use library")

    q1="""create table members(
        username char(30) primary key,
        email char(30) not null,
        securityKey char(30) not null)"""

    mycursor.execute(q1)

    q2="""insert into members (username,email,securityKey)
    values
    ('bimal','bimal@gmail.com','bimal123'),
    ('ishita','ishita@gmail.com','ishita123'),
    ('sandesh','sandesh@gmail.com','sandesh123'),
    ('rahul','rahul@gmail.com','rahul123'),
    ('abhay','abhay@gmail.com','abhay123'),
    ('parth','parth@gmail.com','parth123'),
    ('meet','meet@gmail.com','meet123'),
    ('dev','dev@gmail.com','dev123')"""

    mycursor.execute(q2)
    mydb.commit()


    q3="""create table books(
        bid char(3) primary key,
        title char(50),
        author char(20),
        category char(30),
        book_status char(15))"""
    mycursor.execute(q3)


    with open('Books_data.csv') as csv_file:
        csvfile=csv.reader(csv_file,delimiter=',')
        next(csvfile) #skips the first title row in csv file
        all_value= []
        for row in csvfile:
            value=(row[0],row[1],row[2],row[3],row[4])
            all_value.append(value)

    q4="insert into `books`(`bid`,`title`,`author`,`category`,`book_status`) values (%s,%s,%s,%s,%s)"
    mycursor.executemany(q4,all_value)
    mydb.commit()




    q5="""create table bookissued(
        book_id char(3) primary key,
        issuedto char(30),
        issuedate DATE,
        FOREIGN KEY (book_id) REFERENCES books(bid))""" 
    mycursor.execute(q5)


    q6="""insert into bookissued (issuedto,book_id,issuedate) values
    ('bimal','1','2021-07-01'),
    ('sandesh','2','2021-07-10'),
    ('ishita','3','2021-07-01'),
    ('rishi','4','2021-07-10'),
    ('bimal','5','2021-07-15'),
    ('rahul','6','2021-07-12'),
    ('abhay','7','2021-07-05'),
    ('parth','8','2021-07-10'),
    ('meet','9','2021-07-05'),
    ('dev','10','2021-07-10'),
    ('abhay','11','2021-07-15'),
    ('ishita','12','2021-07-12'),
    ('bimal','13','2021-07-20'),
    ('sandesh','14','2021-07-18'),
    ('rishi','15','2021-07-20')"""
    mycursor.execute(q6)
    mydb.commit()


sql_data()