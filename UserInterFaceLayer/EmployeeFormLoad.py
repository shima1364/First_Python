from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.EmployeeCRUD_BLL import EmployeeCRUD_BLL_Class
from Model.EmployeeModel import EmployeeModel_Class
from UserInterFaceLayer import MenuBar


class EmployeeFormClass:
    def __init__(self):
        pass
    def EmployeeCRUDFormLoad(self):
        employeeFormObject = Tk()
        employeeFormObject.title('Employee Form')
        employeeFormObject.geometry('400x400')
        employeeFormObject.iconbitmap('images/EmployeeForm.ico')
        employeeFormObject.resizable(0, 0)
        x = int(employeeFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(employeeFormObject.winfo_screenheight() / 2 - 400 / 2)
        employeeFormObject.geometry('+{}+{}'.format(x, y))

        def employeeRegister():
            firstName = txtFirstName.get()
            lastName = txtLastName.get()
            nationalCode = txtNationalCode.get()
            sex = intSex.get()
            maritalStatus = intMaritalStatus.get()
            hireDate = txtHireDate.get()
            birthDate = txtBirthDate.get()

            employeeModel_Object = EmployeeModel_Class(fname=firstName, lname=lastName, ncode=nationalCode,
                                                       bdate=birthDate,
                                                       sex=sex, hdate=hireDate, mstatus=maritalStatus)

            employeeCRUD_BLL_Object = EmployeeCRUD_BLL_Class()
            employeeCRUD_BLL_Object.registerEmployee_BLL(employeeModel_Object)
            resetForm()




        def resetForm():
            for widget in employeeFormObject.winfo_children():
                #    if type(widget) == ttk.Entry:
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

        def checkValidation(*args):
            if len(txtNationalCode.get()) > 10:
                txtNationalCode.set(txtNationalCode.get()[:11])

            # if not txtNationalCode.get().isnumeric():
            #     txtNationalCode.set(txtNationalCode.get()[:len(txtNationalCode.get()) - 1])

            for char in txtNationalCode.get():
                if not char.isnumeric():
                    txtNationalCode.set(txtNationalCode.get().replace(char, ''))

        lbFirstName = Label(employeeFormObject, text='FirstName:')
        lbFirstName.grid(row=0, column=0, padx=10, pady=10)
        txtFirstName = StringVar()
        entFirstName = ttk.Entry(employeeFormObject, width=30, textvariable=txtFirstName)
        entFirstName.grid(row=0, column=1, padx=10, pady=10)

        lbLastName = Label(employeeFormObject, text='LastName:')
        lbLastName.grid(row=1, column=0, padx=10, pady=10)
        txtLastName = StringVar()
        entLastName = ttk.Entry(employeeFormObject, width=30, textvariable=txtLastName)
        entLastName.grid(row=1, column=1, padx=10, pady=10)

        lbNationalCode = Label(employeeFormObject, text='NationalCode:')
        lbNationalCode.grid(row=2, column=0, padx=10, pady=10)

        txtNationalCode = StringVar()
        txtNationalCode.trace('w', checkValidation)

        entNationalCode = ttk.Entry(employeeFormObject, width=30, textvariable=txtNationalCode)
        entNationalCode.grid(row=2, column=1, padx=10, pady=10)

        lbSex = Label(employeeFormObject, text='sex:')
        lbSex.grid(row=3, column=0, padx=10, pady=10)

        intSex = IntVar()
        rdSexMale = ttk.Radiobutton(employeeFormObject, text='Male', variable=intSex, value=1)
        rdSexMale.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        rdSexFemale = ttk.Radiobutton(employeeFormObject, text='Female', variable=intSex, value=2)
        rdSexFemale.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        #   intSex = IntVar()
        #  rdSexMale = ttk.Radiobutton(employeeFormObject, text='Male', variable=intSex, value=1)
        #  rdSexMale.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        #  rdSexFemale = ttk.Radiobutton(employeeFormObject, text='Female', variable=intSex, value=2)
        # rdSexFemale.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lbBirthDate = Label(employeeFormObject, text='Birthdate:')
        lbBirthDate.grid(row=4, column=0, padx=10, pady=10)
        txtBirthDate = StringVar()
        entBirthDate = DateEntry(employeeFormObject, width=26, textvariable=txtBirthDate)
        entBirthDate.grid(row=4, column=1, padx=10, pady=10)

        lbHireDate = Label(employeeFormObject, text='HireDate:')
        lbHireDate.grid(row=5, column=0, padx=10, pady=10)
        txtHireDate = StringVar()
        entHireDate = DateEntry(employeeFormObject, width=26, textvariable=txtHireDate)
        entHireDate.grid(row=5, column=1, padx=10, pady=10)

        lblMaritalStatus = Label(employeeFormObject, text='MaritalStatus: ')
        lblMaritalStatus.grid(row=6, column=0, padx=10, pady=10)

        intMaritalStatus = IntVar()
        rdMaritalStatusMarried = ttk.Radiobutton(employeeFormObject, text='Married', variable=intMaritalStatus, value=1)
        rdMaritalStatusMarried.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        rdMaritalStatusSingle = ttk.Radiobutton(employeeFormObject, text='Single', variable=intMaritalStatus, value=2)
        rdMaritalStatusSingle.grid(row=6, column=1, padx=10, pady=10, sticky='e')

        btnEmployeeRegister = ttk.Button(employeeFormObject, text='Employee Register... ', width=20,   command=employeeRegister)
        btnEmployeeRegister.grid(row=8, column=1, padx=10, pady=20, sticky='e')

        btnResetForm = ttk.Button(employeeFormObject, text='ResetForm', width=16, command=resetForm)
        btnResetForm.grid(row=8, column=1, padx=10, pady=20, sticky='w')

        employeeFormObject.mainloop()
