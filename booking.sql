-- creating database
create database booking_database;
-- creating booking table
create table booking(person_ref varchar(5), 
origin varchar(15), destination varchar(15),
airline varchar(15), class varchar(10));
-- creating customer table
create table customer(name varchar(25), phone varchar(25), person_ref varchar(5));
-- create staff table
create table staff(name varchar(25), badge varchar(5), phone varchar(25), role varchar(20));
-- basic, keeps the total amount of money the airline has (for transactions)
create table account(total int);
-- inserting into customer
INSERT INTO customer (name, phone, person_ref) VALUES
('John Doe', '123-456-7890', 'ABC12'),
('Jane Smith', '987-654-3210', 'DEF45'),
('Alice Johnson', '555-555-5555', 'GHI78'),
('Michael Brown', '111-222-3333', 'JKL01'),
('Emily Davis', '444-555-6666', 'MNO34'),
('Robert Wilson', '777-888-9999', 'PQR67'),
('Olivia Martinez', '333-222-1111', 'STU90'),
('William Anderson', '999-888-7777', 'VWX23'),
('Sophia Thomas', '666-777-8888', 'YZA56'),
('Daniel Hernandez', '222-333-4444', 'BCD89');
-- inserting into booking. Here, customer.person_ref=booking.person_ref for future join functions.
INSERT INTO booking (person_ref, origin, destination, airline, class) VALUES
('ABC12', 'New York', 'Los Angeles', 'Delta', 'Economy'),
('DEF45', 'London', 'Paris', 'British Airways', 'Business'),
('GHI78', 'Tokyo', 'Sydney', 'ANA', 'First'),
('JKL01', 'Chicago', 'Miami', 'American Airlines', 'Economy'),
('MNO34', 'Paris', 'Rome', 'Air France', 'Premium Economy'),
('PQR67', 'Los Angeles', 'Tokyo', 'JAL', 'Business'),
('STU90', 'Sydney', 'Singapore', 'Singapore Airlines', 'First'),
('VWX23', 'Dubai', 'London', 'Emirates', 'Business'),
('YZA56', 'Rome', 'Barcelona', 'Iberia', 'Economy'),
('BCD89', 'Hong Kong', 'Singapore', 'Cathay Pacific', 'First');
-- inserting into staff
INSERT INTO staff (name, badge, phone, role) VALUES
('David Williams', 'STF01', '555-111-1111', 'Manager'),
('Jennifer Johnson', 'STF02', '555-222-2222', 'Travel Agent'),
('Christopher Brown', 'STF03', '555-333-3333', 'Travel Agent');
