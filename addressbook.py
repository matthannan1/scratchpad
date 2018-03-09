#! python 3

""" Address Book
    Will store in txt file for now, but should be a database
"""
import pickle as pk

addressbook = {}

class Contact(object):
    def __init__(self, first_name, last_name, email, phone, street_address, town, state, zipcode, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.street_address = street_address
        self.town = town
        self.state = state
        self.zipcode = zipcode
        self.country = country


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
        email = input("Enter email address: ")
        phone = input("Enter phone number: ")
        street_address = input("Enter street address: ")
        town = input("Enter city or town: ")
        state = input("Enter state: ")
        zipcode = input("Enter zip code: ")
        country = input("Enter country: ")
        contact = Contact(firstname, lastname, email, phone, street_address, town, state, zipcode, country)
        #d['mynewkey'] = 'mynewvalue'
        addressbook[fullname] = contact
        
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
#print(contact.first_name, contact.last_name)
#print(fullname)
#print(addressbook)
#print("Email:", contact.email)
#print("State:", contact.state)
# Write to the file
f = open("addressbook.txt", 'wb')
# Dump the object to a file
pk.dump(addressbook, f)
f.close()
