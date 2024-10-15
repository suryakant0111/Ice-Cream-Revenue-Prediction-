import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Load data
@st.cache_data
def load_data():
    IceCreamData = pd.read_csv('IceCreamData.csv')
    return IceCreamData

data = load_data()

# Sidebar for input
st.sidebar.header("User Input Parameters")
temp_input = st.sidebar.slider("Select Temperature (°C):", min_value=0, max_value=50, value=30)

# Display title and data
st.title("Ice Cream Sales Prediction")
st.write("## Ice Cream Data Overview")
st.dataframe(data.head())

# Scatter plot
st.write("### Scatter Plot: Temperature vs Revenue")
col1, col2 = st.columns(2)

with col1:
    st.write("Temperature (°C) vs Revenue")
    fig, ax = plt.subplots()
    ax.scatter(data['Temperature'], data['Revenue'], color='blue', alpha=0.6)
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Revenue')
    ax.set_title('Scatter Plot')
    st.pyplot(fig)

# Model Training
x = data['Temperature'].values.reshape((-1, 1))
y = data['Revenue'].values.reshape((-1, 1))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=2022)

dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)

# Display R² score
r2 = r2_score(y_test, y_pred)
with col2:
    st.write(f"### Model Accuracy (R² Score): **{r2 * 100:.2f}%**")

# Prediction plot
st.write("### Model Prediction Visualization")
fig2, ax2 = plt.subplots()
x_sorted = np.sort(x, axis=0)
ax2.plot(x_sorted, dt.predict(x_sorted), color='red', label="Model Prediction")
ax2.scatter(x, y, alpha=0.6, label="Actual Data")
ax2.set_xlabel('Temperature (°C)')
ax2.set_ylabel('Revenue')
ax2.set_title('Temperature vs Revenue with Model Prediction')
ax2.legend()
st.pyplot(fig2)

# Predict revenue for a given temperature
st.write("### Predict Revenue")
st.write(f"Temperature selected: **{temp_input}°C**")
prediction = dt.predict([[temp_input]])
st.write(f"### Predicted Revenue: **₹{prediction[0]:.2f}**")
