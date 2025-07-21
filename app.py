import streamlit as st
import numpy as np

# Title
st.title("💸 Financial Scenario Simulator - What-If Analysis")
st.markdown("This app dynamically calculates WACC and NPV based on your inputs.")

st.sidebar.header("📊 Input Parameters")

# Sidebar Inputs
with st.sidebar:
    equity = st.number_input("Equity ($)", value=600000)
    debt = st.number_input("Debt ($)", value=400000)
    cost_of_equity = st.slider("Cost of Equity (%)", min_value=0.0, max_value=20.0, value=12.0) / 100
    cost_of_debt = st.slider("Cost of Debt (%)", min_value=0.0, max_value=15.0, value=7.0) / 100
    tax_rate = st.slider("Tax Rate (%)", min_value=0.0, max_value=50.0, value=25.0) / 100
    initial_investment = st.number_input("Initial Investment ($)", value=800000)
    project_duration = st.slider("Project Duration (Years)", 1, 10, 5)
    discount_rate = st.slider("Discount Rate (%)", min_value=0.0, max_value=20.0, value=10.0) / 100

    st.markdown("---")
    st.markdown("### Annual Cash Flows")
    cash_flows = []
    for year in range(1, project_duration + 1):
        cash = st.number_input(f"Year {year} Cash Flow ($)", value=150000 + (year - 1) * 15000)
        cash_flows.append(cash)

# Calculate WACC
if equity + debt > 0:
    wacc = (equity / (equity + debt)) * cost_of_equity + \
           (debt / (equity + debt)) * cost_of_debt * (1 - tax_rate)
else:
    wacc = 0.0

# Calculate NPV
npv = -initial_investment
for t, cf in enumerate(cash_flows, start=1):
    npv += cf / ((1 + discount_rate) ** t)

# Display Results
st.subheader("📈 Results")
st.metric("WACC", f"{wacc*100:.2f}%")
st.metric("NPV", f"${npv:,.2f}")

# Optional commentary (simulated without GROQ)
st.markdown("---")
st.subheader("🧠 Investment Insight")
if npv > 0 and wacc < 0.1:
    st.success("✅ This project is financially viable: Positive NPV and low WACC.")
elif npv > 0:
    st.warning("⚠️ Project NPV is positive, but WACC is relatively high. Reassess financing mix.")
else:
    st.error("❌ NPV is negative. This project may not be a good investment under current assumptions.")
