# '''Create csv file '''


import pandas as pd  

# Create sample data
data = {
    "Name": ["Pooja", "Raj", "Anita"],
    "Age": [25, 30, 28],
    "City": ["Mumbai", "Delhi", "Bangalore"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save DataFrame as CSV file
df.to_csv("data.xlsx", index=False)  

print("CSV file created successfully!")


''' Data Load karavva '''

# import pandas as pd

# # Replace 'data.csv' with the actual name of your file
# df = pd.read_csv(r"C:\Users\BAPS\Desktop\Pooja Rajput\Library\data.csv")

# # Check the first few rows of the data
# print(df.head())
