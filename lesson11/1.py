from main import add_object
def add_employee():
    d={}
    d["EMPLOYEE_ID"]=int(input("Employee_id:"))
    d["FIRST_NAME"]=input("FirstName:")
    add_object("table.json",d)
