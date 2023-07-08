from tkinter import*
from PIL import ImageTk
import psycopg2
from tkinter import messagebox

connection =psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="2135", port="5432")

cursor = connection.cursor()

def connect_database():
    if job_name_entry.get()== '' or Budget_entry.get() == '' or city_entry.get() == '' or Duration_entry.get() == '':
      messagebox.showerror('Error', 'All fileds are required')
    elif check_term.get()==0:
       messagebox.showerror('Eroor', 'Please accept Terms & Conditions')
    else:
       cursor.execute("""CREATE TABLE IF NOT EXISTS works(
                      id SERIAL PRIMARY KEY,
                      jobname varchar(255),                      
                      budget Integer,
                      city_entry VARCHAR(25),
                      duraction VARCHAR(30),
                      about VARCHAR(100)
       );  """)
       
       cursor.execute(""" INSERT INTO works(jobname, budget, city_entry, duraction, about) VALUES
                      (%s, %s,%s,%s,%s)""", (job_name_entry.get(),Budget_entry.get(), city_entry.get(), Duration_entry.get(),about_entry.get()))








userPannel_window=Tk()
userPannel_window.title('New work')
userPannel_window.resizable(False,FALSE)

# bg section
background = ImageTk.PhotoImage(file='userpannel.jpg')
background_label= Label(userPannel_window, image=background)
background_label.grid()


#heading label
heading= Label(userPannel_window, text='Thanks For Choosing US', font=('Microsoft Yahei UI Light', 25,'bold'), fg='firebrick1')
heading.place(x=35, y=280)

#New work heading

frame1 =  Frame(userPannel_window, bg='white')
frame1.place(x=630, y=100)

heading = Label(frame1, text='New Work', font=('Microsoft Yahei UI Light', 18,'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

#Job
job_name = Label(frame1 , text='Job Name', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
job_name.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

job_name_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
job_name_entry.grid(row=2, column=0, sticky='w', padx=25)  

#Budget

budget_label = Label(frame1 , text='Budget', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
budget_label.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

Budget_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
Budget_entry.grid(row=4, column=0, sticky='w', padx=25)  


#city
city_label = Label(frame1 , text='City', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
city_label.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

city_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
city_entry.grid(row=6, column=0, sticky='w', padx=25)  


# Duration 
Duration_label = Label(frame1 , text='Duration', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
Duration_label.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))

Duration_entry = Entry(frame1, width=30, font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
Duration_entry.grid(row=8, column=0, sticky='w', padx=25)  

#about

about_label = Label(frame1 , text='About', font=('Microsoft Yahei UI Light', 10,'bold'), bg='white',fg='firebrick1')
about_label.grid(row=9, column=0, sticky='w', padx=25, pady=(10,0))

about_entry = Entry(frame1, width=30,  font=('Microsoft Yahei UI Light', 10,'bold'), bg='firebrick1',fg='white')
about_entry.grid(row=10, column=0, sticky='w', padx=25 )  

# terms and condition
check_term= IntVar()
terms_and_condition = Checkbutton(frame1, text='I Agree to the Terms & Condition',
                            font=('Microsoft Yahei UI Light', 9,'bold'), fg='firebrick1', bg='white' ,
                              activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check_term)

terms_and_condition.grid(row=11, column=0, sticky='w', pady=10, padx=15)

# sign up button
save_work = Button(frame1, text='Save Work', font=('Open Sans', 16, 'bold'),  bd=0, bg='firebrick1', fg='white', 
                       activebackground='firebrick1', activeforeground='white', width=17, command=connect_database)
save_work.grid(row=12, column=0, pady=10)



userPannel_window.mainloop()
connection.commit()

cursor.close()
connection.close()