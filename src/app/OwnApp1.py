import pandas as pd
import streamlit as st

st.title('Vorhersage des Anteils der erneuerbaren Energien am gesamten Energieverbrauch in Deutschland')

"Autor: David Steinhäuser (https://github.com/DavidStein7)"

from scipy.stats import linregress

st.subheader("Vorhersage")
years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
r_energy = [10.72, 11.61, 12.54, 13.64, 13.63, 14.02, 14.55, 14.24, 15.22, 16.12, 17.17]


regression_result = linregress(years, r_energy)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept
def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result
desired_year = st.number_input('Jahr', value = 2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

"Die Vorhersage des Anteils der erneuerbaren Energien für das ausgewählte Jahr ist"

st.write(prediction_rounded,"%")

"des gesamten Energieverbrauchs."

st.subheader("Genutzte Datenpunkte:")
chart_data=pd.DataFrame(r_energy,years)
st.bar_chart(chart_data)

clicked = st.button("Drück mich! :)",help="Balloons")
if clicked:
    st.balloons()

st.subheader("Über das Modell und Daten")

"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 2009 bis 2019."
"Es steht ein Datenpunkt pro Jahr zur Verfügung"

"Die Daten stammen aus den folgenden Quellen:"
"- IEA. (2021). World Energy Balances."
"- UN Statistics Division. (2021). Energy Balances."
"- https://unstats.un.org/sdgs/dataportal/countryprofiles/DEU#goal-7"