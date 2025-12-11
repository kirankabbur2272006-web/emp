def employee_details(name,emp_id,departement,salary):
   result=(
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {departement}\n"
        f"Salary: {salary}\n"
   )
   return result
if__name= "__main__"
name="allice"
emp_id="E1001"
departement="IT"     
salary=50000
print(employee_details(name, emp_id, departement, salary))