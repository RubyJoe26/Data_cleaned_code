# import pandas as pd
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)


# import pandas as pd
# print(pd.__version__)

import pandas as pd

# Load the Excel file
file_path = r'C:\Users\ELCOT\Desktop\Customer call\Customer Call List.xlsx'
df = pd.read_excel(file_path)

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  #Show all values

df = df.drop_duplicates()

if "Not_Useful_Column" in df.columns:
    df.drop(columns=["Not_Useful_Column"], inplace=True)
else:
    print("Warning: 'Not_Useful_Column' does not exist in the DataFrame.")

if "Last_Name" in df.columns:
    df["Last_Name"] = df["Last_Name"].str.replace("[._/]", "", regex=True)
else:
    print("Warning: 'Last_Name' column does not exist in the DataFrame.")

if "Phone_Number" in df.columns:
    df["Phone_Number"] = df["Phone_Number"].str.replace("nan--|Na--", "", regex=True)
else:
    print("Error: 'Phone_Number' column does not exist in the DataFrame.")

if "Address" in df.columns:
    try:
        # Corrected: Use 'n=2' as a keyword argument to split the string into 3 parts
        df[["Street Address", "State", "Zip_code"]] = df["Address"].str.split(',', n=2, expand=True)
        print("Address split successfully!")
    except ValueError as e:
        print(f"Error during splitting: {e}")
else:
    print("Error: 'Address' column does not exist in the DataFrame.")

df = df.replace("N/a", "")
df = df.fillna('')
print(df)









