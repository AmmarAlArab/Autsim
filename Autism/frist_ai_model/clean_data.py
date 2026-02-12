import pandas as pd
import os


input_file = 'autism_data.csv'
output_file = 'autism_data_clean.csv'


if not os.path.exists(input_file):
    print(f" Error: {input_file} not found!")
else:
    print(" Loading dataset...")
    df = pd.read_csv(input_file)
    df.columns = df.columns.str.strip() 
    
   
    original_count = len(df)
    print(f" Loaded! Original Rows: {original_count}")

     
 
    df['Sex'] = df['Sex'].map({'m': 1, 'f': 0})
    

    lower_case_mapping = {'yes': 1, 'no': 0}
    
    if 'Jauundice' in df.columns:
        df['Jauundice'] = df['Jauundice'].map(lower_case_mapping)
        df.rename(columns={'Jauundice': 'Jaundice'}, inplace=True) 
    
    if 'Family_ASD' in df.columns:
        df['Family_ASD'] = df['Family_ASD'].map(lower_case_mapping)
    upper_case_mapping = {'YES': 1, 'NO': 0}
    
    if 'Class' in df.columns:
        df['Class'] = df['Class'].map(upper_case_mapping)

    df.dropna(inplace=True)
    
    final_count = len(df)
    
    print("\n---------------------------------------------------")
    if final_count > 0:
        print(" SUCCESS! Data cleaned successfully.")
        print(f"Final Row Count: {final_count} (out of {original_count})")
        
     
        df.to_csv(output_file, index=False)
        print(f" Saved to: '{output_file}'")
        
     
        print("\nFirst 5 rows of clean data:")
        print(df.head())
    else:
        print(" WARNING: The file is empty after cleaning!")
        print("Please check if the mappings match the file values exactly.")
    print("---------------------------------------------------")