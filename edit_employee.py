from connect import db
import check_employee

"""
EDIT EMPLOYEE
takes in employee_id and allows for editing of information
change_salary - Increases Salary (Only active function currently, and only supports increase)
PLANNED:
edit_name - Adjust employees first/last name
edit_department Adjust employees department
"""


def change_salary():
    id = input("Enter Employee's Id")

    if check_employee(id) == False:
        print(f"Employee {id} does not exist\nTry Again\n")
        # menu() TODO
    else:
        increase = input("Enter increase in Salary")

        # get current salary
        sql = "select salary from employees where employee_id=%s"
        data = (id,)
        db.cursor().execute(sql, data)  # attempting refactor of sql query statement
        # c = db.cursor()
        # c.execute(sql, data)

        # Fetching Salary of Employee with given Id, and applying the raise
        current_salary = db.cursor().fetchone()
        new_salary = current_salary[0] + increase

        # query to update salary with adjusted salary
        sql = "update employees set salary=%s where employee_id=%s"
        db.cursor().execute(sql, data)

        # Commit changes
        db.commit()

        # Output to terminal
        print(f"Employee {id} Modified")
        # menu() TODO
