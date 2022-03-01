from check_employee import check_employee
from connect import db
import check_employee

"""
ADD EMPLOYEE MODULE
Inserts a record into the database.
"""


def Add_Employee():
    id = input("Enter Employee ID : ")

    # check if employee ID Exists
    if check_employee(id) == True:
        print(f"Employee ID {id} already exists. \nTry Again\n")
        # menu() TODO

    else:
        first_name = input("Enter Employee First Name : ")
        last_name = input("Enter Employee Last Name : ")
        dept = input("Enter Employee Department : ")
        hired = input("Enter Employee Hire Date : ")
        salary = input("Enter Employee Salary : ")

        # Now we construct the data element
        data = (id, last_name, first_name, hired, salary, dept)

        # construct SQL statement
        sql = "insert into employees values(%s,%s,%s,%s,%s)"
        c = db.cursor()

        # execute the query to add the employee
        c.execute(sql, data)

        # commit the changes to the table and output to the user
        db.commit()
        print(f"Employee {id} Successfully Added")
        # menu() TODO
