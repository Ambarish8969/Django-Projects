import pandas as pd
import json

# Load the Excel file into a Pandas DataFrame
input_excel_file = "G:\Django\input_excel_file.xlsx"
df = pd.read_excel(input_excel_file)

# Replace NaN values with "NULL" string
df = df.fillna("NULL")

# Group data by 'Customer ID'
grouped_data = df.groupby(['Customer ID', 'panel_name', 'panel_code', 'age'])

# Initialize the output data structure
output_data = []

# Iterate through grouped data
for (customer_id, panel_name, panel_code, age), group in grouped_data:
    customer_entry = {
        "Customer ID": str(customer_id),
        "age": str(age),
        "panelList": []
    }

    panel_entry = {
        "panel_name": panel_name,
        "panel_code": panel_code,
        "parameters": []
    }

    # Iterate through rows in the group
    for index, row in group.iterrows():
        parameter_entry = {
            "parameterName": row["Parameter Name"],
            "unit": row["Units"],
            "parameterCode": str(row["Parameter Code"]),
            "value": str(row["Result"]),
            "lowerRange": str(row["Low Range"]),
            "upperRange": str(row["High Range"]),
            "displayRange": f"{row['Low Range']}-{row['High Range']}"
        }

        panel_entry["parameters"].append(parameter_entry)

    customer_entry["panelList"].append(panel_entry)
    output_data.append(customer_entry)

# Convert the output data to JSON format
output_json = json.dumps(output_data, indent=4)

# Write the JSON data to the output file
with open("output_json2.json", "w") as json_file:
    json_file.write(output_json)

print("JSON transformation complete.")



# -----------------------------------------------------------------------------------------------------------

# import pandas as pd
# import json
# import numpy as np

# # Load the Excel file into a Pandas DataFrame
# input_excel_file = "G:\Django\input_excel_file.xlsx"
# df = pd.read_excel(input_excel_file)

# # Replace NaN values with "NULL" string
# df = df.fillna("NULL")

# # Group data by 'Customer ID'
# grouped_data = df.groupby('Customer ID')

# # Initialize the output data structure
# output_data = []

# # Iterate through grouped data
# for customer_id, group in grouped_data:
#     customer_entry = {
#         "Customer ID": str(customer_id),
#         "age": str(group['age'].values[0]),
#         "panelList": []
#     }

#     panel_list = []

#     # Iterate through rows in the group
#     for index, row in group.iterrows():
#         panel_entry = {
#             "panel_name": row["panel_name"],
#             "panel_code": row["panel_code"],
#             "parameters": [
#                 {
#                     "parameterName": row["Parameter Name"],
#                     "unit": "NULL" if row["Units"] == "NULL" else row["Units"],
#                     "parameterCode": str(row["Parameter Code"]),
#                     "value": str(row["Result"]),
#                     "lowerRange": str(row["Low Range"]),
#                     "upperRange": str(row["High Range"]),
#                     "displayRange": f"{row['Low Range']}-{row['High Range']}"
#                 }
#             ]
#         }
#         panel_list.append(panel_entry)

#     customer_entry["panelList"] = panel_list
#     output_data.append(customer_entry)

# # Convert the output data to JSON format
# output_json = json.dumps(output_data, indent=4)

# # Write the JSON data to the output file
# with open("output_json3.json", "w") as json_file:
#     json_file.write(output_json)

# print("JSON transformation complete.")
