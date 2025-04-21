import streamlit as st

st.title("Global Unit Converter")
st.markdown("Convert various units of measurement, including length, weight, temperature, and volume.")

category = st.selectbox("Choose a  Category",["Volume","Area","Speed","Time","Length","Weight","Temperature"])

def convert_units (category,value,unit):

    if category == "Volume":
        if unit == "Liters to milliliters":
            return value * 1000
        elif unit == "Milliliters to liters":
            return value / 1000
        elif unit == "Liters to gallons":
            return value * 0.264172
        elif unit == "Gallons to liters":
            return value / 0.264172

    if category == "Length":
        if unit == "Meters to kilometers":
            return value / 1000
        elif unit == "Kilometers to meters":
            return value * 1000
        elif unit == "Inches to miles":
            return value / 63360
        elif unit == "Miles to inches":
            return value * 63360
        elif unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to grams":
            return value * 1000
        elif unit == "Grams to kilograms":
            return value / 1000
        elif unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        elif unit == "Ounces to grams":
            return value * 28.3495
        elif unit == "Grams to ounces":
            return value / 28.3495

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15

    elif category == "Area":
        if unit == "Square meters to square feet":
            return value * 10.7639
        elif unit == "Square feet to square meters":
            return value / 10.7639
        elif unit == "Acres to square meters":
            return value * 4046.86
        elif unit == "Square meters to acres":
            return value / 4046.86

    elif category == "Speed":
        if unit == "Meters per second to kilometers per hour":
            return value * 3.6
        elif unit == "Kilometers per hour to meters per second":
            return value / 3.6
        elif unit == "Miles per hour to kilometers per hour":
            return value * 1.60934
        elif unit == "Kilometers per hour to miles per hour":
            return value / 1.60934

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    else:
        return "Invalid category or unit"

# UI continuation (based on category)
unit_options = {
    "Volume": ["Liters to milliliters", "Milliliters to liters", "Liters to gallons", "Gallons to liters"],
    "Length": ["Meters to kilometers", "Kilometers to meters", "Inches to miles", "Miles to inches", "Kilometers to miles", "Miles to kilometers"],
    "Weight": ["Kilograms to grams", "Grams to kilograms", "Kilograms to pounds", "Pounds to kilograms", "Ounces to grams", "Grams to ounces"],
    "Temperature": ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"],
    "Area": ["Square meters to square feet", "Square feet to square meters", "Acres to square meters", "Square meters to acres"],
    "Speed": ["Meters per second to kilometers per hour", "Kilometers per hour to meters per second", "Miles per hour to kilometers per hour", "Kilometers per hour to miles per hour"],
    "Time": ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"]
}

unit = st.selectbox("Choose Conversion Type", unit_options[category])

value = st.number_input("Enter value to convert:", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"Converted Value: {result}")
