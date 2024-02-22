from abc import ABC, abstractmethod

class PersonModel_Class(ABC):

    def __init__(self, fname, lname, ncode, bdate, education, sex):
        self.FirstName = fname
        self.LastName = lname
        self.NationalCode = ncode
        self.Birthdate = bdate
        self.Education = education
        self.Sex = sex

    @abstractmethod
    def myMethod(self):
        pass

    def getFullName(self):
        return self.FirstName + ' ' + self.LastName


class EmployeeModel_Class(PersonModel_Class):
    def __init__(self, fname, lname, ncode, bdate, education, sex, hdate, mstatus):
        super().__init__(fname, lname, ncode, bdate, education, sex)
        self.Hiredate = hdate
        self.MaritalStatus = mstatus

    def myMethod(self):
        pass