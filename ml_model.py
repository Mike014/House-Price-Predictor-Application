from sklearn.linear_model import LinearRegression
import numpy as np

class MLModel:
    def __init__(self):
        # Initialize the linear regression model
        self.model = LinearRegression()

    def _is_numeric(self, value):
        # Check if a value can be converted to a number
        try:
            float(value)
            return True
        except ValueError:
            return False

    def train(self, features, targets):
        # Ensure all features and targets are numeric and train the model
        if not all(self._is_numeric(f) for f in features) or not all(self._is_numeric(t) for t in targets):
            raise ValueError("Error: Features and targets must be numeric.")
        
        # Convert to NumPy arrays and reshape for the model
        numeric_features = np.array(features, dtype=float).reshape(-1, 1)
        numeric_targets = np.array(targets, dtype=float)
        
        # Train the model
        self.model.fit(numeric_features, numeric_targets)

    def predict(self, feature):
        # Ensure the feature is numeric and make a prediction
        if not self._is_numeric(feature):
            raise ValueError("Error: Feature must be numeric.")
        
        # Convert to NumPy array and reshape for the model
        numeric_feature = np.array([float(feature)]).reshape(-1, 1)
        
        # Return the prediction
        return self.model.predict(numeric_feature)[0]

# Features are input data for predictions; targets are the actual values to predict.
# The train method checks numeric values, converts them to NumPy arrays, and trains the model.
# The predict method checks the feature, converts it, and returns the prediction.
# The _is_numeric method checks if a value can be converted to a number.
# The MLModel class uses scikit-learn's LinearRegression for linear regression.
# Linear regression models the relationship between a dependent variable and independent variables, predicting continuous values.

if __name__ == '__main__':
    model = MLModel()
    try:
        # Example data: sizes of houses in square meters
        features = [50, 60, 70, 80, 90, 100]
        # Corresponding prices in thousands of euros
        targets = [150, 180, 210, 240, 270, 300]
        
        # Train the model with the provided features and targets
        model.train(features, targets)
        
        # Make predictions for new house sizes
        new_features = [55, 65, 75, 85, 95]
        predictions = [model.predict(x) for x in new_features]
        
        # Print the predictions
        for size, price in zip(new_features, predictions):
            print(f"Predicted price for a house of {size} square meters: {price:.2f} thousand euros")
    except ValueError as e:
        print(e)
    except AssertionError as e:
        print(e)
