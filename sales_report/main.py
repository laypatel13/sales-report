import pandas as pd
import os
from colorama import init, Fore, Back, Style
from tabulate import tabulate

init(autoreset=True)

def load_data(filename):
    if not os.path.exists(filename):
        print(Fore.WHITE + Back.RED + "Fatal Error: File Not Found!" + Style.RESET_ALL)
        return None
    try:
        df = pd.read_csv(filename)
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"Loaded {filename} successfully!" + Style.RESET_ALL)
        print(Fore.WHITE + Style.NORMAL + f"Shape: {df.shape}" + Style.RESET_ALL)
        print("\n" + Fore.BLACK + Back.WHITE + "--- First 5 Rows ---" + Style.RESET_ALL)
        print(tabulate(df.head(), headers="keys", tablefmt="pretty", disable_numparse=True))
        return df
    except Exception as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed to load file. {e}" + Style.RESET_ALL)
        return None

def clean_data(df):
    print("\n" + Fore.BLACK + Back.WHITE + "--- Missing Values Before Cleaning ---" + Style.RESET_ALL)
    missing = df.isnull().sum()
    table_data = [[Fore.WHITE + Style.BRIGHT + col + Style.RESET_ALL,
                   Fore.WHITE + Style.NORMAL + str(val) + Style.RESET_ALL]
                  for col, val in missing.items()]
    headers = [Style.BRIGHT + h + Style.RESET_ALL for h in ["Column", "Missing"]]
    print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))

    df = df.dropna()
    df = df.drop_duplicates()
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"Cleaned! Remaining rows: {len(df)}" + Style.RESET_ALL)
    return df

def generate_report(df):
    df["revenue"] = df["quantity"] * df["price"]

    print("\n" + Fore.BLACK + Back.WHITE + "--- Total Revenue ---" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + f"  {df['revenue'].sum():.2f}" + Style.RESET_ALL)

    print("\n" + Fore.BLACK + Back.WHITE + "--- Sales by Category ---" + Style.RESET_ALL)
    by_category = df.groupby("category")["revenue"].sum().reset_index()
    table_data = [[Fore.WHITE + Style.BRIGHT + str(row["category"]) + Style.RESET_ALL,
                   Fore.WHITE + Style.NORMAL + f"{row['revenue']:.2f}" + Style.RESET_ALL]
                  for _, row in by_category.iterrows()]
    headers = [Style.BRIGHT + h + Style.RESET_ALL for h in ["Category", "Revenue"]]
    print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))

    print("\n" + Fore.BLACK + Back.WHITE + "--- Sales by Region ---" + Style.RESET_ALL)
    by_region = df.groupby("region")["revenue"].sum().reset_index()
    table_data = [[Fore.WHITE + Style.BRIGHT + str(row["region"]) + Style.RESET_ALL,
                   Fore.WHITE + Style.NORMAL + f"{row['revenue']:.2f}" + Style.RESET_ALL]
                  for _, row in by_region.iterrows()]
    headers = [Style.BRIGHT + h + Style.RESET_ALL for h in ["Region", "Revenue"]]
    print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))

    print("\n" + Fore.BLACK + Back.WHITE + "--- Top Selling Product ---" + Style.RESET_ALL)
    top_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False).reset_index()
    table_data = [[Fore.WHITE + Style.BRIGHT + str(row["product"]) + Style.RESET_ALL,
                   Fore.WHITE + Style.NORMAL + str(row["quantity"]) + Style.RESET_ALL]
                  for _, row in top_product.head(1).iterrows()]
    headers = [Style.BRIGHT + h + Style.RESET_ALL for h in ["Product", "Quantity Sold"]]
    print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))

def save_report(df):
    try:
        df.to_csv("output.csv", index=False)
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "Report saved to output.csv!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed to save report. {e}" + Style.RESET_ALL)

def export_report(df, source_filename):
    df["revenue"] = df["quantity"] * df["price"]
    lines = []
    lines.append("--- Sales Report ---\n")
    lines.append(f"Source: {source_filename}\n\n")

    lines.append(f"Total Revenue: {df['revenue'].sum():.2f}\n\n")

    lines.append("--- Sales by Category ---\n")
    by_category = df.groupby("category")["revenue"].sum()
    for category, revenue in by_category.items():
        lines.append(f"  {category}: {revenue:.2f}\n")

    lines.append("\n--- Sales by Region ---\n")
    by_region = df.groupby("region")["revenue"].sum()
    for region, revenue in by_region.items():
        lines.append(f"  {region}: {revenue:.2f}\n")

    lines.append("\n--- Top Selling Product ---\n")
    top_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
    top_name = top_product.index[0]
    top_qty = top_product.iloc[0]
    lines.append(f"  {top_name}: {top_qty} units\n")

    output_file = source_filename.replace(".csv", "_report.txt")
    try:
        with open(output_file, "w") as f:
            f.writelines(lines)
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"Report saved to {output_file}!" + Style.RESET_ALL)
    except IOError as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed to save report. {e}" + Style.RESET_ALL)


def main():
    filename = input(Fore.CYAN + Style.BRIGHT + "Enter CSV filename: " + Style.RESET_ALL)
    df = load_data(filename)
    if df is None:
        return

    while True:
        print("\n" + Fore.BLACK + Back.WHITE + "--- Sales Report Generator ---" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(1) Clean Data" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(2) Generate Report" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(3) Save Data" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(4) Export Report to TXT" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(5) Quit" + Style.RESET_ALL)

        try:
            choice = int(input("\n" + Fore.CYAN + Style.BRIGHT + "Enter Your Choice: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Please Enter A Number!" + Style.RESET_ALL)
            continue

        if choice == 1:
            df = clean_data(df)
        elif choice == 2:
            generate_report(df)
        elif choice == 3:
            save_report(df)
        elif choice == 4:
            export_report(df, filename)
        elif choice == 5:
            print(Fore.WHITE + Style.BRIGHT + "Bye! Thanks For Using Sales Report Generator!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Choice, Try Again!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
