
import csv

class Employee:

    def __init__(self):
        self.file = "employee.csv"

    def add(self):
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        dept = input("Enter Department: ")

        with open(self.file, "a", newline="") as f:
            data = csv.writer(f)
            data.writerow([id, name, salary, dept])

        print("Record added successfully!")

    def display(self):
        try:
            with open(self.file, "r") as f:
                data = csv.reader(f)

                print("\nEmployee Details:")
                for row in data:
                    print("ID:", row[0], "Name:", row[1],
                          "Salary:", row[2], "Department:", row[3])

        except FileNotFoundError:
            print("No records available.")

    def search(self):
        id = input("Enter ID to search: ")
        found = False

        try:
            with open(self.file, "r") as f:
                data = csv.reader(f)

                for row in data:
                    if row[0] == id:
                        print("Record found:", row)
                        found = True

            if found == False:
                print("Record not found.")

        except FileNotFoundError:
            print("File does not exist.")

    def modify(self):
        id = input("Enter ID to modify: ")
        records = []
        found = False

        try:
            with open(self.file, "r") as f:
                data = csv.reader(f)

                for row in data:
                    if row[0] == id:
                        row[1] = input("Enter new Name: ")
                        row[2] = input("Enter new Salary: ")
                        row[3] = input("Enter new Department: ")
                        found = True

                    records.append(row)

            with open(self.file, "w", newline="") as f:
                data = csv.writer(f)
                data.writerows(records)

            if found:
                print("Record updated successfully!")
            else:
                print("Employee ID not found.")

        except FileNotFoundError:
            print("File does not exist.")

    def remove(self):
        id = input("Enter ID to remove: ")
        records = []
        found = False

        try:
            with open(self.file, "r") as f:
                data = csv.reader(f)

                for row in data:
                    if row[0] == id:
                        found = True
                    else:
                        records.append(row)

            with open(self.file, "w", newline="") as f:
                data = csv.writer(f)
                data.writerows(records)

            if found:
                print("Record deleted successfully!")
            else:
                print("Employee ID not found.")

        except FileNotFoundError:
            print("File does not exist.")


emp = Employee()

while True:
    print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Modify Employee")
    print("5. Remove Employee")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        emp.add()
    elif ch == "2":
        emp.display()
    elif ch == "3":
        emp.search()
    elif ch == "4":
        emp.modify()
    elif ch == "5":
        emp.remove()
    elif ch == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
