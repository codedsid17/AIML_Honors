
import mysql.connector

class Employee:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="company"
        )
        self.cur = self.con.cursor()

    def create(self):
        id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        sql = "INSERT INTO employee VALUES (%s,%s,%s,%s)"
        self.cur.execute(sql, (id, name, dept, salary))
        self.con.commit()

        print("Record inserted successfully.")

    def read(self):
        self.cur.execute("SELECT * FROM employee")
        data = self.cur.fetchall()

        for row in data:
            print(row)

    def update(self):
        id = int(input("Enter Employee ID: "))
        salary = float(input("Enter new Salary: "))

        sql = "UPDATE employee SET salary=%s WHERE id=%s"
        self.cur.execute(sql, (salary, id))
        self.con.commit()

        print("Record updated successfully.")

    def delete(self):
        id = int(input("Enter Employee ID: "))

        sql = "DELETE FROM employee WHERE id=%s"
        self.cur.execute(sql, (id,))
        self.con.commit()

        print("Record deleted successfully.")


emp = Employee()

while True:
    print("\n--- Employee Menu ---")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp.create()

    elif choice == "2":
        emp.read()

    elif choice == "3":
        emp.update()

    elif choice == "4":
        emp.delete()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
