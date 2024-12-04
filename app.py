from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return "Hello, World!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
