import joblib
from flask import Flask, render_template, request

# Load the pickled model file
model = joblib.load('/home/sai9t/Desktop/IW/model.pkl')

# Load the trained ML model
model = joblib.dump(model, '/home/sai9t/Desktop/IW/model.pkl4' , protocol=4 )

# Create a Flask app
app = Flask(__name__)

# Define a route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request is a POST request, then make a prediction
    if request.method == 'POST':
        # Get the email from the request
        email = request.form['email']

        # Make a prediction
        prediction = model.predict([email])[0]

        # Display the prediction to the user
        if prediction == 1:
            prediction_text = 'Phishing'
        else:
            prediction_text = 'Not Phishing'

        return render_template('index.html', prediction=prediction_text)

    # Otherwise, just render the main page
    else:
        return render_template('index.html')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

