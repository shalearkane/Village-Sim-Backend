import pandas as pd

# Load the CSV file into a Pandas DataFrame
csv_file_path = "data/lgd_localbodies.csv"
df = pd.read_csv(csv_file_path, low_memory=False)

# Select only the necessary columns
selected_columns = ["stateNameEnglish", "localBodyCode", "localBodyNameEnglish", "localBodyTypeName", "localBodyTypeCode"]
df_selected = df[selected_columns]

# Save the selected columns to a new CSV file with compression
output_csv_file_path = "data/selected_localbodies.csv.gz"
df_selected.to_csv(output_csv_file_path, index=False, compression="gzip")

print(f"Selected columns saved to: {output_csv_file_path}")
