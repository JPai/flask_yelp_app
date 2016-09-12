from flask import Flask, render_template, request
from yelp_api import get_businesses
import os

app = Flask(__name__)
term = "restaurant" #assign the term to restaurant

@app.route("/")
def index():
    address = request.values.get('address') #use the get method
    businesses = None
    if address:
        try:
            businesses = get_businesses(term, address)
        except:
            pass
    return render_template('index.html', address=address, businesses=businesses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
