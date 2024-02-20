from DataAccessLayer.EmployeeCRUD_DAL import EmployeeCRUD_DAL_Class
from Model.EmployeeModel import EmployeeModel_Class


class EmployeeCRUD_BLL_Class:

    def __init__(self):
        pass


    def registerEmployee_BLL(self, employee: EmployeeModel_Class):
        employeeCRUD_DAL_Object = EmployeeCRUD_DAL_Class()
        employeeCRUD_DAL_Object.registerEmployee_DAL(employee)