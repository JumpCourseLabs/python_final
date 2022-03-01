from connect import db

"""
Checks for existing employee in the database by doing a rowcount against the supplied ID
"""


def check_employee(id):
    # create SQL Statement to do the check
    sql = "select * from employees where employee_id=%s"

    # buffering the cursor position so that rowcount works
    c = db.cursor(buffered=True)
    data = (id,)

    # make the search
    c.execute(sql, data)

    # Now we'll count the rows to make sure that there is only one. If not, the employee doesn't exist

    row = c.rowcount

    if row == 1:
        return True
    else:
        return False


# Sanity Check to make sure that the function does as intended
# print(check_employee(1))
