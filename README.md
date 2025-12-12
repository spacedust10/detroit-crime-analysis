# Detroit Crime Forecasting & Resource Allocation

A data-driven exploration of Detroit’s reported crime incidents combining **spatial analytics**, **time-series forecasting**, and **AI-based modeling** to identify hotspots, forecast trends, and inform strategic planning.

---

## Overview
This repository presents an end-to-end **machine-learning workflow** for analyzing and forecasting crime data using the **Detroit RMS (Records Management System)** open dataset.  
The project integrates **SARIMAX** and **LSTM** models with geospatial clustering techniques such as **KDE**, **DBSCAN**, and **Getis-Ord Gi\*** to deliver interpretable forecasts and risk insights for urban-safety research.

---

## Objectives
- Build reproducible pipelines for data ingestion, cleaning, and feature engineering.  
- Analyze **temporal and spatial dynamics** in crime patterns.  
- Develop and compare classical vs. deep-learning forecasting models.  
- Quantify uncertainty and trend reliability for operational decisions.  
- Deploy dashboards and interactive visualizations for stakeholder exploration.

---

## Technologies Used
**Languages:** Python, SQL  
**Frameworks & Libraries:** TensorFlow, scikit-learn, Statsmodels, GeoPandas, Pandas, NumPy  
**Modeling & Analytics:** SARIMAX, LSTM, KDE, DBSCAN, Getis-Ord Gi\*, Time-Series Decomposition  
**Visualization & Deployment:** Plotly, Dash, Streamlit, Folium, Scattermapbox  
**Experiment Tracking & Environment:** MLflow (Databricks), Jupyter, Git  

---

## Project Structure

<details>
<summary><b>Part 1 – Data Acquisition & Initial Exploration</b></summary>

- Collected Detroit RMS Crime Incidents via the city’s open-data API.  
- Established temporal indexing (`incident_occurred_at`) and validated coordinates.  
- Conducted exploratory statistics to assess completeness and variability.

</details>

<details>
<summary><b>Part 2 – Data Cleaning & Feature Engineering</b></summary>

- Dropped redundant administrative attributes; standardized event/time/spatial fields.  
- Engineered calendar features (hour, day, week, month, year).  
- Built an interactive **Dash overview dashboard** with filters, KPI cards, and crime-by-hour/day heatmaps.

</details>

<details>
<summary><b>Part 3 – Temporal Pattern Analysis</b></summary>

- Aggregated incidents at daily, weekly, and monthly resolutions.  
- Performed **additive/multiplicative decomposition** for trend and seasonality extraction.  
- Constructed a temporal dashboard to highlight **peak hours, weekdays, and seasonal effects**.

</details>

<details>
<summary><b>Part 4 – Spatial Pattern Analysis</b></summary>

- Applied **KDE** and **DBSCAN** clustering to locate organically emerging hotspots.  
- Conducted **Getis-Ord Gi\*** analysis to confirm statistically significant high-activity zones.  
- Visualized results with **Folium** and **Plotly** interactive heatmaps.  
- Explored spatial correlations between crime locations and liquor-store density.

</details>

<details>
<summary><b>Part 5 – Model Training & Forecasting</b></summary>

- Trained **SARIMAX** (monthly) and **LSTM** (weekly) models on aggregated series.  
- Evaluated performance using RMSE, MAE, MAPE, R², and **Directional Accuracy (≈ 78.8 %)**.  
- Generated **1-year forecasts** with 95 % confidence bands and visual comparison plots.  
- Demonstrated model stability via ADF/ACF/PACF diagnostics and early-stopping criteria.

</details>

<details>
<summary><b>Part 6 – Resource Allocation & Risk Scoring</b></summary>

- Trained precinct-specific SARIMAX models for top-volume districts.  
- Computed a **Composite Risk Score** blending forecasted volume and recent trend momentum.  
- Developed an interactive **Scattermapbox visualization** displaying high-risk and increasing-trend precincts.  
- Analyzed **seasonal and within-week patterns** to inform staffing and outreach timing.

</details>

---

## Key Results
- Detected statistically significant hotspots (Gi\* p < 0.05) aligned with major activity corridors.  
- **SARIMAX model:** RMSE < 10 % of mean, MAPE ≈ 6.3 %, Directional Accuracy ≈ 78.8 %.  
- Integrated analytics delivered interpretable, reproducible forecasts for each precinct.  
- Dashboards enabled **data-driven scenario planning** and stakeholder transparency.

---

## Ethical Considerations
All outputs describe **reported incidents**, not verified crime rates.  
The analysis is intended for **academic and strategic insight**, emphasizing responsible, transparent, and non-prescriptive use of predictive analytics in public-sector data.

---

## Getting Started

```bash
# Clone repository
git clone https://github.com/yourusername/detroit-crime-forecasting.git
cd detroit-crime-forecasting

# Install dependencies
pip install -r requirements.txt

# Launch interactive dashboard
python app.py