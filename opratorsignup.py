from tkinter import*
from PIL import ImageTk
import psycopg2
from tkinter import messagebox

connection =psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="2135", port="5432")

cursor = connection.cursor()


def connect_database():
    if email_entry.get()== '' or userName_entry.get() == '' or confirm_password_entry.get() == '':
      messagebox.showerror('Error', 'All fileds are required')
    elif password_entry.get() != confirm_password_entry.get():
       messagebox.showerror('Error', 'password not matched')
    elif check_term.get()==0:
       messagebox.showerror('Eroor', 'Please accept Terms & Conditions')
    else:
       cursor.execute("""CREATE TABLE IF NOT EXISTS oprator(
                      id SERIAL PRIMARY KEY,
                      email varchar(255),                      
                      username VARCHAR(255),
                      password VARCHAR(25)
       );  """)
       
       cursor.execute(""" INSERT INTO oprator(email, username, password) VALUES
                      (%s, %s,%s)""", (email_entry.get(),userName_entry.get(), password_entry.get()))






def login_page(): 
    signup_window.destroy()
    import oparatorlogin



signup_window=Tk()
signup_window.title('Signup page Operator')
signup_window.resizable(False,FALSE)

# bg section
background = ImageTk.PhotoImage(file='bg.jpg')
background_label= Label(signup_window, image=background)
background_label.grid()


#heading section
frame1 =  Frame(signup_window, bg='white')
frame1.place(x=554, y=100)

heading = Label(frame1, text=' Operator Account', font=('Microsoft Yahei UI Light', 18,'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

#email section
email_label = Label(frame1 , text='Email', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
email_label.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

email_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
email_entry.grid(row=2, column=0, sticky='w', padx=25)  

#user name section

userName_label = Label(frame1 , text='UserName', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
userName_label.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

userName_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
userName_entry.grid(row=4, column=0, sticky='w', padx=25)  

# password section
password_label = Label(frame1 , text='Password', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
password_label.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

password_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
password_entry.grid(row=6, column=0, sticky='w', padx=25)  

#confirm password

confirm_password_label = Label(frame1 , text='Confirm Password', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
confirm_password_label.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))

confirm_password_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
confirm_password_entry.grid(row=8, column=0, sticky='w', padx=25)  

# terms and condition
check_term= IntVar()
terms_and_condition = Checkbutton(frame1, text='I Agree to the Terms & Condition',
                            font=('Microsoft Yahei UI Light', 9,'bold'), fg='firebrick1', bg='white' ,
                              activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check_term)

terms_and_condition.grid(row=9, column=0, sticky='w', pady=10, padx=15)

# sign up button
signup_button = Button(frame1, text='signup', font=('Open Sans', 16, 'bold'),  bd=0, bg='firebrick1', fg='white', 
                       activebackground='firebrick1', activeforeground='white', width=17, command=connect_database)
signup_button.grid(row=10, column=0, pady=10)


already_account = Label(frame1, text='Already Have An Account', font=('Open Sans', '9',  'bold'),
                        bg='white', fg='firebrick')
already_account.grid(row=11, column=0, sticky='w', padx=25, pady=10)

login_button= Button(frame1, text='Log in', font=('Open Sans', 9, 'bold underline')
                     ,bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white', activeforeground='blue', command=login_page)

login_button.place(x=170, y='402')


signup_window.mainloop()
connection.commit()

cursor.close()
connection.close()  