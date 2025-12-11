from employee import employee_details
def test_employee_details():
    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 50000
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E1001\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details("alice","E1001","IT",50000) == expected_output