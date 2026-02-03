import streamlit as st
import pandas as pd
import plotly.express as px

# Load enriched dataset
df = pd.read_csv("data/processed/ethiopia_fi_unified_data_enriched.csv")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends", "Forecasts", "Projections"])

# -------------------------------
# Overview Page
# -------------------------------
if page == "Overview":
    st.title("Financial Inclusion Dashboard – Overview")

    # Key metrics summary
    st.metric("Account Ownership (2024)", "42%")
    st.metric("Mobile Money Accounts (2024)", "28%")
    st.metric("Digital Payment Adoption (2024)", "6%")

    st.write("**P2P/ATM Crossover Ratio:** Mobile money vs ATM density")
    st.write("Growth highlights: steady account ownership increase, but slowdown after 2017.")

# -------------------------------
# Trends Page
# -------------------------------
elif page == "Trends":
    st.title("Trends")

    # Indicator selector
    indicator = st.selectbox("Select Indicator", df["indicator"].unique())
    subset = df[df["indicator"] == indicator]

    # Interactive time series plot
    fig = px.line(subset, x="observation_date", y="value_numeric",
                  title=f"{indicator} Over Time", markers=True)
    st.plotly_chart(fig)

    # Date range slider
    min_year, max_year = int(df["observation_date"].min()), int(df["observation_date"].max())
    years = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    filtered = subset[(subset["observation_date"] >= years[0]) & (subset["observation_date"] <= years[1])]
    fig2 = px.line(filtered, x="observation_date", y="value_numeric", title=f"{indicator} ({years[0]}–{years[1]})", markers=True)
    st.plotly_chart(fig2)

# -------------------------------
# Forecasts Page
# -------------------------------
elif page == "Forecasts":
    st.title("Forecasts")

    st.write("Baseline vs Event-Augmented Forecasts (2025–2027)")

    # Example forecast data (replace with your regression outputs)
    forecast_data = pd.DataFrame({
        "Year": [2025, 2026, 2027],
        "Baseline": [47, 48, 48.5],
        "Event-Augmented": [49, 50, 52]
    })

    fig = px.line(forecast_data, x="Year", y=["Baseline","Event-Augmented"],
                  markers=True, title="Forecasts of Account Ownership")
    st.plotly_chart(fig)

    st.write("Confidence intervals and event impacts are shown in scenario analysis.")

# -------------------------------
# Projections Page
# -------------------------------
elif page == "Projections":
    st.title("Inclusion Projections")

    scenario = st.selectbox("Select Scenario", ["Optimistic", "Base", "Pessimistic"])

    if scenario == "Optimistic":
        forecast = [52, 55, 60]
    elif scenario == "Base":
        forecast = [50, 52, 54]
    else:
        forecast = [47, 48, 49]

    forecast_df = pd.DataFrame({"Year":[2025,2026,2027], "Forecast":forecast})
    fig = px.line(forecast_df, x="Year", y="Forecast", markers=True,
                  title=f"{scenario} Scenario – Progress Toward 60% Target")
    st.plotly_chart(fig)

    st.write(f"Under the {scenario} scenario, Ethiopia is projected to reach between {forecast[-1]}% account ownership by 2027.")

    # Data download
    st.download_button("Download Data", df.to_csv().encode("utf-8"),
                       "ethiopia_fi_data.csv", "text/csv")
