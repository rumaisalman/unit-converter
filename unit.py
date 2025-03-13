import streamlit as st

st.set_page_config(page_title="Unit Converter🌡")
st.title("Unit Converter🌡")
st.markdown("## Welcome to the Unit Converter!")
st.markdown("#### An app that converts length, temperature, weight, and time instantly.")

# Select category
category = st.selectbox("Choose a category", ("length", "temperature", "weight", "time"))

# Define conversion function
def convert_units(category, value, unit):
    if category == "length":
        if unit == "kilometer to meter":
            return value * 1000
        elif unit == "meter to kilometer":
            return value / 1000
        elif unit == "kilometer to centimeter":
            return value * 100000
        elif unit == "meter to centimeter":
            return value * 100
        elif unit == "meter to millimeter":
            return value * 1000
        elif unit == "centimeter to meter":
            return value / 100
        elif unit == "millimeter to meter":
            return value / 1000
        elif unit == "centimeter to kilometer":
            return value / 100000
        elif unit == "millimeter to kilometer":
            return value / 1000000

    elif category == "temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    elif category == "weight":
        if unit == "kilogram to gram":
            return value * 1000
        elif unit == "kilogram to milligram":
            return value * 1_000_000
        elif unit == "kilogram to metric ton":
            return value / 1000
        elif unit == "gram to kilogram":
            return value / 1000
        elif unit == "milligram to kilogram":
            return value / 1_000_000
        elif unit == "metric ton to kilogram":
            return value * 1000
        elif unit == "pound to ounce":
            return value * 16
        elif unit == "ounce to pound":
            return value / 16
        elif unit == "ton to pound":
            return value * 2000
        elif unit == "pound to ton":
            return value / 2000
        elif unit == "kilogram to pound":
            return value * 2.20462
        elif unit == "pound to kilogram":
            return value / 2.20462
        elif unit == "gram to ounce":
            return value * 0.035274
        elif unit == "ounce to gram":
            return value / 0.035274
        elif unit == "metric ton to ton":
            return value * 1.10231
        elif unit == "ton to metric ton":
            return value / 1.10231

    elif category == "time":
        if unit == "second to millisecond":
            return value * 1000
        elif unit == "millisecond to second":
            return value / 1000
        elif unit == "second to minute":
            return value / 60
        elif unit == "minute to second":
            return value * 60
        elif unit == "minute to hour":
            return value / 60
        elif unit == "hour to minute":
            return value * 60
        elif unit == "hour to day":
            return value / 24
        elif unit == "day to hour":
            return value * 24
        elif unit == "day to week":
            return value / 7
        elif unit == "week to day":
            return value * 7
        elif unit == "week to month":
            return value / 4.345
        elif unit == "month to week":
            return value * 4.345
        elif unit == "month to year":
            return value / 12
        elif unit == "year to month":
            return value * 12
        elif unit == "year to decade":
            return value / 10
        elif unit == "decade to year":
            return value * 10
        elif unit == "year to century":
            return value / 100
        elif unit == "century to year":
            return value * 100

    return "Invalid conversion"  # Handles cases where no match is found

# Select unit based on category
if category == "length":
    unit = st.selectbox("Select to convert", [
        "kilometer to meter", "meter to kilometer", "kilometer to centimeter",
        "meter to centimeter", "meter to millimeter", "centimeter to meter",
        "millimeter to meter", "centimeter to kilometer", "millimeter to kilometer"
    ])

elif category == "temperature":
    unit = st.selectbox("Choose to convert", [
        "Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius",
        "Fahrenheit to Kelvin", "Kelvin to Celsius", "Kelvin to Fahrenheit"
    ])

elif category == "weight":
    unit = st.selectbox("Choose to convert", [
        "kilogram to gram", "kilogram to milligram", "kilogram to metric ton",
        "gram to kilogram", "milligram to kilogram", "metric ton to kilogram",
        "pound to ounce", "ounce to pound", "ton to pound", "pound to ton",
        "metric ton to ton", "ton to metric ton"
    ])

elif category == "time":
    unit = st.selectbox("Choose to convert", [
        "second to millisecond", "millisecond to second", "second to minute",
        "minute to second", "minute to hour", "hour to minute", "hour to day",
        "day to hour", "day to week", "week to day", "week to month",
        "month to week", "month to year", "year to month", "year to decade",
        "decade to year", "year to century", "century to year"
    ])

# Get user input
value = st.number_input("Enter the value to convert.", min_value=0.0, format="%.2f")

# Convert and display result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
