from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



# create route that renders index.html template
@app.route("/")
def index():
    mars_data = mongo.db.mission.find_one()
    return render_template("index.html", data=mars_data)


@app.route("/scrape")
def scraper():
    data = scrape_mars.scrape()
    mongo.db.mission.update({}, data, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)