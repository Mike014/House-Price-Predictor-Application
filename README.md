# House-Price-Predictor-Application
he House Price Predictor is a Python application that predicts house prices based on their size in square meters. It uses a linear regression model to make predictions and provides a graphical user interface (GUI) for user interaction. The application also includes logging, database management, and concurrency features.  

## How to Use
1. **Run the Application**: Execute `main.py` to start the GUI.
2. **Add Data**: Enter house sizes and corresponding prices, then click "Add Data" to store them in the database.
3. **Train the Model**: Click "Train Model" to train the linear regression model with the stored data.
4. **Make Predictions**: Enter a house size and click "Predict" to get the predicted price.

## Concepts Used
- **Linear Regression**: A statistical method to model the relationship between a dependent variable and one or more independent variables. In this application, it is used to predict house prices based on their sizes. The model finds the best-fit line that minimizes the difference between the actual and predicted values.
- **Logging**: Recording events that happen during the execution of the program.
- **Threading**: Running multiple threads (smaller units of a process) concurrently.
- **SQLite Database**: A lightweight, disk-based database to store and manage data.
- **Tkinter**: A standard Python library for creating graphical user interfaces.

This application combines machine learning, GUI development, database management, logging, and concurrency to provide a comprehensive tool for predicting house prices.
