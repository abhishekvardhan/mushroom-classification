import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('myhtml.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    output=None;
    prediction = model.predict(final_features)

    output = prediction[0]
    if output== None:
        return render_template('myhtml.html', prediction_text="select any option  ")
    if output==0:
        return render_template('myhtml.html', prediction_text="Mushroom is POISONOUS ")
    elif output==1:
        return render_template('myhtml.html', prediction_text="Mushroom is EDABLE ")
    
if __name__ == "__main__":
    app.run(debug=True)