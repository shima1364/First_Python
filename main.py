from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
import pyodbc
from UserInterFaceLayer.MainFormModule import MainForm
from UserInterFaceLayer import MenuBar

loginFormObject = Tk()
menu_bar = MenuBar(loginFormObject)  # Pass loginFormObject as parent
loginFormObject.config(menu=menu_bar.menu_bar)

loginFormObject.title('Login form')
loginFormObject.geometry('300x200')
loginFormObject.wm_iconbitmap('Images/Login_Icon.ico')
loginFormObject.resizable(0, 0)
x = int(loginFormObject.winfo_screenwidth() / 2 - 300 / 2)
y = int(loginFormObject.winfo_screenheight() / 2 - 200 / 2)
loginFormObject.geometry('+{}+{}'.format(x, y))


def checkLogin():
    username = txtUserName.get()
    password = txtPassword.get()

    connectionString = 'Driver={SQL Server};Server=localhost;Database=Sematec;Trusted_Connection=yes;'
    commandText = 'exec [dbo].[checkLogin] ?,?'
    params = (username, password)
    with pyodbc.connect(connectionString) as connection:
        curser = connection.cursor()
        curser.execute(commandText, (username, password))
        rows = curser.fetchone()
    if rows is not None:
        # msg.showinfo('wellcome', f'Welcome {rows[2]} {rows[3]}')
        loginFormObject.destroy()
        MainFormObject = MainForm()
        MainFormObject.MainFormLoad(fName=rows[2], lName=rows[3])
    else:
        msg.showerror('Error', 'Invalid username or password')

    # if username == 'admin' and password == '<admin>':
    #   msg.showinfo('wellcome', 'wellcome Admin')
    # else:
    #   msg.showerror('Error', 'Invalid username or password')


lbUserName = Label(loginFormObject, text='UserInfo:')
lbUserName.grid(row=0, column=0, padx=10, pady=10)
txtUserName = StringVar()
entUserName = ttk.Entry(loginFormObject, width=30, textvariable=txtUserName)
entUserName.grid(row=0, column=1, padx=10, pady=10)

lbPassword = Label(loginFormObject, text='password:')
lbPassword.grid(row=1, column=0, padx=10, pady=10)
txtPassword = StringVar()
entPassword = ttk.Entry(loginFormObject, width=30, show='*', textvariable=txtPassword)
entPassword.grid(row=1, column=1, padx=10, pady=10)
BtnLogin = ttk.Button(loginFormObject, text='login', width=20, command=checkLogin)
BtnLogin.grid(row=2, column=1, padx=10, pady=20, sticky='e')

loginFormObject.mainloop()
