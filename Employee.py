class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        print(f"Employee Name: {self.name}")

    def get_salary(self):
        print(f"Employee Salary: {self.salary}")

        from Assignment6 import Employee
        emp = Employee("Alice", 50000)
        emp.get_name()
        emp.get_salary()