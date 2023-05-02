import pandas as pd

df = pd.read_csv('.\data\classified_names_augmentation.csv') 

# Function to create augmented names
def augment_names(df):
    augmented_data = []
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            name1, gender1 = df.iloc[i]['nombre'], df.iloc[i]['gender']
            name2, gender2 = df.iloc[j]['nombre'], df.iloc[j]['gender']

            if gender1 == gender2:
                combined_name1 = name1 + name2
                combined_name2 = name2 + name1
                augmented_data.append((combined_name1, gender1))
                augmented_data.append((combined_name2, gender2))

    augmented_df = pd.DataFrame(augmented_data, columns=['nombre', 'gender'])
    return augmented_df

augmented_df = augment_names(df)

# Combine the original DataFrame with the augmented DataFrame
combined_df = pd.concat([df, augmented_df]).reset_index(drop=True)
print(combined_df.shape)


combined_df.to_csv("./data/classified_names_augmentation_combined.csv", index=False) 
