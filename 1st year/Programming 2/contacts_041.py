#!/usr/bin/env python3

import sys

def load_contacts(filename):
    contacts={}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            name, phone = parts
            contacts[name] = phone
        return contacts

def main():
    contacts_file = sys.argv[1]
    contacts = load_contacts(contacts_file)

    for line in sys.stdin:
        name = line.strip()
        if name in contacts:
            print(f'Name: {name}\nPhone: {contacts[name]}')
        else:
            print(f'Name: {name}\nNo such contact')

if __name__ == "__main__":
    main()

