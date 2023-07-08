from tkinter import*
from PIL import ImageTk




credit_window=Tk()
credit_window.title('Signup page')
credit_window.resizable(False,FALSE)

#function section
def open_new_work(): 
    credit_window.destroy()
    import new_work


# bg section
background = ImageTk.PhotoImage(file='userPannel.jpg')
background_label= Label(credit_window, image=background)
background_label.grid()


#credit
credit = Label(credit_window, text='Your Credit', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17)
credit.place(x=650, y=100)


#Increase credit
credits = Button(credit_window, text='Increase credit ', font=('Open Sans', 18, 'bold'),  bd=0, bg='white', fg='firebrick1', 
                       activebackground='firebrick1', activeforeground='white', width=17)
credits.place(x=650, y=250)



credit_window.mainloop()