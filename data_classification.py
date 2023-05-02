import pandas as pd

# Read the CSV file
file_name = '../Dataset/nombres_con_col.csv'  # Replace with your CSV file name
df = pd.read_csv(file_name)

# Add a new column for the gender classification
df['genero'] = None
df = df.iloc[:300]

# Iterate through the DataFrame and ask for user input to classify each name
for idx, row in df.iterrows():
    print(f"Classify the name: {row['nombre']}")

    while True:
        gender_input = input("Enter 'q for male' or 'e for female': ").lower()
        if gender_input in ['q', 'e']:
            if gender_input == 'q':
                df.at[idx, 'gender'] = 'm'
                break
            if gender_input == 'e':
                df.at[idx, 'gender'] = 'f'
                break
        else:
            print("Invalid input. Please enter 'girl' or 'boy'.")

# Save the classified DataFrame to a new CSV file
output_file_name = 'classified_names.csv'
df.to_csv(output_file_name, index=False)
print(f"Classification completed. Results saved in '{output_file_name}'.")
