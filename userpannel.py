from tkinter import*
from PIL import ImageTk




userPannel_window=Tk()
userPannel_window.title('User pannel')
userPannel_window.resizable(False,FALSE)

#function section
def open_new_work(): 
    userPannel_window.destroy()
    import new_work


# bg section
background = ImageTk.PhotoImage(file='userpannel.jpg')
background_label= Label(userPannel_window, image=background)
background_label.grid()


#heading label
heading= Label(userPannel_window, text='Welcome TO Pannel', font=('Microsoft Yahei UI Light', 25,'bold'), fg='firebrick1')
heading.place(x=35, y=280)

#New work
new_work = Button(userPannel_window, text='New Work', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17, command=open_new_work)
new_work.place(x=650, y=100)

works = Button(userPannel_window, text='works', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17)
works.place(x=650, y=200)

#Increase credit
credits = Button(userPannel_window, text='credit', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17)
credits.place(x=650, y=300)


edit_account = Button(userPannel_window, text='Edit Account', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17)
edit_account.place(x=650, y=400)

delete_account = Button(userPannel_window, text='Delete Account', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17)
delete_account.place(x=650, y=500)


userPannel_window.mainloop()
