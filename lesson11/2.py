from main import add_object,get_data_from_json,save_data_to_json
data = get_data_from_json("table.json")
employee_name="Peter"
employee_indexs=[]
for i in range(len(data)):
    employee = data[i]
    if employee["FIRST_NAME"]==employee_name:
        print(employee["EMPLOYEE_ID"],employee["FIRST_NAME"],employee['LAST_NAME'])
        employee_indexs.append(i)

# for i in range(len(employee_indexs)):
#     data.pop(employee_indexs[i])
# save_data_to_json("table.json",data)
