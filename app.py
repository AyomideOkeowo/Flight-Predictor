# cretae the flask api
from flask import Flask, render_template, request
import pandas as pd
import pickle
from datetime import datetime

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 1. Extract inputs from form
        airline = request.form['airline']
        source = request.form['Source']
        destination = request.form['Destination']
        total_stops = int(request.form['stops'])

        dep_time = request.form['Dep_Time']
        arrival_time = request.form['Arrival_Time']

        # 2. Convert time strings to datetime
        dep_time = datetime.strptime(dep_time, "%Y-%m-%dT%H:%M")
        arrival_time = datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M")

        # 3. Extract features from datetime
        Journey_day = dep_time.day
        Journey_month = dep_time.month
        Dep_hour = dep_time.hour
        Dep_min = dep_time.minute
        Arrival_hour = arrival_time.hour
        Arrival_min = arrival_time.minute
        Duration_hours = abs(Arrival_hour - Dep_hour)
        Duration_mins = abs(Arrival_min - Dep_min)

        # 4. Construct input DataFrame
        input_dict = {
            'Airline': [airline],
            'Source': [source],
            'Destination': [destination],
            'Total_Stops': [total_stops],
            'Journey_day': [Journey_day],
            'Journey_month': [Journey_month],
            'Dep_hour': [Dep_hour],
            'Dep_min': [Dep_min],
            'Arrival_hour': [Arrival_hour],
            'Arrival_min': [Arrival_min],
            'Duration_hours': [Duration_hours],
            'Duration_mins': [Duration_mins]
        }

        input_df = pd.DataFrame(input_dict)

        # 5. One-hot encoding to match training format
        deploy_df = pd.read_csv("deploy_df")
        X = deploy_df.drop(['Unnamed: 0', 'Price'], axis=1)

        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=X.columns, fill_value=0)

        # 6. Predict
        prediction = model.predict(input_df)[0]

        return render_template("index.html", prediction_text=f"Predicted Flight Price: {int(prediction):,}")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)