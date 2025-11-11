#q1

#!/usr/bin/env python3

class Horse(object):
    def __init__(self, rank = 100, price = 1000):
        self.rank = rank
        self.price = price
        self.horse_prices = {self.rank : self.price}

    def calculate_rating(self):

        for i in range(99,0, -1):
            self.horse_prices[i] = int(self.horse_prices[i+1] * 1.1)


    def display(self, rank):
        if rank in self.horse_prices:
            print(self.horse_prices[rank])

        else:
            print(f"A horse with rank {rank} was not found!")


my_horse = Horse()
my_horse.calculate_rating()
my_horse.display(100)
my_horse.display(99)
my_horse.display(98)
my_horse.display(50)
my_horse.display(1)
my_horse.display(-1)
my_horse.display(101)
my_horse.display(0)

#q2

#!/usr/bin/env python3

def number_squared(number_list):
    squared_list = []
    for item in number_list:
        squared_list.append(item * item)

    return squared_list

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_squared(number_list))

#q3

#!/usr/bin/env python3

def reversed_uppercase(list_of_strings):
    list_of_strings_upper_reversed = []
    for i in list_of_strings:
        temp_string = i.upper()
        temp_string_reversed = temp_string[::-1]
        list_of_strings_upper_reversed.append(temp_string_reversed)

    return list_of_strings_upper_reversed

list_of_strings = ["hey", "test", "this code is so cool"]
print(reversed_uppercase(list_of_strings))

#q4-6

#!usr/bin/env python3

class BankAccount(object):
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.overdraft = 0
        self.account_type = "Bank Account"
        self.interest_rate = 0.00

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have enough money!")

    def get_balance(self):
        return self.balance

    def apply_interest(self, interest_rate):
        self.balance += self.balance * self.interest_rate

    def get_account_type(self):
        return self.account_type

class SavingsAccount(BankAccount):
    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name, balance)
        self.account_type = "Savings Account"
        self.interest_rate = 0.02


class CurrentAccount(BankAccount):
    def __init__(self, first_name, last_name, balance):
        super().__init__(first_name, last_name, balance)
        self.overdraft = 300
        self.account_type = "Current Account"
        self.interest_rate = 0.01


    def withdraw(self, amount):
        if self.balance + self.overdraft >= amount:
            self.balance -= amount
        else:
            print("You don't have enough money!")


account = BankAccount("Joe", "Bloggs", 0)
savings_account = SavingsAccount("Peter", "Jones", 0)
current_account = CurrentAccount("Jane", "Doe", 0)

print(account.get_account_type())
print(savings_account.get_account_type())

savings_account.apply_interest(.02)
current_account.apply_interest(.01)

savings_account.deposit(100)
current_account.deposit(500)

print(savings_account.get_balance())
print(current_account.get_balance())