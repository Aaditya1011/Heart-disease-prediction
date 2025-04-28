from flask import Flask,render_template,request,session
import numpy as np
import pickle 
import preprocessor

app = Flask(__name__)

# loading model and scaler.
model = pickle.load(open('models/model2.pkl','rb'))
scaler = pickle.load(open('models/scaler2.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    # get data from user.
    data1 = [
        float(request.form['age']),
        int(request.form['sex']),
        int(request.form['fbs']),
        float(request.form['hr']),
        int(request.form['exang']),
        float(request.form['op'])
    ]

    # process and append to first one.
    data2= [
        int(request.form['cp']),
        int(request.form['ecg']),
        int(request.form['st']),
        float(request.form['chl']),
        float(request.form['bp'])   
    ]

    '''
    columns_name = ['Age', 'Sex', 'FastingBS', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ASY',
       'ATA', 'NAP', 'TA', 'LVH', 'Normal', 'ST', 'Down', 'Flat', 'Up',
       '(27.95, 31.267]', '(31.267, 34.533]', '(34.533, 37.8]',
       '(37.8, 41.067]', '(41.067, 44.333]', '(44.333, 47.6]',
       '(47.6, 50.867]', '(50.867, 54.133]', '(54.133, 57.4]',
       '(57.4, 60.667]', '(60.667, 63.933]', '(63.933, 67.2]',
       '(67.2, 70.467]', '(70.467, 73.733]', '(73.733, 77.0]', 'n_Cholesterol',
       'low', 'normal', 'above normal', 'risk', 'high risk']
       ['op*2','riskop']
    '''

    # preprocessing.
    processed_data = preprocessor.preprocess(data1,data2)

    # reshaping.
    dataArr = np.array(processed_data).reshape(1,-1)
    
    # scaling.
    scaled_data = scaler.transform(dataArr)

    # prediction.
    prediction = model.predict_proba(scaled_data)

    # custom threshold.
    if prediction[0][1] > 0.4:
        data = 1
    else:
        data = 0

    return render_template('index.html',data=data)
    

if __name__ == "__main__":
    app.run(debug=True)


