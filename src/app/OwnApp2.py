import pandas as pd
import streamlit as st

st.title('Number of Nuclear Warheads - USA vs Russia')

"Autor: David Steinhäuser (https://github.com/DavidStein7)"

from scipy.stats import linregress

st.subheader("Vorhersage 1")
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
warheadsR = [12188, 11152, 10114, 9076, 8038, 7000, 6643, 6286, 5929, 5527, 5215, 4858, 4750, 4650, 4600, 4500, 4490, 4300, 4350, 4330, 4310, 4495, 4477]
warheadsU = [10577, 10526, 10457, 10027, 8570, 8360, 7853, 5709, 5273, 5113, 5066, 4897, 4881, 4804, 4717, 4571, 4018, 3822, 3785, 3805, 3750, 3708, 3708]

regression_result = linregress(years, warheadsR)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept
def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result
desired_year = st.number_input('Jahr', value = 2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

"Die Vorhersage"

st.write(prediction_rounded)

"Lineare Vorhersage"
slope = (warheadsR[22]-warheadsR[0])/(years[22]-years[0])
intercept = warheadsR[0]-(slope*years[0])

def model(desired_year):
    model_result2 = slope * desired_year + intercept
    return model_result2

st.write(model(desired_year))

"Daten"

st.write(warheadsR[22])

st.success("nice!")

st.subheader("Data points used:")
chart_data=pd.DataFrame(warheadsR,years)
st.bar_chart(chart_data)

clicked = st.button("Click me",help="Balloons")
if clicked:
    st.balloons()

