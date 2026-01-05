class Flight:

    def __init__(self, code, seats, price):
        self.code = code
        self.seats = seats
        self.price = price

class FlightBookingSystem:
    def __init__(self):
        self.flights = {}
        self.ticket_id = 1

    def add_flight(self, code, seats, price):
        self.flights[code] = Flight(code, seats, price)

    def view_flights(self):
        for f in self.flights.values():
            print(f"{f.code} | Seats Left: {f.seats} | Price: ${f.price}")

    def book_seat(self, code):
        if code in self.flights and self.flights[code].seats > 0:
            self.flights[code].seats -= 1
            print("✅ Seat booked!")
            return self.flights[code].price
        else:
            print("❌ Not available!")
            return None
        
    def pay(self, amount):
        print(f"💳 Payment of ${amount} successful!")

    def generate_ticket(self, flight_code, amount):
        print("\n🧾==== Ticket Receipt ====")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Flight Code: {flight_code}")
        print(f"Amount Paid: ${amount}")
        print("Status: Confirmed")
        print("========================")
        self.ticket_id+=1

system = FlightBookingSystem()

while True:
    print("\n✈️ Flight Booking System")
    print("1️⃣ Add Flight")
    print("2️⃣ View Flights")
    print("3️⃣ Book & Pay")
    print("4️⃣ Exit")

    ch = input("Select option: ")

    if ch == "1":
        code = input("Enter flight code: ")
        seats = int(input("Enter total seats: "))
        price = int(input("Enter ticket price: "))
        system.add_flight(code,seats,price)
    elif ch == "2":
        system.view_flights()
    elif ch == "3":
        code = input("Enter flight code: ")
        price = system.book_seat(code)
        
        if price:
            confirm = input(f"Pay ${price}? (y/n): ")
            if confirm.lower() == "y":
                system.pay(price)
                system.generate_ticket(code,price)
            else:
                print("❌ Payment cancelled!")
    elif ch == "4":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid option!")