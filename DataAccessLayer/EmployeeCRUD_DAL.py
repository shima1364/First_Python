import pyodbc
from Model.EmployeeModel import EmployeeModel_Class


class EmployeeCRUD_DAL_Class:
    def __init__(self):
        pass

    def registerEmployee_DAL(self, employee:EmployeeModel_Class):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=Sematec;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[RegisterEmployee] ?,?,?,?,?,?,?'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText, (employee.FirstName, employee.LastName,  employee.Birthdate, employee.NationalCode, employee.Sex
                                         , employee.MaritalStatus, employee.Hiredate))
            connection.commit()