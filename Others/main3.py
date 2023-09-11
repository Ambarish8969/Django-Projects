import json
import pandas as pd
import numpy as np

def excel_to_nested_json(excel_file, sheet_name):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet_name)

        # Replace NaN values with 'NULL'
        df.replace(np.nan, 'NULL', inplace=True)

        # Initialize an empty list to store the final JSON structure
        json_data = []

        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            customer_data = {
                "Customer ID": row["Customer ID"],
                "age": row["age"],
                "panelList": []
            }

            # Process panel data
            panel_dict = {
                "panel_name": row["panel_name"],
                "panel_code": row["panel_code"],
                "parameters": []
            }

            parameter_dict = {
                "parameterName": row["Parameter Name"],
                "unit": row["Units"],
                "parameterCode": row["Parameter Code"],
                "value": row["Result"],
                "lowerRange": row["Low Range"],
                "upperRange": row["High Range"],
                "displayRange": f"{row['Low Range']}-{row['High Range']}"
            }
            panel_dict["parameters"].append(parameter_dict)

            customer_data["panelList"].append(panel_dict)
            json_data.append(customer_data)

        return json_data
    except Exception as e:
        return str(e)

# Provide the path to your Excel file and the sheet name
excel_file_path = 'G:\Django\input_excel_file.xlsx'
sheet_name = 'data'

# Call the function to convert Excel data to nested JSON
json_data = excel_to_nested_json(excel_file_path, sheet_name)

# Write JSON data to a file
with open('output3.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print("Excel data converted to JSON and saved as 'output3.json'")
