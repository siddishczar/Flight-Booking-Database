# Flight-Booking-Database
This project mirrors a database of a simple booking company using postgres as the database management system and
psyopcg2 to handle basic security topics. While an actual database would likely be very large, this database
is trying to emulate that of a small travel agency, and of that a customer interface with basic security measures.

The database has four tables: booking, customer, staff, and account. The 'booking' table manages the different
bookings brought through the company. The 'staff' table manages the staff that work at the company. The 'customer'
table manages the customers that work at the company, whilst the 'amount' table has the total amount of money the
travel agency has.

Amount has one entry (and one column, that being the total value of the agency). Booking contains the booking
number(person_ref), origin, destination, airline, and class. Customer contains the person, their reference number
(also person_ref), and their phone number (phone). Staff contains the staffs' names, their badge (ID) numbers,
their phone numbers, and role in the agency. No roles are granted here (since the python interface would manage
access for customers, and staff would theoretically have access to the database itself).

To load the database, open postgres and run the command:
         create database booking_database;

Now, load the sql file into the database by running:
         \i /filepath/booking.sql

This should load all of the tables and insert statements into the code.
If it does not, feel free to load them in manually.

Now, open the booking_system.py and main.py. booking_system.py contains the connection definitions and the
function definitions for getting bookings and making transactions. Main.py contains the main function. In main.py,
set the passowrd (line 7) equal to your own password in postgres.

Now, the project should be compiled and able to run. To run the project, run main.py and follow the insturctions.
For option 1, enter in your booking number and you will get the passenger, origin, destintion, airline, and
class they are flying. For option 2, you can add money (sort of like a transaction), that will update the value
in the amount table. Option 3 terminates the program.
