import sys
import datetime

from connect import db
from check_employee import check_employee


def menu():
    print("Welcome to the Cognixia JUMP Employee Management System")
    print("Please Choose : ")

    print("1 : Add New Employee")
    print("2 : Edit Employee")
    print("3 : Remove Employee")
    print("4 : Display List of Employees")
    print("5 : Exit \n \n")

    # record input and redirect to correct operation

    user_choice = int(input("Enter Your Selection : "))

    match user_choice:
        case 1:
            add_employee()
        case 2:
            change_salary()
        case 3:
            remove_employee()
        case 4:
            display_employees()
        case 5:
            print("Exiting...")
            sys.exit()
        case _:
            print("Invalid Selection")


class SalaryException(Exception):
    menu()


"""
ADD EMPLOYEE MODULE
Inserts a record into the database.
"""


def add_employee():
    try:
        id = int(input("Enter Employee ID : "))
    except TypeError:
        print("Invalid ID Format - Must be numbers\n\n")
        menu()

        # check if employee ID Exists
        if check_employee(id) == True:
            print(f"Employee ID {id} already exists. \nTry Again\n\n")
            menu()

        else:
            try:
                first_name = input("Enter Employee First Name : ")
                last_name = input("Enter Employee Last Name : ")
                dept = input("Enter Employee Department : ")
                hired = input("Enter Employee Hire Date : ")
                salary = int(input("Enter Employee Salary : "))
            except TypeError:
                print("ERROR: Value is invalid\n\n")

                # let's make sure that's a real date
            try:
                datetime.datetime.strptime(hired, "%d-%m-%Y")
            except ValueError:
                print("Incorrect data format, should be MM-DD-YYYY")

                # Ok that checked out
                # Now we construct the data element
                data = (str(id), last_name, first_name, hired, str(salary), dept)

                # construct SQL statement
                sql = "insert into employees values(%s,%s,%s,%s,%s,%s)"
                query = db.cursor()

                # execute the query to add the employee
                query.execute(sql, data)

                # commit the changes to the table and output to the user
                db.commit()
                print(f"Employee {id} Successfully Added \n\n")
                menu()


"""
DELETE EMPLOYEE
Takes employee_id, and checks it against the database. If it exists, the record is deleted
"""


def remove_employee():
    try:
        id = int(input("Enter Employee ID : "))
    except TypeError:
        print("Invalid ID Format (should be numeric)")
        menu()

        # Checking if Employee with given Id
        # Exist or Not
        if check_employee(id) == False:
            print("Employee does not  exists\nTry Again\n")
            # menu() TODO

        else:

            # Query to Delete Employee from Table
            sql = "delete from employees where employee_id=%s"
            data = (str(id),)
            query = db.cursor(buffered=True)

            # Execute Query
            query.execute(sql, data)

            # commit the changes to the table
            db.commit()
            print(f"Employee {id} Removed \n \n")
            menu()


"""
EDIT EMPLOYEE
takes in employee_id and allows for editing of information
change_salary - Increases Salary (Only active function currently, and only supports increase)
PLANNED:
edit_name - Adjust employees first/last name
edit_department Adjust employees department
"""


def change_salary():
    try:
        id = int(input("Enter Employee's Id : "))
    except TypeError:
        print("Invalid ID Format (Should be numeric)")
        menu()

        if check_employee(id) == False:
            print(f"Employee {id} does not exist\nTry Again\n\n")
            # menu() TODO
        else:
            try:
                increase = int(input("Enter increase in Salary : "))
            except ValueError:
                print("That isn't a number!")
                menu()

        if increase > 20000:
            raise SalaryException("What, did you make him owner or something?")

        # get current salary
        sql = "select salary from employees where employee_id=%s"
        data = (id,)
        query = db.cursor()
        query.execute(sql, data)

        # Fetching Salary of Employee with given Id, and applying the raise
        check_salary = query.fetchone()
        old_salary = int(check_salary[0])
        new_salary = old_salary + increase

        # query to update salary with adjusted salary
        sql = "update employees set salary=%s where employee_id=%s"
        data = (str(new_salary), id)
        query.execute(sql, data)

        # Commit changes
        db.commit()

        # Output to terminal
        print(f"Employee {id} Modified\n\n")
        menu()


"""
DISPLAY EMPLOYEES -
Outputs employees list from Database to the console
"""


def display_employees():

    # query to select all rows from
    # Employee Table
    sql = "select * from employees"
    query = db.cursor()

    # Executing the SQL Query
    query.execute(sql)

    # Fetching all details of all the
    # Employees
    result = query.fetchall()

    # Turn table into an iterable list
    employee_list = [i for i in result]
    print("\n\n")
    for e in employee_list:
        print("Employee Id : ", e[0])
        print("Employee Name : ", e[1])
        print("Employee Post : ", e[2])
        print("Employee Salary : ", e[3])
        print("-----------------------------\n\n\n")

    menu()


if __name__ == "__main__":
    menu()
