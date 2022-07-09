from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('rfcmodel.pkl','rb'))
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route("/predict",methods = ["POST"])
def predict():
    features = request.form.values()
    float_features = []


    for i in features:
        float_features.append(float(i))


    features = [np.array(float_features)]
    pred = model.predict(features)
    if pred == 0:
        pred = "Phishing"
    else:
        pred = "Safe"

    return render_template('index.html',prediction_text = "The website is {}".format(pred))


if __name__ == '__main__':
    app.run()
