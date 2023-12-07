'''
  this example shows these features:
  1. class init method
  2. instance and class variables
  3. difference between accessing class variable form instance or from class
  4. instance method, class method and static method
  5. use class method as an alternative for making an instance of the class
  6. inheritance and creating subclasses
  7. special (magic/Dunder) methods
  8. property decorators - getters, setters and deleters
'''


class Employee:
    salary_raise = 1.04
    number_of_employees = 0

    def __init__(self, firstname, lastname, salary) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

        Employee.number_of_employees += 1

    @property
    def email(self):
        return f'{self.firstname}.{self.lastname}@company.com'

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, fullname):
        firstname, lastname = fullname.split(' ')
        self.firstname = firstname
        self.lastname = lastname

    @fullname.deleter
    def fullname(self):
        print('fullname deleted!')
        self.firstname = None
        self.lastname = None

    def apply_raise(self):
        self.salary = int(self.salary) * self.salary_raise

    @classmethod
    def set_salary_raise(cls, salary_raise):
        cls.salary_raise = salary_raise

    @classmethod
    def from_str(cls, employee_str):
        firstname, lastname, salary = employee_str.split('-')
        return cls(firstname, lastname, salary)

    @staticmethod
    def is_workday(date):
        if date.weekday() == 3 or date.weekday() == 4:
            return False
        return True

    def __repr__(self) -> str:
        return f'Employee("{self.firstname}", "{self.lastname}", {self.salary})'

    def __str__(self) -> str:
        return f'{self.fullname()} - {self.email}'


class Developer(Employee):
    salary_raise = 1.10

    def __init__(self, firstname, lastname, salary, programming_lang) -> None:
        super().__init__(firstname, lastname, salary)
        self.programming_lang = programming_lang
