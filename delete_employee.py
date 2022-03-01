from connect import db
import check_employee

"""
DELETE EMPLOYEE
Takes employee_id, and checks it against the database. If it exists, the record is deleted
"""


def Remove_Employ():
    id = input("Enter Employee ID : ")

    # Checking if Employee with given Id
    # Exist or Not
    if check_employee(id) == False:
        print("Employee does not  exists\nTry Again\n")
        # menu() TODO

    else:

        # Query to Delete Employee from Table
        sql = "delete from employees where employee_id=%s"
        data = (id,)
        c = db.cursor()

        # Execute Query
        c.execute(sql, data)

        # commit the changes to the table
        db.commit()
        print(f"Employee {id} Removed")
        # menu()  TODO
