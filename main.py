# Import necessary modules
from flask import Flask, jsonify, request
import csv

# Initialize lists to store articles
all_articles = []
liked_articles = []
not_liked_articles = []

# Read data from CSV file and populate all_articles list
with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

# Create a Flask app instance
app = Flask(__name__)

# Define a route to get the next article
@app.route("/get-article")
def get_article():
    # Return the first article in all_articles list as JSON response
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

# Define a route to mark an article as liked
@app.route("/liked-article", methods=["POST"])
def liked_article():
    # Get the first article in all_articles
    article = all_articles[0]
    
    # Append the article to the liked_articles list
    liked_articles.append(article)
    
    # Remove the article from all_articles
    all_articles.pop(0)

    # Return a success status as JSON response with HTTP status code 201
    return jsonify({
        "status": "success"
    }), 201

# Define a route to mark an article as not liked
@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    # Get the first article in all_articles
    article = all_articles[0]
    
    # Append the article to the not_liked_articles list
    not_liked_articles.append(article)
    
    # Remove the article from all_articles
    all_articles.pop(0)

    # Return a success status as JSON response with HTTP status code 201
    return jsonify({
        "status": "success"
    }), 201

# Run the Flask app if this script is the main entry point
if __name__ == "__main__":
    app.run()
