from flask import Flask, render_template, request
import pandas as pd
import joblib


# Your prediction function
def predict_insurance_cost(data):
    # Assume 'gb' is your trained model
    new_pred = gb.predict(data)
    return new_pred

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        bmi = float(request.form['bmi'])
        children = float(request.form['children'])
        smoker = float(request.form['smoker'])
        region = float(request.form['region'])

        # Create a DataFrame with user input
        user_data = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker],
            'region': [region]
        })

        # Use the prediction function
        prediction = predict_insurance_cost(user_data)

        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    # Assuming you have your model loaded (replace 'your_model_file.pkl' with your actual model file)
     gb = joblib.load('model_gb')
    
    # Run the Flask app
app.run(debug=True)
