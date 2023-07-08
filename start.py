from tkinter import*
from PIL import ImageTk




start_window=Tk()
start_window.title('App')
start_window.resizable(False,FALSE)

#function section
def open_user_section():
    start_window.destroy()
    import signup

def open_oprator_section():
    start_window.destroy()
    import opratorsignup    


# bg section
background = ImageTk.PhotoImage(file='userpannel.jpg')
background_label= Label(start_window, image=background)
background_label.grid()


#heading label
heading= Label(start_window, text='Welcome TO App', font=('Microsoft Yahei UI Light', 25,'bold'), fg='firebrick1')
heading.place(x=35, y=280)

#user
user = Button(start_window, text='USER', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17, command=open_user_section)
user.place(x=650, y=200)
#oprator
oprator = Button(start_window, text='OPRATOR', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17 , command=open_oprator_section)
oprator.place(x=650, y=300)




start_window.mainloop()
