# House Price Predictor Application

## Overview
The House Price Predictor is a Python application that predicts house prices based on their size in square meters. It uses a linear regression model to make predictions and provides a graphical user interface (GUI) for user interaction. The application also includes logging, database management, and concurrency features.

## Components

### 1. Linear Regression Model (`ml_model.py`)
- **MLModel Class**: Utilizes scikit-learn's `LinearRegression` to model the relationship between house sizes (features) and prices (targets).
- **Methods**:
  - `train(features, targets)`: Trains the model using provided features and targets.
  - `predict(feature)`: Predicts the price for a given house size.
  - `_is_numeric(value)`: Checks if a value can be converted to a number.

### 2. Graphical User Interface (`gui.py`)
- **App Class**: Creates a GUI using Tkinter for user interaction.
- **Widgets**:
  - Entry fields for house size and price.
  - Buttons to add data, train the model, and make predictions.
  - Labels to display results and messages.
- **Methods**:
  - `add_data()`: Adds user input data to the database.
  - `train_model()`: Trains the model with data from the database.
  - `predict()`: Predicts the price for a given house size.
  - `run()`: Starts the Tkinter main loop.

### 3. Database Management (`database.py`)
- **Database Class**: Manages SQLite database operations.
- **Methods**:
  - `create_table()`: Creates a table for storing data.
  - `insert_data(feature, target)`: Inserts feature and target data into the table.
  - `fetch_all()`: Retrieves all data from the table.
  - `close()`: Closes the database connection.

### 4. Logging (`logger.py`)
- **Logger**: Configures logging to output messages to both the console and a file (`app.log`).
- **Usage**: Logs information, warnings, and errors throughout the application.

### 5. Concurrency (`concurrency.py`)
- **Concurrency Class**: Manages threading for concurrent execution.
- **Methods**:
  - `start()`: Starts a new thread.
  - `join()`: Waits for the thread to finish.

### 6. Application Initialization (`main.py`)
- **Main Script**: Initializes and runs the `App` class.

### 7. Package Initialization (`__init__.py`)
- **Initialization**: Imports all necessary modules and classes for the package.

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

### Libraries Used

#### 1. Tkinter
- **Purpose**: Provides a graphical user interface (GUI) for user interaction.
- **Usage**: Creating windows, labels, entry fields, buttons, and message boxes.

#### 2. SQLite3
- **Purpose**: Manages a lightweight, disk-based database.
- **Usage**: Storing and retrieving data for training the model.

#### 3. Scikit-learn
- **Purpose**: Provides machine learning tools.
- **Usage**: Implementing the `LinearRegression` model for predicting house prices.

#### 4. NumPy
- **Purpose**: Supports large, multi-dimensional arrays and matrices.
- **Usage**: Converting data to NumPy arrays for model training and prediction.

#### 5. Logging
- **Purpose**: Records events that happen during the execution of the program.
- **Usage**: Logging information, warnings, and errors to both the console and a file (`app.log`).

#### 6. Threading
- **Purpose**: Manages concurrent execution of threads.
- **Usage**: Running tasks in separate threads to improve performance.

#### 7. Messagebox (from Tkinter)
- **Purpose**: Displays message boxes in the GUI.
- **Usage**: Showing information, warnings, and error messages to the user.

#### 8. Dataclasses (Custom Modules)
- **Database**: Manages SQLite database operations.
- **MLModel**: Implements the linear regression model.
- **Concurrency**: Manages threading for concurrent execution.
- **Logger**: Configures and manages logging.
- **App**: Creates and manages the GUI application.

