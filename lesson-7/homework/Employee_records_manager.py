import os

class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.id=employee_id
        self.name=name
        self.position=position
        self.salary=salary

    def __str__(self):
        return f"Employee_ID:{self.id}, \nName:{self.name} \nPosition:{self.position} \nSalary:{self.salary}"
    
class EmployeeManager:
    def __init__(self):
        self.employee=[]

    def add_employee(self,employee_id,name,position,salary):
        new_employee=Employee(employee_id,name,position,salary)
        with open('employee.txt','a') as file:
            file.write(f"{new_employee.id}, {new_employee.name}, {new_employee.position}, {new_employee.salary}\n")
        print('Employee records sucessfully added')

    def view_employee(self):
        with open('employee.txt','r') as file:
            lines=file.readlines()
        if not lines:
            print("No employee exist")
        else:
            for line in lines:
                print(line.strip())

    def search_employee(self,employee_id):
        found=False
        with open('employee.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                line=line.strip().split(',')
                if line[0]==employee_id:
                    print(f"Employee found: {','.join(line)}")
                    found=True
                    break
            if not found:
                print(f'No employee with {employee_id} is found ')

    def update_employee(self, employee_id, new_name=None, new_position=None, new_salary=None ):
            updated=False
            with open('employee.txt','r') as file:
                lines=file.readlines()

            with open('employee.txt','w') as file:
                for line in lines:
                    line = line.strip().split(', ')
                    if line[0]==employee_id:
                        if new_name:
                            line[1]=new_name
                        if new_position:
                            line[2]=new_position
                        if new_salary:
                            line[3]=new_salary
                        updated=True
                        file.write(', '.join(line) + '\n')
                    else:
                        file.write(line+ '\n')

                if updated:
                    print( f"Employee with ID:{employee_id} is updated!")
                if not updated:
                    print( "Employee is not found!")
            
    def delete_employee(self,employee_id):
        found=False
        with open('employee.txt','r') as file:
            lines=file.readlines()
        with open('employee.txt','w') as file:
            for line in lines:
                if line.strip().split(', ')[0] != employee_id:
                    file.write(line)
                else:
                    found=True
        if found:
            print( f"The employee with ID:{employee_id} is successfully deleted")
        else:
            print(f"Employee with ID {employee_id} not found.")
    
def initialize_file():
    if not os.path.exists('employee.txt'):
        with open('employee.txt','w') as file:
            pass

def main():
    initialize_file()
    manager=EmployeeManager()

    while True:
        print("\nWelcome to the Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = input("Enter Employee Salary: ")
            manager.add_employee(emp_id, name, position, salary)
        elif choice == '2':
            manager.view_employee()
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            manager.search_employee(emp_id)
        elif choice == '4':
            emp_id = input("Enter Employee ID to update: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_position = input("Enter new position (leave blank to keep current): ")
            new_salary = input("Enter new salary (leave blank to keep current): ")
            manager.update_employee(emp_id, new_name, new_position, new_salary)
        elif choice == '5':
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=='__main__':
    main()