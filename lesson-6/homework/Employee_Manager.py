import os

def initialize_file():
    if not os.path.exists('employees.txt'):
        with open('employees.txt','w') as file:
            pass

def view_all():
    with open('employees.txt','r') as file:
        employees=file.readlines()
        if employees:
            for record in employees:
                print(record.strip())
        else:
            print('No employee records found.')
def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    new_record = f"{employee_id}, {name}, {position}, {salary}\n"
    with open('employees.txt','a') as file:
        file.write(new_record)
    print('Employee record sucessfully added')

def search_employee():
    search_id=input("Enter Employee ID to search: ")
    found=False
    with open('employee.txt','r') as file:
        employees=file.readlines()
        for record in employees:
            if record.startswith(search_id):
                print('Employee ID is found', record.strip())
                found=True
        if not found:
            print('Employee ID is not found.')

def update_employee():
    update_id = input("Enter Employee ID to update: ")
    updated = False
    with open('employees.txt', 'r') as file:
        employees = file.readlines()
    
    with open('employees.txt', 'w') as file:
        for record in employees:
            employee_data = record.strip().split(', ')
            if employee_data[0] == update_id:
                name = input(f"Enter new Name (current: {employee_data[1]}): ")
                position = input(f"Enter new Position (current: {employee_data[2]}): ")
                salary = input(f"Enter new Salary (current: {employee_data[3]}): ")
                updated_record = f"{update_id}, {name}, {position}, {salary}\n"
                file.write(updated_record)
                print("Employee record updated successfully.")
                updated = True
            else:
                file.write(record)
    
    if not updated:
        print("Employee with this ID not found.")
def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")
    deleted = False
    with open('employees.txt', 'r') as file:
        employees = file.readlines()

    with open('employees.txt', 'w') as file:
        for record in employees:
            if not record.startswith(delete_id):
                file.write(record)
            else:
                print(f"Employee record with ID {delete_id} deleted successfully.")
                deleted = True

    if not deleted:
        print("Employee with this ID not found.")
def main():
    initialize_file()
    
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()