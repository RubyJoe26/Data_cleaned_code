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

# print("Columns in the DataFrame:", df.columns)

df = df.drop_duplicates()

if "Not_Useful_Column" in df.columns:
    df.drop(columns=["Not_Useful_Column"], inplace=True)
else:
    print("Warning: 'Not_Useful_Column' does not exist in the DataFrame.")

if "last_name" in df.columns:
    df["last_name"] = df["last_name"].str.replace("[._/]", "", regex=True)
else:
    print("Warning: 'last_name' column does not exist in the DataFrame.")

if "phone_number" in df.columns:
    df["phone_number"] = df["phone_number"].str.replace("nan--|Na--", "", regex=True)
else:
    print("Error: 'phone_number' column does not exist in the DataFrame.")

print(df)








