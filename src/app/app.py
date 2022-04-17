import streamlit as st

st.title("Vorhersage der deutschen CO2 Emissionen")

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]

from scipy.stats import linregress

regression_result = linregress(years, emissions_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept


def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.slider(label="Choose number", min_value=1950, max_value=2050, value=2022, step=1, format=None, disabled=False)

"Die Vorhersage für das Jahr"
st.write(desired_year)
"ist:"
st.write(scipy_model(desired_year))

"Autor Finn Böckenhoff"

st.subheader("Informationen zum Modell und seinen Daten")
"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten der Jahre 2010 bis 2020."
"Es steht ein Datenpunkt pro Jahr zur Verfügung."

"Die Daten stammen aus den folgenden Quellen:"






