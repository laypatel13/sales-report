# 📈 Sales Report Generator - CLI
A simple command-line Sales Report Generator built using Python. This project helps you load, clean, and analyze sales data from CSV files with a colorful and neatly formatted tabular interface.

---

## ✨ Features

- Load and preview CSV sales data
- Clean data by removing missing values and duplicates
- Generate revenue reports by category and region
- Identify top selling products
- Export full sales report to a `.txt` file
- Save cleaned data to a new CSV file
- Colorful CLI output for better readability

---

## 📦 Install via pip

```bash
pip install laypatel13-sales-report
```

Then run it from anywhere in your terminal:

```bash
sales-report
```

---

## 🛠️ Install from source

```bash
git clone https://github.com/laypatel13/sales-report.git
cd sales-report
pip install -r requirements.txt
pip install -e .
```

Then run:

```bash
sales-report
```

---

## 📂 Project Structure

```text
sales-report/
├── sales_report/
│   ├── __init__.py
│   └── main.py
├── sales-data.csv
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧰 Built With

- Used [Pandas](https://pandas.pydata.org/) for data loading, cleaning, and analysis.
- Used [Colorama](https://pypi.org/project/colorama/) for colored terminal output.
- Used [Tabulate](https://pypi.org/project/tabulate/) for formatted table display.