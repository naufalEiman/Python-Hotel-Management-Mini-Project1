import os
import re

print("| Welcome to Pullman Hotel |\n")

# List 
customer_database = []

# File 
customer_file = "cust_database.txt"

# Load 
def load_customer_data():
    if os.path.exists(customer_file):
        with open(customer_file, "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith("Customer Name:"):
                    customer = {
                        "name": lines[i].strip().split(": ")[1],
                        "age": lines[i+1].strip().split(": ")[1],
                        "email": lines[i+2].strip().split(": ")[1],
                        "phone": lines[i+3].strip().split(": ")[1],
                        "numOfperson": lines[i+4].strip().split(": ")[1],
                    }
                    customer_database.append(customer)
                    i += 6  # Skip to the next record
                else:
                    i += 1

# Save 
def save_customer_data():
    with open(customer_file, "w") as file:
        for customer in customer_database:
            file.write(f"Customer Name: {customer['name']}\n")
            file.write(f"Age: {customer['age']}\n")
            file.write(f"Email: {customer['email']}\n")
            file.write(f"Phone Number: {customer['phone']}\n")
            file.write(f"Number of person that will be staying: {customer['numOfperson']}\n\n")

def mainmenu():
    while True:
        print("| MAIN MENU |\n")
        print("1. Staff\n")
        print("2. Exit\n")

        choice = input("Please choose your category: ")
        if choice == "1":
            staffmenu()
        elif choice == "2":
            print("Thank you for using our system.")
            break
        else:
            print("Invalid choice. Please try again.")
        cont = input("Do you want to continue to the Main menu? (Yes/No): ")
        if cont.lower() != "yes":
            print("Thank you for using our system.")
            break

def staffmenu():
    while True:
        print("\nStaff Menu\n")
        print("1. Insert Customer Data")
        print("2. Update Customer Data")
        print("3. Delete Customer Data")
        print("4. View Customer Data")
        print("5. Search Customer")
        print("6. Exit\n")
        choice = input("Please choose an operation: ")
        if choice == "1":
            staffinsert()
        elif choice == "2":
            staffupdate()
        elif choice == "3":
            staffdelete()
        elif choice == "4":
            staffview()
        elif choice == "5":
            staffsearch()
        elif choice == "6":
            print("Thank you for using our system.")
            break
        else:
            print("Invalid choice. Please try again.\n")
        cont = input("Do you want to continue to the Staff menu? (Yes/No): ")
        if cont.lower() != "yes":
            print("Thank you for using our system.")
            break

def staffview():
    print("\nCustomer Database:")
    for customer in customer_database:
        print_customer(customer)

def staffinsert():
    cust_name = input("Enter Customer Name: ")
    cust_age = input_number("Enter Customer Age: ")
    cust_email = input_email("Enter Customer Email: ")
    cust_phone = input_phone("Enter Customer Phone Number: ")
    cust_noOfperson = input_number("Enter number of person that will be staying: ")

    customer = {
        "name": cust_name,
        "age": cust_age,
        "email": cust_email,
        "phone": cust_phone,
        "numOfperson": cust_noOfperson,
    }
    
    customer_database.append(customer)
    save_customer_data()

def staffdelete():
    cust_name = input("Enter Customer Name to remove: ")
    global customer_database
    customer_database = [customer for customer in customer_database if customer["name"] != cust_name]
    save_customer_data()
    print(f"Customer '{cust_name}' has been removed.")

def staffupdate():
    cust_name = input("Enter Customer Name to update: ")
    customer = next((customer for customer in customer_database if customer["name"] == cust_name), None)
    
    if customer:
        customer["name"] = input("Enter new Customer Name: ")
        customer["age"] = input_number("Enter new Customer Age: ")
        customer["email"] = input_email("Enter new Customer Email: ")
        customer["phone"] = input_phone("Enter new Customer Phone Number: ")
        customer["numOfperson"] = input_number("Enter new number of person that will be staying: ")
        save_customer_data()
        print(f"Customer '{cust_name}' has been updated.")
    else:
        print(f"Customer '{cust_name}' not found.")

def staffsearch():
    cust_name = input("Enter customer name to search: ")
    customer = next((customer for customer in customer_database if customer["name"] == cust_name), None)
    
    if customer:
        print("\nCustomer Information:")
        print_customer(customer)
    else:
        print("No registered customer found for the given name.")

def print_customer(customer):
    print(f"Customer Name: {customer['name']}")
    print(f"Age: {customer['age']}")
    print(f"Email: {customer['email']}")
    print(f"Phone Number: {customer['phone']}")
    print(f"Number of person that will be staying: {customer['numOfperson']}")
    print()

# Validation
def input_email(prompt):
    while True:
        email = input(prompt)
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Incorrect email format. Please enter a valid email.")

def input_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        else:
            print("Incorrect. Please enter a number.")

def input_phone(prompt):
    while True:
        phone = input(prompt)
        if phone.isdigit() and (len(phone) == 10 or len(phone) == 11):
            return phone
        else:
            print("Invalid phone number. Please enter a 10 or 11-digit phone number.")

# Load the data when the program starts
load_customer_data()

# Start the main menu
mainmenu()


