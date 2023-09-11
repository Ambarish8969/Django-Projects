import pandas as pd
import json

input_excel_file = "G:\Django\input_excel_file.xlsx"
df = pd.read_excel(input_excel_file)

df = df.fillna("NULL")

grouped_data = df.groupby(['Customer ID', 'age'])

output_data = []

for (customer_id, age), group in grouped_data:
    customer_entry = {
        "Customer ID": str(customer_id),
        "age": str(age),
        "panels": {}  
    }

    for index, row in group.iterrows():
        panel_code = str(row["panel_code"])  
        parameter_code = str(row["Parameter Code"])  
        parameter_entry = {
            "parameterName": row["Parameter Name"],
            "unit": row["Units"],
            "value": str(row["Result"]),
            "lowerRange": str(row["Low Range"]),
            "upperRange": str(row["High Range"]),
            "displayRange": f"{row['Low Range']}-{row['High Range']}"
        }

        if panel_code not in customer_entry["panels"]:
            customer_entry["panels"][panel_code] = {  
                "panel_name": row["panel_name"],
                "parameters": {}
            }

        if parameter_code not in customer_entry["panels"][panel_code]["parameters"]:
            customer_entry["panels"][panel_code]["parameters"][parameter_code] = {}  
            customer_entry["panels"][panel_code]["parameters"][parameter_code]["parameterName"] = parameter_entry["parameterName"]
            customer_entry["panels"][panel_code]["parameters"][parameter_code]["unit"] = parameter_entry["unit"]
            customer_entry["panels"][panel_code]["parameters"][parameter_code]["value"] = parameter_entry["value"]
            customer_entry["panels"][panel_code]["parameters"][parameter_code]["lowerRange"] = parameter_entry["lowerRange"]
            customer_entry["panels"][panel_code]["parameters"][parameter_code]["upperRange"] = parameter_entry["upperRange"]
            customer_entry["panels"][panel_code]["parameters"][parameter_code]["displayRange"] = parameter_entry["displayRange"]

    output_data.append(customer_entry)

output_json = json.dumps(output_data, indent=4)

with open("try1.json", "w") as json_file:
    json_file.write(output_json)

print("JSON transformation complete.")