# COVID-19 Data Analysis Framework

## Overview

This document outlines the analytical methodologies and statistical approaches used in the COVID-19 Global Data Tracker project.

## Key Analytical Components

### 1. Time Series Analysis

**Objective:** Track pandemic progression globally and nationally

**Methods:**

- Daily case aggregation
- 7-day moving average calculation:

```python
df['7d_MA'] = df.groupby('Country/Region')['Confirmed'].transform(lambda x: x.rolling(7).mean())
```

### 2. Mortality Rate Analysis

**Formula:**

```python
Mortality Rate = (Total Deaths / Confirmed Cases) * 100
```

**Code:**

```python
country_data['Mortality Rate'] = (country_data['Deaths'] / country_data['Confirmed']) * 100
```

### 3. Case Trend Visualization

- Heatmap of daily new cases
- Country comparison trajectories
- Growth factor calculation:

```python
GF_t = (C_t - C_{t-1}) / (C_{t-1} - C_{t-2})
```

### 4. Spatial Analysis

- Country-level aggregation
- Regional comparisons
- Normalized case counts:

```python
df['Cases per 100k'] = (df['Confirmed'] / population_data['Population']) * 1e5
```

### 5. Growth Rate Modeling

```python
global_daily['Growth Rate'] = global_daily['Confirmed'].pct_change()
global_daily['EMA_14'] = global_daily['Growth Rate'].ewm(span=14).mean()
```

### 6. Doubling Time Calculation

```python
Td = ln(2) / ln(1 + r)
```

Where `r` is the daily growth rate.

### 7. Statistical Testing

- Kolmogorov–Smirnov test
- Pearson correlation
- Regression analysis

---

## 🧪 Data Processing Pipeline

### 1. Cleaning

```python
df = df.dropna(subset=['Confirmed', 'Deaths'])
df = df[df['New Cases'] >= 0]
```

### 2. Feature Engineering

```python
df['New Cases'] = df.groupby('Country/Region')['Confirmed'].diff()
df['Recovery Rate'] = df['Recovered'] / df['Confirmed']
```

### 3. Normalization

- Adjusted per 100k population
- Time-indexed series
- Z-score normalization

---

## 📊 Visualization Guidelines

### 1. Principles

- Colorblind-friendly palettes
- Dual axes for comparison
- Time-based formatting:

```python
ax.xaxis.set_major_formatter(DateFormatter("%b '%y"))
```

### 2. Interactive Elements

- Plotly charts
- Tooltips and annotations

### 3. Output Standards

- Export as PDF, SVG
- Interactive HTML
- Static images: 300 DPI

---

## 🔍 Key Insights

- Top 10 countries by case and death counts
- Mortality and recovery rate comparisons
- Daily and cumulative progression trends
- Country growth factor changes
- Regional comparisons
- Predictive modeling results
