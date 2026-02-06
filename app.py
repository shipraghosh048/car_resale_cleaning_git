import streamlit as st
import pandas as pd

st.set_page_config(page_title="Car Resale Analysis", layout="wide")

st.title("🚗 Car Resale Price Analysis")
st.write("Cleaned dataset preview")

# Load data
df = pd.read_csv("car_resale_cleaned_data.csv")
st.write(df.columns)


# Show data
st.subheader("📄 Dataset Preview")
st.dataframe(df.head(20))

# Basic info
st.subheader("📊 Dataset Info")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

st.subheader("🔍 Filter by City")

city_columns = [
    "city_Bangalore", "city_Chennai", "city_Delhi", "city_Gurgaon",
    "city_Hyderabad", "city_Jaipur", "city_Kolkata",
    "city_Mumbai", "city_Pune", "city_Other"
]

selected_city = st.selectbox(
    "Select City",
    [c.replace("city_", "") for c in city_columns]
)

city_col = "city_" + selected_city

filtered_df = df[df[city_col] == 1]

st.subheader("📈 KM Driven vs Resale Price")

plt.figure()
plt.scatter(filtered_df["kms_driven"], filtered_df["resale_price"])
plt.xlabel("KMs Driven")
plt.ylabel("Resale Price")
plt.title(f"KMs Driven vs Resale Price ({selected_city})")

st.pyplot(plt)


st.subheader("📈 KM Driven vs Resale Price")

plt.figure()
plt.scatter(filtered_df["kms_driven"], filtered_df["resale_price"])
plt.xlabel("KMs Driven")
plt.ylabel("Resale Price")
plt.title(f"KMs Driven vs Resale Price ({selected_city})")


st.pyplot(plt)

