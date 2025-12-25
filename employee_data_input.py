# Q): w.a.p to read employee data from the keyboard and print that data.

empid=int(input("Enter the employee Id:"))
empname=input("Enter the employee name:")
empsal=float(input("Enter the employee salary:"))
eadd=input("Enter the employee address")
# emarried=bool(input("Enter employee married?[True|False]"))
# Directly using bool(input(...)) doesn’t work correctly because any non-empty string → True.
# Correct way → check if input string equals "True" (case-insensitive)

emarried=input("Enter employee married?[True|False]")
if emarried.lower()=='true':
    emar=True
else:
    emar=False
print("Confirm Information")
print("Employee Id :",empid)
print("Employee Name:",empname)
print("Employee Salary :",empsal)
print("Employee Address:",eadd)
print("Employee Married? :",emar)

