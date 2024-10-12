from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://nkreddy4312:pZxUG3qxFycc3RpJ@cluster0.spq8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['shop_db']
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