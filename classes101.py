# Ethan Lawrnce
# April 29 2025
# Python Classes

# Part 1
print()
class BankAcount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.bal = balance
    def deposit(self, amount):
        print(f'${amount} has been added to the account.')
        self.bal += amount
        print(f'The new balance of {self.owner}\'s acount is ${self.bal}.')
    def withdraw(self, amount):
        if self.bal - amount > 0:
            print(f'${amount} has been removed from the account.')
            self.bal -= amount
            print(f'The new balance of {self.owner}\'s acount is ${self.bal}.')
        else:
            print('Account does not have enough funds to withdraw.')
    # End of BankAccount
bank_accounts = {
    'Mike' : BankAcount('Mike', 100),
    'Billy' : BankAcount('billy', 200),
    'Sandra' : BankAcount('Sandra', 300)
}
for account in bank_accounts:
    bank_accounts[account].withdraw(200)
    bank_accounts[account].deposit(19)
    print()
print()
print()
print()

# Part 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f'The book "{self.title}", is by {self.author}'
    def is_written_by(self):
        return self.author.lower()

books = [
    Book('Green Eggs and Ham', 'Dr Suess'),
    Book('The Toll', 'Neal Shusterman'),
]

for book in books:
    print(book.get_info())
    print(book.is_written_by())
    print()
print()
print()
print()
# Part 3

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def update_grade(self, new_grade):
        self.grade = new_grade
        return f'{self.name}, now has a {self.grade}'
    def display_info(self):
        return f'{self.name}, has a {self.grade}'

students = [
    Student('Jimmy', 100),
    Student('Johnny', 90),
    Student('Jimmy John', 80)
]

for student in students:
    print(student.display_info())
    print(student.update_grade(student.grade - 5))
    print()