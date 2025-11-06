#!/usr/bin/env python3

class BankAccount(object):
    def __init__(self, balance:float=0.0):
        self.balance = balance
        self.balanceHistory = []
        self.opening_balance = self.balance

    def deposit(self, value):
        self.balance += value
        self.balanceHistory.append((value, self.balance))

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.balanceHistory.append((-value, self.balance))

    def __str__(self):
        output = []
        if len(self.balanceHistory) < 3:
            output.append(f"Opening balance: {self.opening_balance:.2f} euros")
        else:
            opening_balance = self.balanceHistory[-3][1] - self.balanceHistory[-3][0]
            output.append(f"Opening balance: {opening_balance:.2f} euros")

        for amount, new_balance in self.balanceHistory[-3:]:
            transaction_type = "deposit" if amount > 0 else "withdrawal"
            output.append(f"{amount:.2f} {transaction_type} for a new balance of {new_balance:.2f}")

        output.append(f"Current balance: {self.balance:.2f} euros")
        return "\n".join(output)