from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# MongoDB connection
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_uri = os.getenv('MONGODB_URI')

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client.shop_db
products_collection = db['products']

@app.route('/')
def home():
    return render_template('home.html')

# Products page route
@app.route('/products')
def products():
    # Retrieve products from MongoDB
    products = list(products_collection.find())
    return render_template('products.html', products=products)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)