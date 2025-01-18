import pandas as pd

data1 = pd.read_csv("file1.csv")
data2 = pd.read_csv("file2.csv")

data_combined = pd.concat([data1, data2])

duplicated_data = data_combined[data_combined.duplicated(keep=False)]

merged_data = data_combined.drop_duplicates().reset_index(drop=True)

duplicated_data.to_csv("duplicated_file.csv", index=False)
merged_data.to_csv("merged_file.csv", index=False)

print("The files 'file1_large.csv' and 'file2_large.csv' have been processed.")
print("'duplicated_file.csv' contains only the duplicated rows.")
print("'merged_file.csv' contains the merged data without duplicates.")