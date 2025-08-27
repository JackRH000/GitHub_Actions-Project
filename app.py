from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
    def hello():
        return "Hello, Flask!"

# Run the application (for development)
if __name__ == '__main__':
    app.run(debug=True)
