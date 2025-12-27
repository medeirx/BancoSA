import sqlite3 as sql

connection = sql.connect("../database.db")
cursor = connection.cursor()

insert_query = '''
               INSERT INTO Students (name, age, email)
               VALUES (?, ?, ?); 
               '''
student_data = ('Jane Doe', 23, 'jane@example.com')

cursor.execute(insert_query, student_data)

# Commit the changes automatically
connection.commit()

# Write the SQL command to select all records from the Students table
# select_query = "SELECT * FROM Students;"
#
# # Execute the SQL command
# cursor.execute(select_query)
#
# # Fetch one record
# student = cursor.fetchone()
#
# print(student)

# update_query = '''
#                UPDATE Students
#                SET age = ?
#                WHERE name = ?; \
#                '''
#
# # Data for the update
# new_age = 21
# student_name = 'Jane Doe'
#
# # Execute the SQL command with the data
# cursor.execute(update_query, (new_age, student_name))
#
# # Commit the changes to save the update
# connection.commit()
#
# # Print a confirmation message
# print(f"Updated age for {student_name} to {new_age}.")

# delete_query = '''
#                DELETE \
#                FROM Students
#                WHERE name = ?; \
#                '''
#
# # Name of the student to be deleted
# student_name = 'Jane Doe'
#
# # Execute the SQL command with the data
# cursor.execute(delete_query, (student_name,))
#
# # Commit the changes to save the deletion
# connection.commit()
#
# # Print a confirmation message
# print(f"Deleted student record for {student_name}.")

def transfer_funds(from_customer, to_customer, amount):
    with sql.connect('../my_database.db') as connection:
        cursor = connection.cursor()

        try:
            # Start a transaction
            cursor.execute("BEGIN;")

            # Deduct amount from the sender
            cursor.execute(
                "UPDATE Customers SET balance = balance - ? WHERE name = ?;", (amount, from_customer))
            # Add amount to the receiver
            cursor.execute(
                "UPDATE Customers SET balance = balance + ? WHERE name = ?;", (amount, to_customer))

            # Commit the changes
            connection.commit()
            print(
                f"Transferred {amount} from {from_customer} to {to_customer}.")

        except Exception as e:
            # If an error occurs, rollback the transaction
            connection.rollback()
            print(f"Transaction failed: {e}")


# Example usage
transfer_funds('Ashutosh', 'Krishna', 80.0)