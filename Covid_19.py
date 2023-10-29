import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Covid_19.csv")
data['Date_reported'] = pd.to_datetime(data['Date_reported'])

# 1. Line Plot: Global daily cases over time
def plot_global_cases(data):
    global_data = data.groupby("Date_reported").sum()
    plt.figure(figsize=(12, 6))
    plt.plot(global_data.index, global_data["New_cases"], label="Daily Cases")
    plt.title("Global Daily COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Cases")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_global_cases(data)

# 2. Bar Chart: Total cases by month for the current year
def plot_monthly_cases(data):
    this_year = pd.Timestamp.now().year
    monthly_data = data[data['Date_reported'].dt.year == this_year]
    monthly_cases = monthly_data.groupby(monthly_data['Date_reported'].dt.month).sum()
    plt.figure(figsize=(12, 6))
    plt.bar(monthly_cases.index, monthly_cases["New_cases"], label=f"Cases in {this_year}")
    plt.title(f"Total COVID-19 Cases By Month in {this_year}")
    plt.xlabel("Month")
    plt.ylabel("Number of Cases")
    plt.xticks(monthly_cases.index)
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

plot_monthly_cases(data)


# 3. Pie Chart: Breakdown of cases vs. deaths globally
def plot_case_death_breakdown(data):
    total_cases = data["Cumulative_cases"].sum()
    total_deaths = data["Cumulative_deaths"].sum()
    sizes = [total_cases, total_deaths]
    labels = ["Total Cases", "Total Deaths"]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Global COVID-19 Total Cases vs. Total Deaths")
    plt.show()

plot_case_death_breakdown(data)
