

---

# Ice Cream Sales Prediction App

This project is a **Streamlit** application that predicts ice cream sales based on temperature. The app uses a machine learning model to predict revenue based on user input.

## Features

- **Data Upload**: Loads ice cream sales data from a CSV file.
- **User Input**: Allows users to input temperature via a sidebar slider.
- **Data Overview**: Displays an overview of the ice cream data.
- **Scatter Plot**: Visualizes the relationship between temperature and revenue.
- **Prediction**: Uses a Decision Tree Regressor to predict sales based on temperature.

## Libraries Used

- `streamlit`: To build the web interface.
- `numpy`: For numerical computations.
- `pandas`: To handle and process data.
- `matplotlib`: For plotting graphs.
- `scikit-learn`: For training and testing the machine learning model.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/suryakant0111/Ice-Cream-Revenue-Prediction-/tree/main
   ```
   
2. Navigate to the project directory:
   ```bash
   cd ice-cream-sales-prediction
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the provided URL in your browser to interact with the app.

## Usage

1. Upload a CSV file containing ice cream sales data.
2. Use the slider in the sidebar to input the temperature.
3. The app will display an overview of the data and generate a scatter plot of temperature vs revenue.
4. The app will predict sales based on the selected temperature.

## Example Data Format

The CSV file should contain columns similar to the following:
```
Temperature, Revenue
20, 100
25, 150
30, 200
...
```

## License

This project is licensed under the MIT License.

---

