#!/usr/env/usr python3

import sys

def load_contacts(filename):
    contacts={}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            name, phone, email = parts
            contacts[name] = phone, email
        return contacts

def main():
    contacts_file = sys.argv[1]
    contacts = load_contacts(contacts_file)

    for line in sys.stdin:
        name = line.strip()
        if name in contacts:
            print(f'Name: {name}\nPhone: {contacts[name][0]}\nEmail: {contacts[name][1]}')
        else:
            print(f'Name: {name}\nNo such contact')

if __name__ == "__main__":
    main()