from booking_system import BookingSystem

def main():
    # Initialize BookingSystem object
    booking_system = BookingSystem(
        dbname="booking_database",
        user="postgres",
        password="sidd!2004"
    )

    # Connect to the database
    booking_system.connect()

    # Main loop
    while True:
        print("\nChoose an option:")
        print("1. Get booking information")
        print("2. Make a transaction")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            # Get booking information for a person
            person_ref = input("Enter person_ref: ")
            bookings = booking_system.get_booking_info(person_ref)
            if bookings:
                print(f"Booking information for person_ref {person_ref}:")
                for booking in bookings:
                    print(booking)
            else:
                print(f"No booking information found for person_ref {person_ref}")

        elif choice == "2":
            # Make a transaction
            amount = int(input("Enter transaction amount: "))
            booking_system.make_transaction(amount)

        elif choice == "3":
            # Exit the program
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    # Disconnect from the database
    booking_system.disconnect()
    print("Exiting program.")

if __name__ == "__main__":
    main()