import pandas as pd
import os

def load_data(filename):
    if not os.path.exists(filename):
        print("File Not Found!")
        return None
    df = pd.read_csv(filename)    
    print(f"\nLoaded {filename} successfully!")
    print(f"Shape: {df.shape}")   
    print("\nFirst 5 rows:")
    print(df.head())

def clean_data(df):
    print(f"\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    df = df.dropna()              
    df = df.drop_duplicates()   
    
    print(f"\nCleaned! Remaining rows: {len(df)}")
    return df 