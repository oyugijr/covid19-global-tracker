import pandas as pd
import requests
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'
BASE_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"

def download_covid_data():
    """Download and process COVID-19 data from JHU repository"""
    try:
        # Download datasets
        confirmed = pd.read_csv(BASE_URL + "time_series_covid19_confirmed_global.csv")
        deaths = pd.read_csv(BASE_URL + "time_series_covid19_deaths_global.csv")
        recovered = pd.read_csv(BASE_URL + "time_series_covid19_recovered_global.csv")
        
        # Save raw data
        confirmed.to_csv(DATA_DIR / "raw_confirmed.csv", index=False)
        deaths.to_csv(DATA_DIR / "raw_deaths.csv", index=False)
        recovered.to_csv(DATA_DIR / "raw_recovered.csv", index=False)
        
        return confirmed, deaths, recovered
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None, None, None

def process_data(confirmed, deaths, recovered):
    """Process and merge datasets"""
    def melt_data(df, value_name):
        return df.melt(
            id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
            var_name='Date',
            value_name=value_name
        )
    
    confirmed_long = melt_data(confirmed, 'Confirmed')
    deaths_long = melt_data(deaths, 'Deaths')
    recovered_long = melt_data(recovered, 'Recovered')
    
    # Merge datasets
    merged = confirmed_long.merge(
        deaths_long, 
        on=['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']
    ).merge(
        recovered_long,
        on=['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']
    )
    
    # Clean data
    merged['Date'] = pd.to_datetime(merged['Date'])
    merged = merged.sort_values(['Country/Region', 'Date'])
    
    # Save processed data
    merged.to_csv(DATA_DIR / "processed_global_data.csv", index=False)
    return merged

if __name__ == "__main__":
    print("Downloading COVID-19 data...")
    confirmed, deaths, recovered = download_covid_data()
    if confirmed is not None:
        print("Processing data...")
        process_data(confirmed, deaths, recovered)
        print("Data processing complete!")
    else:
        print("Failed to download data")