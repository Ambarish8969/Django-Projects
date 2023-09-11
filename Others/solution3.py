import pandas as pd    # Import necessory libraries
import json            # Import necessory libraries

input_excel_file = "G:\Django\input_excel_file.xlsx"    # Define the input Excel file path
df = pd.read_excel(input_excel_file)    # Read the data from the excel file into a Pandas dataframe

df = df.fillna("NULL")  # Fill missing values in the DataFrame with the string 'NULL'

grouped_data = df.groupby(['Customer ID', 'age'])   # Group the DataFrame by columns 'Customer ID' and 'age'

output_data = []    # Initialize an empty list for output data.

for (customer_id, age), group in grouped_data:  # Iterate through each group in 'grouped_data'
    
    # print(group["panel_code"])

    # Create a dictonary 'customer_entry' for each group
    customer_entry = {
        "Customer ID": str(customer_id),
        "age": str(age),
        str(group["panel_code"]): [] 
    }

    panels_dict = {}    # Initialize an empty dictonary 'panels_dict' to store panel data

    for index, row in group.iterrows(): # Iterate through rows in the 'group' Dataframe
        panel_name = row["panel_name"] # Accessing individual element.
        panel_code = row["panel_code"] # Accessing individual element.
        parameter_entry = {
            "parameterName": row["Parameter Name"],
            "unit": row["Units"],
            "parameterCode": str(row["Parameter Code"]),
            "value": str(row["Result"]),
            "lowerRange": str(row["Low Range"]),
            "upperRange": str(row["High Range"]),
            "displayRange": f"{row['Low Range']}-{row['High Range']}"
        }

        if panel_name not in panels_dict:   # Check if the panel name exists in panels_dict' and add it if not.
            panels_dict[panel_name] = {
                "panel_name": panel_name,
                "panel_code": panel_code,
                # str(row["Parameter Code"]): []
            }

        # Append the 'parameter_entry' to the appropriate panel in 'panels_dict'
        # panels_dict[panel_name][str(row["Parameter Code"])].append(parameter_entry)
    
    # Assign the 'panels_dict' as the 'panelList' in customer_entry
    customer_entry[str(panel_code)] = list(panels_dict.values())

    # Append the 'customer_entry' to the 'output_data' list.
    output_data.append(customer_entry)

output_json = json.dumps(output_data)   # Convert the 'output_data' list to a JSON formatted string.

with open("try.json", "w") as json_file:
    json_file.write(output_json)

print("JSON transformation complete.")