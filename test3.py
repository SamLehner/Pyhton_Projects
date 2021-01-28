
# Creating the parent class called User
class User:
    name = 'No Name Provided'
    email = ''
    password = '1234abcd'
    account_number = 0


# Adding child classes called Employee and Customer and adding specific info for both
class Employee(User):
    base_pay = 15.00
    department = 'General'

class Customer(User):
    mailing_address = ''
    mailing_list = True
    
