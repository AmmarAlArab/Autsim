import pandas as pd
import os

filename = 'autism_data.csv'

if not os.path.exists(filename):
    print(f" Error: {filename} not found!")
else:
 
    df = pd.read_csv(filename)
    

    df.columns = df.columns.str.strip()
    
    print("----- UNIQUE VALUES IN EACH COLUMN -----")


    if 'Sex' in df.columns:
        print("\n[Sex] values found:")
        print(df['Sex'].unique())

    if 'Jauundice' in df.columns:
        print("\n[Jauundice] values found:")
        print(df['Jauundice'].unique())

 
    if 'Family_ASD' in df.columns:
        print("\n[Family_ASD] values found:")
        print(df['Family_ASD'].unique())

    
    if 'Class' in df.columns:
        print("\n[Class] values found:")
        print(df['Class'].unique())
        
    print("\n------------------------------------------------")