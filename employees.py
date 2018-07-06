class Company_Employee(object):
    """This represents employees"""

    def __init__(self, employee_name, company=None):
        self.employee_name = employee_name
        self.company_name = company

    def change_self_name(self, input_name):
        """Changes the name of the employee"""
        self.employee_name = input_name

    def change_company_name(self, input_name):
        """Changes the name of the employee"""
        if(self.company_name is None):
            self.company_name = input_name
            
        else:
            self.company_name.leaving_employee(self)
            self.company_name = input_name
        

    def quit(self):
        self.company_name.leaving_employee(self)
        self.company_name = None

    def get_company_name(self):
        if(self.company_name is None):
            return "No Company"

        else:
            return self.company_name.get_company_name()

james = Company_Employee("James")

james.change_self_name("Jamie")

john = Company_Employee("John")

joe = Company_Employee("Joe")

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name
            
    
    def hire_employee(self, employee):
        employee.change_company_name(self)
        self.employees.append(employee)

    def fire_employee(self, employee):
        if(employee in self.employees):
            self.employees.remove(employee)
            employee.change_company_name(None)
        
        
    def leaving_employee(self, employee):
        if(employee in self.employees):
            self.employees.remove(employee)

evilCorp = Company("E Corp", "1995")

otherCorp = Company("Other Corporation", "1905")

evilCorp.hire_employee(james)

evilCorp.hire_employee(john)

evilCorp.hire_employee(joe)

otherCorp.hire_employee(joe)

otherCorp.fire_employee(joe)

john.quit()

print(joe.get_company_name())


print(len(evilCorp.employees))


    # Add the remaining methods to fill the requirements above
