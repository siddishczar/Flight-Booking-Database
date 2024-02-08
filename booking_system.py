import psycopg2
from psycopg2 import sql

class BookingSystem:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, 
                user=self.user, 
                password=self.password, 
                host=self.host, 
                port=self.port
            )
            print("Connected to database successfully.")
        except psycopg2.Error as e:
            print("Error connecting to database:", e)

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Disconnected from database.")

    def get_booking_info(self, person_ref):
        try:
            cursor = self.conn.cursor()
            query = sql.SQL("""
                SELECT c.name, b.origin, b.destination, b.airline, b.class 
                FROM customer c 
                JOIN booking b ON c.person_ref = b.person_ref
                WHERE b.person_ref = %s
            """)
            cursor.execute(query, (person_ref,))
            bookings = cursor.fetchall()
            cursor.close()
            return bookings
        except psycopg2.Error as e:
            print("Error fetching booking information:", e)
            return []

    def make_transaction(self, amount):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE account 
                SET total = total + %s
            """, (amount,))
            self.conn.commit()
            cursor.close()
            print("Transaction completed successfully.")
        except psycopg2.Error as e:
            self.conn.rollback()
            print("Error making transaction:", e)