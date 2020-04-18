from main import save_csv_to_json,get_data_from_json,add_object
d={}
d["EMPLOYEE_ID"]=int(input("Employee_id:"))
d["FIRST_NAME"]=input("FirstName:")
add_object("table.json",d)
