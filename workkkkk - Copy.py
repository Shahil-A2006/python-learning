# Train Ticket Booking System

trains = {
    1: {"train_no": "101", "destination": "Delhi", "rate": 500},
    2: {"train_no": "102", "destination": "Mumbai", "rate": 700},
    3: {"train_no": "103", "destination": "Chennai", "rate": 600},
    4: {"train_no": "104", "destination": "Bangalore", "rate": 550},
    5: {"train_no": "105", "destination": "Kochi", "rate": 400}
}

print("\n===== TRAIN TICKET BOOKING SYSTEM =====")

name = input("Enter Passenger Name: ")
age = int(input("Enter Age: "))

print("\nAvailable Trains")
print("-" * 50)
print("No\tTrain No\tDestination\tRate")
print("-" * 50)

for key, value in trains.items():
    print(f"{key}\t{value['train_no']}\t\t{value['destination']}\t\t₹{value['rate']}")

choice = int(input("\nSelect Train (1-5): "))

if choice in trains:
    tickets = int(input("Enter Number of Tickets: "))

    selected = trains[choice]
    total = selected["rate"] * tickets

    print("\n===== BOOKING DETAILS =====")
    print("Passenger Name :", name)
    print("Age            :", age)
    print("Train Number   :", selected["train_no"])
    print("Destination    :", selected["destination"])
    print("Ticket Rate    : ₹", selected["rate"])
    print("No of Tickets  :", tickets)
    print("Total Amount   : ₹", total)

    confirm = input("\nConfirm Booking (yes/no): ")

    if confirm.lower() == "yes":
        print("\n✅ Ticket Booked Successfully!")
        print("Thank you for choosing our railway service.")
    else:
        print("\n❌ Booking Cancelled.")
else:
    print("\nInvalid Train Selection!")