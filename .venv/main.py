# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This renders the index.html file from the templates folder
    return render_template('index.html')

if __name__ == '__main__':
    # Start the Flask app on port 5001 in debug mode
    app.run(debug=True, port=5001)
