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
        "panelList": []  
    }

    panels_dict = {}

    for index, row in group.iterrows():
        panel_name = row["panel_name"]
        panel_code = row["panel_code"]
        parameter_entry = {
            "parameterName": row["Parameter Name"],
            "unit": row["Units"],
            "parameterCode": str(row["Parameter Code"]),
            "value": str(row["Result"]),
            "lowerRange": str(row["Low Range"]),
            "upperRange": str(row["High Range"]),
            "displayRange": f"{row['Low Range']}-{row['High Range']}"
        }

        if panel_name not in panels_dict:
            panels_dict[panel_name] = {
                "panel_name": panel_name,
                "panel_code": panel_code,
                "parameters": []
            }

        panels_dict[panel_name]["parameters"].append(parameter_entry)

    customer_entry["panelList"] = list(panels_dict.values())
    output_data.append(customer_entry)

output_json = json.dumps(output_data, indent=4)

with open("final_output.json", "w") as json_file:
    json_file.write(output_json)

print("JSON transformation complete.")