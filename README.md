# COVID-19 ETL Pipeline

This project is a simple ETL (Extract, Transform, Load) pipeline for COVID-19 data by country. It fetches live data from a public API, processes the data using pandas, and visualizes key metrics using matplotlib.

## Features

- Extracts the latest COVID-19 statistics for countries worldwide from the [disease.sh](https://disease.sh/) API.
- Transforms the data by selecting relevant columns and calculating:
  - Cases per million people
  - Death rate (%)
  - Recovery rate (%)
- Identifies and visualizes:
  - Top 10 countries by COVID-19 cases per million
  - Top 10 countries by COVID-19 death rate
  - Top 10 countries by COVID-19 recovery rate
- Visualizes data with bar charts and pie charts.

## Requirements

- Python 3.7+
- pandas
- requests
- matplotlib

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/covid_etl_pipeline.git
   cd covid_etl_pipeline
