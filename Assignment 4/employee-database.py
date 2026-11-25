
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="siddhi@17111975",
    database="company"
)

cur = con.cursor()

while True:
    print("\n--- Employee Menu ---")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        sql = "INSERT INTO employee VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (id, name, dept, salary))
        con.commit()

        print("Employee added successfully.")

    elif ch == "2":
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    elif ch == "3":
        id = int(input("Enter Employee ID: "))
        salary = float(input("Enter new Salary: "))

        sql = "UPDATE employee SET salary=%s WHERE id=%s"
        cur.execute(sql, (salary, id))
        con.commit()

        print("Employee updated successfully.")

    elif ch == "4":
        id = int(input("Enter Employee ID: "))

        sql = "DELETE FROM employee WHERE id=%s"
        cur.execute(sql, (id,))
        con.commit()

        print("Employee deleted successfully.")

    elif ch == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

cur.close()
con.close()