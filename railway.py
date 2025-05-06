total_seats = 5
available_seats = total_seats
booked_tickets = {}

def show_menu():
    print("\n--- Railway Booking System ---")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Booked Tickets")
    print("4. Train Status")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if available_seats > 0:
            name = input("Enter passenger name: ")
            seat_no = total_seats - available_seats + 1
            booked_tickets[seat_no] = name
            available_seats -= 1
            print(f"✅ Ticket booked! Seat No: {seat_no}, Name: {name}")
        else:
            print("❌ No seats available!")

    elif choice == "2":
        try:
            seat_no = int(input("Enter seat number to cancel: "))
            if seat_no in booked_tickets:
                print(f"✅ Ticket canceled for {booked_tickets[seat_no]}")
                del booked_tickets[seat_no]
                available_seats += 1
            else:
                print("❌ Invalid seat number.")
        except ValueError:
            print("❌ Please enter a valid seat number.")

    elif choice == "3":
        if booked_tickets:
            print("\n📋 Booked Tickets:")
            for seat, name in booked_tickets.items():
                print(f"Seat {seat}: {name}")
        else:
            print("📭 No tickets booked yet.")

    elif choice == "4":
        print(f"\n🚆 Train Status:")
        print(f"Total Seats: {total_seats}")
        print(f"Available Seats: {available_seats}")

    elif choice == "5":
        print("👋 Thank you for using the system. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1 to 5.")