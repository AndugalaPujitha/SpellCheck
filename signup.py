from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3
from tkinter import messagebox
def login_page():
    signup_window.destroy()
    import login
 
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def email_enter(event):
    if emailEntry.get()=='email':
        emailEntry.delete(0,END)              
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)  
def confirmpassword_enter(event):
    if confirmpasswordEntry.get()=='confirmPassword':
        confirmpasswordEntry.delete(0,END)           
    
#Function to create the database table
conn = sqlite3.connect('signup.db')
cursor = conn.cursor()
table_create_query = ('''CREATE TABLE IF NOT EXISTS login_data
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT NOT NULL,Username TEXT NOT NULL,
                   Password TEXT UNIQUE NOT NULL,
                   confirmPassword TEXT UNIQUE NOT NULL
                )
            ''')
    
cursor.execute(table_create_query)


def login_user(email,Username,Password,confirmPassword):
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()
    data_insert_query = '''INSERT INTO login_data (email, Username, Password, confirmPassword) VALUES(?, ?, ?, ?)'''
    # data_insert_tuple = (f"'{email}','{Username}','{Password},'{confirmPassword}'")
    data_insert_tuple = (email, Username, Password, confirmPassword)
    cursor.execute(data_insert_query,data_insert_tuple)
    messagebox.showinfo("Information","Account created Succesfully")
    messagebox.showinfo("Information","Now you can login")
    conn.commit()
conn.close()


signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

signup_window.iconphoto(False, tk.PhotoImage(file='logo.png'))

background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)
emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                               fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',
                    activebackground='firebrick1',activeforeground='white',width=17,command=lambda: login_user(emailEntry.get(), usernameEntry.get(),
                                                 passwordEntry.get(), confirmpasswordEntry.get()))
signupButton.grid(row=10,column=0,pady=10)
alreadyaccount=Label(frame,text="Dont have an account?",font=('Open Sans','9','bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)
loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline')
                   ,bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=404)
signup_window.mainloop()

