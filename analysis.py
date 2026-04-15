import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS   # used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

    file_path = get_resource_path("data/main_dataset.csv")
# ---------------- LOAD DATA ----------------
def load_data():
   df = pd.read_csv(get_resource_path("data/main_dataset.csv"))
   return df


# ---------------- TRANSFORM DATA ----------------
def transform_data(df):
    # Remove unnecessary column
    if 'S. No.' in df.columns:
        df = df.drop(columns=['S. No.'])

    # Rename column
    df = df.rename(columns={'States/UTs': 'State'})

    # Convert wide format → long format
    df = df.melt(id_vars='State',
                 var_name='Year',
                 value_name='Value')

    # Extract year (2011, 2012, etc.)
    df['Year'] = df['Year'].str.extract('(\d{4})')

    # Convert Year to integer
    df['Year'] = df['Year'].astype(int)

    return df


# ---------------- CLEAN DATA ----------------
def clean_data(df):
    # Remove missing values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    return df


# ---------------- ANALYSIS ----------------

# Year-wise trend
def plot_yearly_trend(df):
    yearly_avg = df.groupby('Year')['Value'].mean()

    yearly_avg.plot(marker='o')
    plt.title("Average Severity of Accidents Over Years")
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100 Accidents")
    plt.grid()
    plt.show()


# Top dangerous states
def plot_top_states(df):
    state_avg = df.groupby('State')['Value'].mean().sort_values(ascending=False).head(10)

    state_avg.plot(kind='bar')
    plt.title("Top 10 Dangerous States (Avg Severity)")
    plt.xlabel("State")
    plt.ylabel("Deaths per 100 Accidents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Load
    df = load_data()

    # Transform
    df = transform_data(df)

    # Clean
    df = clean_data(df)

    # Preview
    print("\nTransformed Data:")
    print(df.head())

    # Graphs
    plot_yearly_trend(df)
    plot_top_states(df)