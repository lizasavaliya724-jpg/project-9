import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        print("Sales Data Analyzer Object Created!")

    def __del__(self):
        print("Sales Data Analyzer Object Destroyed!")

    # Create Sample Dataset
    def create_sample_dataset(self):
        data = {
            "SalesID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
            "Product": [
                "Product A", "Product B", "Product C", "Product D",
                "Product E", "Product A", "Product B", "Product C",
                "Product D", "Product E"
            ],
            "Region": [
                "North", "East", "West Coast", "South", "Central",
                "North", "East", "West Coast", "South", "Central"
            ],
            "Sales": [500, 600, 700, 800, 550, 650, 750, 900, 850, 950],
            "Year": [2022, 2022, 2022, 2022, 2022,
                     2023, 2023, 2023, 2023, 2023],
            "Profit": [100, 150, 200, 180, 120,
                       160, 210, 250, 220, 300]
        }

        df = pd.DataFrame(data)
        df.to_csv("sales_data.csv", index=False)
        print("Sample dataset created successfully!")

    # Load Dataset
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")

        except FileNotFoundError:
            print("File not found! Creating sample dataset...")
            self.create_sample_dataset()
            self.data = pd.read_csv("sales_data.csv")
            print("Dataset loaded successfully!")

        except Exception as e:
            print("Error loading dataset:", e)

    # Explore Data
    def explore_data(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        while True:
            print("\n===== Explore Data =====")
            print("1. Display first 5 rows")
            print("2. Display last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic information")
            print("6. Display dataset description")
            print("7. Back to Main Menu")

            ch = input("Enter your choice: ")

            if ch == '1':
                print(self.data.head())

            elif ch == '2':
                print(self.data.tail())

            elif ch == '3':
                print(self.data.columns.tolist())

            elif ch == '4':
                print(self.data.dtypes)

            elif ch == '5':
                self.data.info()

            elif ch == '6':
                print(self.data.describe())

            elif ch == '7':
                break

            else:
                print("Invalid choice!")

    # DataFrame Operations
    def dataframe_operations(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        print("\n===== DataFrame Operations =====")
        print("1. Convert columns to NumPy array")
        print("2. Indexing")
        print("3. Slicing")
        print("4. Mathematical Operations")
        print("5. Combine DataFrames")
        print("6. Split DataFrame")

        ch = input("Enter your choice: ")

        if ch == '1':
            arr = self.data["Sales"].to_numpy()
            print("NumPy Array:", arr)

        elif ch == '2':
            arr = self.data["Sales"].to_numpy()
            print("First Element:", arr[0])
            print("Third Element:", arr[2])

        elif ch == '3':
            arr = self.data["Sales"].to_numpy()
            print("Array Slicing:", arr[0:5])

        elif ch == '4':
            self.mathematical_operations()

        elif ch == '5':
            self.combine_data()

        elif ch == '6':
            self.split_data()

        else:
            print("Invalid choice!")

    # Mathematical Operations
    def mathematical_operations(self):
        sales = self.data["Sales"].to_numpy()

        print("\n===== Mathematical Operations =====")
        print("Original Sales:", sales)
        print("Addition:", sales + 100)
        print("Subtraction:", sales - 100)
        print("Multiplication:", sales * 2)
        print("Division:", sales / 2)

    # Combine DataFrames
    def combine_data(self):
        new_data = pd.DataFrame({
            "SalesID": [111, 112],
            "Product": ["Product F", "Product G"],
            "Region": ["North", "South"],
            "Sales": [1000, 1100],
            "Year": [2024, 2024],
            "Profit": [350, 400]
        })

        combined = pd.concat(
            [self.data, new_data],
            ignore_index=True
        )

        print("\nCombined DataFrame:")
        print(combined)

    # Split DataFrame
    def split_data(self):
        north = self.data[self.data["Region"] == "North"]
        south = self.data[self.data["Region"] == "South"]

        print("\nNorth Region Data:")
        print(north)

        print("\nSouth Region Data:")
        print(south)

    # Handle Missing Data
    def clean_data(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        print("\n===== Handle Missing Data =====")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with specific value")

        ch = input("Enter your choice: ")

        if ch == '1':
            print(self.data[self.data.isnull().any(axis=1)])

        elif ch == '2':
            self.data = self.data.copy()
            self.data.fillna(
                self.data.select_dtypes(include="number").mean(),
                inplace=True
            )
            print("Missing values filled with mean!")
            print(self.data)

        elif ch == '3':
            self.data = self.data.dropna()
            print("Missing rows dropped successfully!")
            print(self.data)

        elif ch == '4':
            self.data = self.data.fillna(0)
            print("Missing values replaced with 0!")
            print(self.data)

        else:
            print("Invalid choice!")

    # Search, Sort and Filter
    def search_sort_filter(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        print("\n===== Search, Sort and Filter =====")
        print("1. Search Product")
        print("2. Sort by Sales")
        print("3. Filter by Region")
        print("4. Filter by Sales")

        ch = input("Enter your choice: ")

        if ch == '1':
            product = input("Enter product name: ")
            print(self.data[
                self.data["Product"].str.contains(
                    product, case=False, na=False
                )
            ])

        elif ch == '2':
            print(self.data.sort_values(
                by="Sales", ascending=False
            ))

        elif ch == '3':
            region = input("Enter region: ")
            print(self.data[
                self.data["Region"].str.contains(
                    region, case=False, na=False
                )
            ])

        elif ch == '4':
            amount = float(input("Enter minimum sales: "))
            print(self.data[self.data["Sales"] > amount])

        else:
            print("Invalid choice!")

    # Aggregate Functions
    def aggregate_functions(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        print("\n===== Aggregate Functions =====")
        print("Total Sales:", self.data["Sales"].sum())
        print("Average Sales:", self.data["Sales"].mean())
        print("Maximum Sales:", self.data["Sales"].max())
        print("Minimum Sales:", self.data["Sales"].min())
        print("Total Records:", self.data["Sales"].count())

        print("\nRegion-wise Sales:")
        print(self.data.groupby("Region")["Sales"].sum())

    # Statistical Analysis
    def statistical_analysis(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        sales = self.data["Sales"]

        print("\n===== Statistical Analysis =====")
        print("Mean:", sales.mean())
        print("Median:", sales.median())
        print("Standard Deviation:", sales.std())
        print("Variance:", sales.var())
        print("25th Percentile:", sales.quantile(0.25))
        print("50th Percentile:", sales.quantile(0.50))
        print("75th Percentile:", sales.quantile(0.75))

        print("\nComplete Statistics:")
        print(self.data.describe())

    # Pivot Table
    def create_pivot_table(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        pivot = pd.pivot_table(
            self.data,
            values="Sales",
            index="Region",
            columns="Year",
            aggfunc="sum",
            fill_value=0
        )

        print("\n===== Sales Pivot Table =====")
        print(pivot)

    # Data Visualization
    def visualize_data(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        print("\n===== Data Visualization =====")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Heatmap")
        print("8. Box Plot")

        ch = input("Enter your choice: ")

        plt.figure(figsize=(8, 5))

        if ch == '1':
            self.data.groupby("Product")["Sales"].sum().plot(
                kind="bar"
            )
            plt.title("Product-wise Sales")
            plt.xlabel("Product")
            plt.ylabel("Sales")

        elif ch == '2':
            self.data.groupby("Year")["Sales"].sum().plot(
                kind="line", marker="o"
            )
            plt.title("Year-wise Sales")
            plt.xlabel("Year")
            plt.ylabel("Sales")

        elif ch == '3':
            plt.scatter(
                self.data["Sales"],
                self.data["Year"]
            )
            plt.title("Sales vs Year")
            plt.xlabel("Sales")
            plt.ylabel("Year")

        elif ch == '4':
            region_sales = self.data.groupby("Region")["Sales"].sum()
            plt.pie(
                region_sales,
                labels=region_sales.index,
                autopct="%1.1f%%"
            )
            plt.title("Region-wise Sales")

        elif ch == '5':
            plt.hist(
                self.data["Sales"],
                bins=5,
                edgecolor="black"
            )
            plt.title("Sales Distribution")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")

        elif ch == '6':
            pivot = self.data.pivot_table(
                values="Sales",
                index="Year",
                columns="Region",
                aggfunc="sum",
                fill_value=0
            )

            plt.stackplot(
                pivot.index,
                *[pivot[col] for col in pivot.columns],
                labels=pivot.columns
            )
            plt.title("Year-wise Regional Sales")
            plt.xlabel("Year")
            plt.ylabel("Sales")
            plt.legend(loc="upper left")

        elif ch == '7':
            sns.heatmap(
                self.data.select_dtypes(
                    include="number"
                ).corr(),
                annot=True,
                cmap="coolwarm"
            )
            plt.title("Sales Data Heatmap")

        elif ch == '8':
            sns.boxplot(x=self.data["Sales"])
            plt.title("Sales Box Plot")
            plt.xlabel("Sales")

        else:
            plt.close()
            print("Invalid choice!")
            return

        plt.tight_layout()
        plt.show()

    # Save Visualization
    def save_visualization(self):
        if self.data is None:
            print("Please load dataset first!")
            return

        filename = input("Enter file name (e.g. sales_plot.png): ")

        plt.figure(figsize=(8, 5))
        self.data.groupby("Product")["Sales"].sum().plot(
            kind="bar"
        )

        plt.title("Product-wise Sales")
        plt.xlabel("Product")
        plt.ylabel("Sales")
        plt.tight_layout()

        plt.savefig(filename)
        plt.close()

        print("Visualization saved successfully!")


# Main Program
obj = SalesDataAnalyzer()

while True:

    print("\n========== Data Analysis & Visualization Program ==========")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        path = input("Enter CSV file path: ")
        obj.load_data(path)

    elif choice == '2':
        obj.explore_data()

    elif choice == '3':
        obj.dataframe_operations()

    elif choice == '4':
        obj.clean_data()

    elif choice == '5':
        obj.aggregate_functions()
        obj.statistical_analysis()
        obj.create_pivot_table()

    elif choice == '6':
        obj.visualize_data()

    elif choice == '7':
        obj.save_visualization()

    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")