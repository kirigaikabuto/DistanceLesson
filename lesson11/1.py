from main import save_csv_to_json,get_data_from_json

#save_csv_to_json("table.csv","table.json")
data = get_data_from_json("main.json")
print(data[0])