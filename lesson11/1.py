from main import save_csv_to_json,get_data_from_json,save_data_to_json

#save_csv_to_json("table.csv","table.json")
data = get_data_from_json("table.json")
# employee_id=int(input("Employee_id:"))
# first_name = input("FirstName")
d={}
d["EMPLOYEE_ID"]=int(input("Employee_id:"))
d["FIRST_NAME"]=input("FirstName:")
data.append(d)
save_data_to_json("table.json",data)



#...
# 1)в существующий массив из словарей добавить текущий словарб
# 2)сохранить весь массив в файл откуда был взят наш массив