# Project Methodology

## 1. Data Collection

- **Sources**:
  - Johns Hopkins University CSSE for global case data
  - World Bank for population statistics
  - WHO for health guidelines and updates
- **Methods**:
  - API calls for real-time data
  - CSV downloads for historical data
- **Frequency**: Daily updates
- **Data Cleaning**:
  - Missing value imputation
  - Outlier detection and handling
  - Data type conversions (e.g., dates, numerics)
- **Data Storage**:
  - Raw data stored in `data/raw/`
  - Processed data in `data/processed/`
- **Version Control**: Git for code, DVC for data
- **Data Formats**: CSV for tabular data, JSON for hierarchical data
- **Data Size**: Approximately 1GB for the entire dataset
- **Data Retention**: Historical data retained indefinitely, with regular backups

## 2. Analysis Framework

- **Tools Used**:
  - Pandas for data manipulation
  - Matplotlib/Seaborn for static visualizations
  - Plotly for interactive charts

## 3. Visualization Principles

- **Color Scheme**: Colorblind-friendly palettes
- **Scaling**: Dual linear/logarithmic views
- **Annotation**: Key event markers (lockdowns, vaccine rollouts)

## 4. Quality Assurance

- Unit tests for data processing
- Visual sanity checks
- Peer review process
