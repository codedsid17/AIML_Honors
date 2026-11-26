import mysql.connector
import pandas as pd

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="siddhi@17111975",
    database="company"
)

cur = con.cursor()

while True:
    print("------Employee Management------")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Change Salary")
    print("4. Remove Employee")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        eid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        query = "INSERT INTO employee VALUES (%s,%s,%s,%s)"
        cur.execute(query, (eid, name, dept, salary))
        con.commit()
        print("New employee added.")

    elif choice == "2":
        cur.execute("SELECT * FROM employee")
        records = cur.fetchall()

        columns = [col[0] for col in cur.description]
        df = pd.DataFrame(records, columns=columns)
        print("\nEmployee Details:")
        print(df)

    elif choice == "3":
        eid = int(input("Enter ID: "))
        salary = float(input("Enter updated Salary: "))

        query = "UPDATE employee SET salary=%s WHERE id=%s"
        cur.execute(query, (salary, eid))
        con.commit()

        if cur.rowcount > 0:
            print("Salary changed successfully.")
        else:
            print("Employee not found.")

    elif choice == "4":
        eid = int(input("Enter ID to remove: "))

        query = "DELETE FROM employee WHERE id=%s"
        cur.execute(query, (eid,))
        con.commit()

        if cur.rowcount > 0:
            print("Employee removed.")
        else:
            print("Employee not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Please enter a valid choice.")

cur.close()
con.close()
