#!/usr/bin/env python3

class BankAccount(object):

    def set_attributes(bank, name, number, balance):
        bank.name = name
        bank.number = number
        bank.balance = balance


    def print_attributes(bank):
        print(f"Name: {bank.name}")
        print(f"Account number: {bank.number}")
        print(f"Balance: {bank.balance}.00")

    def deposit(bank, amount):
        bank.balance = bank.balance + amount