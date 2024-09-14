import tkinter as tk
from tkinter import messagebox
from database import Database
from logger import logger
from concurrency import Concurrency
from ml_model import MLModel

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("House Price Predictor")
        self.db = Database()
        self.ml_model = MLModel()
        self.create_widgets()

    def create_widgets(self):
        self.feature_label = tk.Label(self.root, text="House Size (sqm):")
        self.feature_label.pack()
        self.feature_entry = tk.Entry(self.root)
        self.feature_entry.pack()

        self.target_label = tk.Label(self.root, text="Price (thousands of euros):")
        self.target_label.pack()
        self.target_entry = tk.Entry(self.root)
        self.target_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Data", command=self.add_data)
        self.add_button.pack()

        self.train_button = tk.Button(self.root, text="Train Model", command=self.train_model)
        self.train_button.pack()

        self.predict_button = tk.Button(self.root, text="Predict", command=self.predict)
        self.predict_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def add_data(self):
        try:
            feature = float(self.feature_entry.get())
            target = float(self.target_entry.get())
            self.db.insert_data(feature, target)
            logger.info(f"Data added: Feature={feature}, Target={target}")
            messagebox.showinfo("Success", "Data added successfully")
        except ValueError:
            logger.error("Invalid input for feature or target")
            messagebox.showerror("Error", "Invalid input for feature or target")

    def train_model(self):
        data = self.db.fetch_all()
        if data:
            features, targets = zip(*[(row[1], row[2]) for row in data])
            self.ml_model.train(features, targets)
            logger.info("Model trained successfully")
            messagebox.showinfo("Success", "Model trained successfully")
        else:
            logger.warning("No data to train the model")
            messagebox.showwarning("Warning", "No data to train the model")

    def predict(self):
        try:
            feature = float(self.feature_entry.get())
            prediction = self.ml_model.predict(feature)
            self.result_label.config(text=f"Predicted price: {prediction:.2f} thousand euros")
            logger.info(f"Prediction made for feature={feature}: {prediction}")
        except ValueError:
            logger.error("Invalid input for feature")
            messagebox.showerror("Error", "Invalid input for feature")

    def run(self):
        self.root.mainloop()
        self.db.close()
