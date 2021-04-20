from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
import import_ipynb
import mission_to_mars.ipynb

# Create an instance of Flask
app = Flask(__name__)








if __name__ == "__main__":
    app.run(debug=True)