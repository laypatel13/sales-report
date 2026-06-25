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

def clean_data(df):
    print(f"\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    df = df.dropna()              
    df = df.drop_duplicates()   
    
    print(f"\nCleaned! Remaining rows: {len(df)}")
    return df 

def generate_report(df):
    df["revenue"] = df["quantity"] * df["price"]
    
    print(f"\nTotal Revenue: {df['revenue'].sum():.2f}")
    
    print("\nSales by Category:")
    by_category = df.groupby("category")["revenue"].sum()
    print(by_category)
    
    print("\nSales by Region:")
    by_region = df.groupby("region")["revenue"].sum()
    print(by_region)

    print("\nTop Selling Product:")
    top_product = df.groupby("product")["quantity"].sum()
    top_product = top_product.sort_values(ascending=False)
    print(top_product.head(1))

def save_report(df):
    df.to_csv("output.csv", index=False)
    print("Report saved to output.csv!")
    
def main():
    filename = input("Enter CSV filename: ")
    df = load_data(filename)
    if df is None:
        return
    
    while True:
        print("\n--- Sales Report Generator ---")
        print("1. Clean data")
        print("2. Generate report")
        print("3. Save cleaned data")
        print("4. Quit")
        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
            
        if choice == 1:
            df = clean_data(df)
        elif choice == 2:
            generate_report(df)
        elif choice == 3:
            save_report(df)
        elif choice == 4:
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()