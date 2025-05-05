# COVID-19 Global Data Tracker

A Python project to explore, clean, and visualize global COVID-19 data.

## 🎯 Objectives

- Load real-world COVID-19 data
- Clean and preprocess data
- Perform exploratory data analysis
- Visualize global trends and country-level insights

## 🛠 Tools and Libraries

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## ▶️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/oyugijr/covid19-global-tracker.git
   cd covid19-global-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook:
   ```bash
   jupyter notebook notebook/covid_analysis.ipynb
   ```

## 🔍 Insights

- The spread of COVID-19 varied greatly across continents.
- Daily new cases and deaths showed clear waves.
- Vaccination rollout changed the trajectory significantly.

---

# src/data_loader.py

import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("✅ Data loaded successfully")
        return data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

---

# src/data_cleaner.py

def clean_data(df):
    df = df.dropna(subset=['location', 'date', 'total_cases'])
    df['date'] = pd.to_datetime(df['date'])
    return df

---

# src/data_visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns


def plot_top_countries(df, column='total_cases', top_n=10):
    latest = df[df['date'] == df['date'].max()]
    top = latest.groupby('location')[column].sum().sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top.values, y=top.index)
    plt.title(f"Top {top_n} Countries by {column.replace('_', ' ').title()}")
    plt.xlabel(column.replace('_', ' ').title())
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

---

# requirements.txt

pandas
matplotlib
seaborn
jupyter

---

# notebook/covid_analysis.ipynb

# The actual notebook file should be created in Jupyter. Here's a suggested structure:

# 1. Import modules
from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.data_visualizer import plot_top_countries

# 2. Load data
data = load_data("../data/covid_data.csv")

# 3. Clean data
data = clean_data(data)

# 4. Visualize
data.head()
plot_top_countries(data, column='total_cases')
plot_top_countries(data, column='total_deaths')
