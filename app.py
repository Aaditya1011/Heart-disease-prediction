from flask import Flask,render_template,request,session,redirect ,url_for
import numpy as np
import pickle 
import preprocessor

app = Flask(__name__)
app.secret_key = 'treoijg34534759'

# loading model and scaler.
model = pickle.load(open('models/model2.pkl','rb'))
scaler = pickle.load(open('models/scaler2.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html',form_data={},data={})
    
@app.route('/predict',methods=['GET','POST'])
def predict():

    if request.method == 'POST':
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


        # session the user data.
        form_data = {
            'age' : request.form.get('age'),
            'sex' : request.form.get('sex'),
            'fbs' : request.form.get('fbs'),
            'hr' : request.form.get('hr'),
            'exang' : request.form.get('exang'),
            'op' : request.form.get('op'),
            'cp' : request.form.get('cp'),
            'ecg' : request.form.get('ecg'),
            'st' : request.form.get('st'),
            'chl' : request.form.get('chl'),
            'bp' : request.form.get('bp'),
            }

        session['form_data'] = form_data


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
        
        # session output.
        session['output'] = data

        return redirect(url_for('predict'))

    # get data from session. 
    form_data = session.get('form_data')
    data = session.get('output')
    return render_template('index.html',form_data=form_data,data=data)
    

if __name__ == "__main__":
    app.run(debug=True)


