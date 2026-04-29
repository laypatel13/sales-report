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
    return df