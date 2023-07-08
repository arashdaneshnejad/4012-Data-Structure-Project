from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import psycopg2

###############  Functionality SECTION ############
def hide(): 
    open_eye.config(file='closeye.png')
    password_entry.config(show='*')
    eye_Button.config(command=show)
def show():
    open_eye.config(file='openeye.png')
    password_entry.config(show='')
    eye_Button.config(command=hide)


def userName_enter(event):
    if user_name_entry.get()== 'Username':
        user_name_entry.delete(0, END)

def password_enter(event):
    if password_entry.get()== 'Password':
        password_entry.delete(0, END)


def sign_up_page():
    oprator_login_window.destroy()
    import opratorsignup

def open_opr_pannel():
    oprator_login_window.destroy()
    import oparatorpannel
#data base

def connect_database():
    connection =psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="2135", port="5432")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from oprator"

    cursor.execute(postgreSQL_select_Query)
    oprator = cursor.fetchall()
    print(oprator)

    print(user_name_entry.get())
    for opr in oprator:
        (id,email,username,password) = opr
        if username == user_name_entry.get() and password == password_entry.get():
            open_opr_pannel()
        else:
            messagebox.showerror("Error", "loggied faild")    








    

###############  GUI SECTION ############
oprator_login_window= Tk()
oprator_login_window.geometry('990x660+50+50')
oprator_login_window.title('Login Page')

#Background section
background_image = ImageTk.PhotoImage(file='bg.jpg')
background_label = Label(oprator_login_window, image=background_image)
background_label.place(x=0, y=0)

#Heading section
heading = Label(oprator_login_window, text='OPR LOGIN', font=('Microsoft Yahei UI Light', 23,'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

#User Name
user_name_entry = Entry(oprator_login_window, width=25, font=('Microsoft Yahei UI Light', 11,'bold'), bd='0', fg='firebrick1')
user_name_entry.place(x=580, y=200)
user_name_entry.insert(0, 'Username')

user_name_entry.bind('<FocusIn>', userName_enter)

frame1 =Frame(oprator_login_window, width=250, height=2,bg='firebrick1')
frame1.place(x=580, y=222)

#password 
password_entry = Entry(oprator_login_window, width=25, font=('Microsoft Yahei UI Light', 11,'bold'), bd='0', fg='firebrick1')
password_entry.place(x=580, y=260)
password_entry.insert(0, 'Password')

password_entry.bind('<FocusIn>', password_enter)

frame2 =Frame(oprator_login_window, width=250, height=2,bg='firebrick1')
frame2.place(x=580, y=282)

#open and close eye section
open_eye = PhotoImage(file='openeye.png')
eye_Button=Button(oprator_login_window, image=open_eye, bd=0, bg='White', activebackground='white', cursor='hand2', command=hide)

eye_Button.place(x=800, y=255)

forget_password = Button(oprator_login_window, text='Forger Password?', bd=0, bg='White', activebackground='white', cursor='hand2',
                          font=('Microsoft Yahei UI Light', 9,'bold'), fg='firebrick1', activeforeground='firebrick1')

forget_password.place(x=715, y=295)

#login

login_Button= Button(oprator_login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',activeforeground='white',
                      activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=connect_database)

login_Button.place(x=578,y=350)

sign_up= Label(oprator_login_window, text='DONT HAVe AN ACCOUNT?', font=('Open Sans', 9, 'bold'), fg='firebrick1', bg='white')
sign_up.place(x=590, y=400)

sign_up_button= Button(oprator_login_window, text='Create account', font=('Open Sans', 9, 'bold'), fg='white', bg='firebrick1',activeforeground='white',
                      activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=sign_up_page)

sign_up_button.place(x=578,y=500)


oprator_login_window.mainloop()
