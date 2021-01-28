# Parent Class
class Account:
    name = "Sam"
    email = "sam@gmail.com"
    password = "ABC123"

    def getAccountInfo(self):
        login_name = input("Enter your name: ")
        login_email = input("Enter your email: ")
        login_password = input("Enter your password: ")
        if (login_email == self.email and login_password == self.password):
            print("Welcome back, {}!".format(login_name))
        else:
            print("The password or email is incorrect.")


# Child Class
class Manager(Account):
    salary = 87,000
    store = 48
    pin = "4512"

    # This is the same method but we are using the manager pin instead of password
    def getAccountInfo(self):
        login_name = input("Enter your name: ")
        login_email = input("Enter your email: ")
        login_pin = input("Enter your pin: ")
        if (login_email == self.email and login_pin == self.pin):
            print("Welcome back, {}!".format(login_name))
        else:
            print("The pin or email is incorrect.")



# Another Child class of Account
class Employee(Account):
    base_pay = 12.00
    department = "General"
    emp_number = "1567"

    # This is the same method as before but we are using the employee number instead.
    def getAccountInfo(self):
        login_name = input("Enter your name: ")
        login_email = input("Enter your email: ")
        login_emp = input("Enter your employee number: ")
        if (login_email == self.email and login_emp == self.emp_number):
            print("Welcome back, {}!".format(login_name))
        else:
            print("The employee number or email is incorrect.")



# This code invokes the methods inside each class
user = Account()
user.getAccountInfo()

manager = Manager()
manager.getAccountInfo()

employee = Employee()
employee.getAccountInfo()
