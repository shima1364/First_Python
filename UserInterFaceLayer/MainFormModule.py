from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from UserInterFaceLayer.EmployeeFormLoad import EmployeeFormClass


class MainForm:
    def MainFormLoad(self, fName, lName):
        MainFormObject = Tk()

        MainFormObject.title('Main form')
        MainFormObject.geometry('600x400')
        MainFormObject.wm_iconbitmap('Images/MainForm.ico')
        MainFormObject.resizable(0, 0)
        x = int(MainFormObject.winfo_screenwidth() / 2 - 600 / 2)
        y = int(MainFormObject.winfo_screenheight() / 2 - 400 / 2)
        MainFormObject.geometry('+{}+{}'.format(x, y))

        def employeeFormLoad():
            MainFormObject.destroy()
            employeeFormObject = EmployeeFormClass()
            employeeFormObject.EmployeeCRUDFormLoad()

        lbWellcomeMessage = Label(MainFormObject, text=f'Wellcome {fName} {lName}')
        lbWellcomeMessage.grid(row=0, column=0, padx=10, pady=10)

        employeeCRUD = PhotoImage(file='images/Employee.png')
        btnEmployeeCRUD = Button(MainFormObject, text='Employee CRUD', compound=TOP, image=employeeCRUD,
                                 command=employeeFormLoad)
        btnEmployeeCRUD.grid(row=1, column=0, padx=10, pady=20, sticky='e')
        MainFormObject.mainloop()
