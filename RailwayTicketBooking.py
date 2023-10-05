import random

class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def checkpassword(self, password):
        return self.password == password

class Train():
    def __init__(self, train_num, train_name, source, avl_seats, destination):
        self.train_num = train_num
        self.train_name = train_name
        self.source = source
        self.avl_seats = avl_seats
        self.destination = destination
        
    def display_info(self):
        print("---------------")
        print(f"train_num: {self.train_num}")
        print(f"train_name: {self.train_name}")
        print(f"train_source: {self.source}")
        print(f"train_avl seats: {self.avl_seats}")
        print(f"train_destination: {self.destination}") 
        print("-----------------")
     
    def book_tickets(self, num_tickets):
        if num_tickets > self.avl_seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.avl_seats -= num_tickets
            return pnr_list       

class Passenger():
    def __init__(self, passenger_name, passenger_age, passenger_gender, passenger_mobile_number):
        self.passenger_name = passenger_name
        self.passenger_age = passenger_age
        self.passenger_gender = passenger_gender
        self.passenger_mobile_number = passenger_mobile_number
        
    def display_info(self):
        print(f"passenger_name: {self.passenger_name}")
        print(f"passenger_age: {self.passenger_age}")
        print(f"passenger_gender: {self.passenger_gender}")
        print(f"passenger_mobile_number: {self.passenger_mobile_number}")       

class Ticket:
    def __init__(self, train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
        
    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR: {self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()  

accounts = []
loginaccount = None

while True:
    print("-----------------")
    print("\nWelcome to IRCTC. Please select the option to be processed:\n")
    print("-----------------")
    print("1. Create account\n2. Login\n3.help")
    option = input("Enter the option to be processed: ")
    if not option:
        raise ValueError("Option cannot be empty")
    option = int(option)
    if option == 1:
        Firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        c_number = input("Enter your contact number: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if not (Firstname and lastname and c_number and username and password):
            raise ValueError("All fields must be filled")
        if len(c_number) != 10 or not c_number.isdigit():
            raise ValueError("Invalid Phone Number")
        accounts.append(Account(username, password))
        print("Account was created successfully. Please login with your credentials:")
    elif option == 2:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if not (username and password):
            raise ValueError("Username and password cannot be empty")
        for account in accounts:
            if account.username == username and account.checkpassword(password):
                loginaccount = account
                print(f"{username} has logged in successfully")
                break
        if loginaccount is None:
            print("Invalid username or password")
        else:
            print("Train bookings:")
        break
    elif option == 3:
        print("Please contact the helpline number \"1800111321\" ")
        break
    else:
        print("Invalid details")

#if loginaccount is not None:
    trains = [
        Train(12739, "GARIB RATH", "vskp", 50, "sc"),
        Train(20833, "VANDE BHARATH", "vskp", 30, "sc"),
        Train(12841, "COROMANDEL EXPRESS", "vskp", 130, "mas")
    ]

for train in trains:
    train.display_info()

while True:
    try:
        train_num = int(input("Enter train Number: "))
        num_tickets = int(input("Enter Number of Tickets: "))
        if num_tickets <= 0:
            raise ValueError("Number of tickets should be greater than 0")
        
        selected_train = None
        for train in trains:
            if train.train_num == train_num:
                selected_train = train
                if num_tickets > train.avl_seats:
                    raise ValueError("Selected more tickets than available seats")
                break
        if selected_train is None:
            raise ValueError("Invalid Train Number.")
        break
    except ValueError as e:
        print(f"Invalid Input: {e}")

passengers = []
for i in range(num_tickets):
    print(f"\nEnter the details for passenger {i + 1}: ")
    while True:
        try:
            passenger_name = input("Passenger name: ")
            if not passenger_name:
                raise ValueError("Invalid Name")
            passenger_age = int(input("Passenger age: "))
            if passenger_age <= 0 or passenger_age > 120:
                raise ValueError("Invalid Age")
            passenger_gender = input("Gender: ")
            passenger_number = input("Mobile number: ")
            if not passenger_number or len(passenger_number) != 10 or not passenger_number.isdigit():
                raise ValueError("Invalid Phone Number")
            passenger = Passenger(passenger_name, passenger_age, passenger_gender, passenger_number)
            passengers.append(passenger)
            break
        except ValueError as e:
            print(f"Invalid Input: {e}")

pnr_list = selected_train.book_tickets(num_tickets)
if pnr_list is None:
    print("Tickets not available.")
else:
    print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")
    for i in range(num_tickets):
        ticket = Ticket(selected_train, selected_train.source, selected_train.destination, [passengers[i]], pnr_list[i])
        ticket.display_info()
        print("                               ")
        print("-----------Have a safe journey---------")
        print("                                   ")
        print("Thank you for choosing Indian Railways as your travel partner")
        print("                                   ")