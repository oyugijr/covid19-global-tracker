
# Data Sources and Processing

## Primary Data Sources

| Dataset | Source | Frequency | Description |
|---------|--------|-----------|-------------|
| COVID-19 Cases | [JHU CSSE](https://github.com/CSSEGISandData/COVID-19) | Daily | Time-series of confirmed cases, deaths, and recoveries |
| Population Data | [World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL) | Annual | Country population estimates |

## Data Processing Pipeline

1. **Raw Data Ingestion**
    - Download CSV files from JHU CSSE repository
    - Store in `data/raw/` directory

```python
# scripts/data_processing.py
confirmed = pd.read_csv(BASE_URL + "time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv(BASE_URL + "time_series_covid19_deaths_global.csv")
recovered = pd.read_csv(BASE_URL + "time_series_covid19_recovered_global.csv")
```

## Data Transformation

- Wide-to-long format conversion
- Date parsing with explicit format:

```python
pd.to_datetime(df['Date'], format='%m/%d/%y')
```

## 3. Feature Engineering

```python
df['New Cases'] = df.groupby['Country/Region']('Confirmed').diff()
```

## Data Validation

- Negative value check
- Missing data imputation
- Outlier detection
- Data type validation

```python
# Check for negative values
if (df['Confirmed'] < 0).any():
    raise ValueError("Negative values found in confirmed cases")
```
