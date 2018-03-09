#! python 3

""" Address Book
    Will store in txt file for now, but should be a database
"""
import pickle as pk

addressbook = {}

class Contact(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = ""
        self.phone = ""
        self.street_address = ""
        self.town = ""
        self.state = ""
        self.zipcode = ""

    def add_email(self):
        self.email = input("Enter email address: ")

    def add_phone(self):
        self.phone = input("Enter phone number: ")

    def add_address(self):
        self.street_address = input("Enter street address: ")
        self.town = input("Enter city or town: ")
        self.state = input("Enter state: ")
        self.zipcode = input("Enter zip code: ")


run = True
valid_answers = ["a", "A", "e", "E", "q", "Q", "s", "S"]
while run:
    answer = input("(A)dd new contact, (S)earch for contact, (E)dit contact, or (Q)uit? ")
    if answer == "Q" or answer == "q":
        run = False
    
    elif answer == "A" or answer == 'a':
        firstname = input("First name: ")
        lastname = input("Last name: ")
        fullname = firstname + lastname
        contact = Contact(firstname, lastname)
        contact.add_address
        contact.add_email
        contact.add_phone
        addressbook[fullname] = contact
        print(addressbook)

    elif answer == "S" or answer == 's':
        pass

    elif answer == "E" or answer == "e":
        pass

    if answer not in valid_answers:
        print("Invalid input.")
        

#print(type(Noon))
#Noon.add_email()
#Noon.add_phone()
print()
print(contact.first_name, contact.last_name)
print(fullname)
print(addressbook)
print("Email:", contact.email)
print("State:", contact.state)