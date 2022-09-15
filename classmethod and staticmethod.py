import datetime

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@company.org').lower()
        Employee.num_of_emps += 1

    @property
    def full_name(self):    # a getter
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay *= Employee.raise_amt

    @classmethod
    def set_raise_amt(cls, amt):    # a setter
        cls.raise_amt = amt
    
    @classmethod
    @property
    def num_emps(cls):  # a getter
        return cls.num_of_emps
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    # use a static method when you don't access instances or the class anywhere inside the method
    # a static method doesn't use any variables associated with the class
    @staticmethod
    def isworkday(day): # static methods don't take the instance or the class as the first argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self) -> str:
        return f"""
                   first name: {self.first}
                   last name: {self.last}
                   salary: {self.pay}
                   """

my_date = datetime.date(2022, 10, 9)
print(Employee.isworkday(my_date))


