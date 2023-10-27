# flask, pandas, scit-learn, pickle-mixin
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__, template_folder='template')
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
athlete = pd.read_csv('cleaned_athletee_data.csv')


@app.route('/recommend')
def index():
    age = sorted(athlete['Age'].unique())
    training_hours_per_week = sorted(athlete['Training_Hours_Per_Week'].unique())
    performance_score = sorted(athlete['Performance_Score'].unique())
    vegetables = sorted(athlete['Preference_For_Vegetables'].unique())
    protein = sorted(athlete['Preference_For_Protein'].unique())
    gender = sorted(athlete['Gender'].unique())
    height = sorted(athlete['Height'].unique())
    weight = sorted(athlete['Weight'].unique())
    price = sorted(athlete['Price_in_Kenya_Shillings'].unique())
    complexity = sorted(athlete['Training_Complexity'].unique())
    complexity_range = sorted(athlete['Training_Complexity_Range'].unique())
    return render_template("index.html", Age=age, Training_Hours_Per_Week=training_hours_per_week,
                           Performance_Score=performance_score, Preference_For_Vegetables=vegetables,
                           Preference_For_Protein=protein, Gender=gender, Height=height, Weight=weight,
                           Price_in_Kenya_Shillings=price, Training_Complexity=complexity,
                           Training_Complexity_Range=complexity_range)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form.get('Age'))
        training_hours_per_week = int(request.form.get('training_hours_per_week'))
        performance_score = int(request.form.get('performance_score'))
        vegetables = int(request.form.get('preference_for_vegetables'))
        protein = int(request.form.get('preference_for_protein'))
        gender = request.form.get('Gender')
        height = int(request.form.get('height'))
        weight = int(request.form.get('weight'))
        price = 300
        complexity = request.form.get('complexity')
        complexity_range = 6

        prediction = model.predict(pd.DataFrame(
            [[age, training_hours_per_week, performance_score, vegetables, protein, gender, height, weight, price,
              complexity, complexity_range]],
            columns=['Age', 'Training_Hours_Per_Week', 'Performance_Score', 'Preference_For_Vegetables',
                     'Preference_For_Protein', 'Gender', 'Height', 'Weight', 'Price_in_Kenya_Shillings',
                     'Training_Complexity', 'Training_Complexity_Range']))
        return str(np.round(prediction[0], 2))

    except ValueError as e:
        return str(e)  # Return an error message if conversion fails

    # Route for handling the login page logic


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            print("Redirecting to /recommend")
            return redirect(url_for('index'))
    return render_template('login.html', error=error)




if __name__ == "__main__":
    app.run(debug=True)
