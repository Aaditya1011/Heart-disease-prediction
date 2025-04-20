Heart Disease Predition Model.

This project is a Heart Disease Predition Model built using the Logistic Regression model from the scikit-learn library. It predicts about a person having heart disease on the basis of the inputs like age, gender, bp, cholesterol etc. The model achieves an accuracy of 87%.

Features
Data Preprocessing:

1. Some features like age, cholesterol and bp are converted to categorical values for better patter recognition.
2. Scaling the features using StandaedScaler from Scikit-learn.

Model:
The classification model is built using the Logistic Regression Model from Scikit-learn.

Accuracy:
The model has an accuracy of 87% on the test dataset.

Deployment:
The model is deployed using Flask, a web application framework, allowing for easy interaction and testing of the model via a user-friendly interface.

Requirements:
To run the project, you will need to have the following Python libraries installed:
Scikit-learn: For the Logistic Regression Model.
Flask: For building web server.
pandas: For handling the dataset.
numpy: For numerical operations.

1. You can install the required libraries by running :

pip install scikit-learn flask pandas numpy

2. Installation and Setup :

Clone the repository:
git clone https://github.com/Aaditya1011/Heart-disease-prediction.git


Install the dependencies :
pip install -r requirements.txt

In the terminal, Run the Flask app :
flask run 

This will launch a web interface in your default browser, where you can input data to Predict Heart Disease.
On the interface, enter the details and press the "predict" button.
The model will return its prediction about the data, whether it detected heart disease or not.

Project Structure:

heart-disease-prediction/
│
├── data/
│   └── heart.csv           # dataset.
├── models/
│   ├── model.pkl           # Pretrained logistic regression model.
│   └── scaler.pkl          # scaler model.
├── notebook/
│   └── heart-disease.ipynb # jupyter notebook.
├── static/
│   ├── image.jpg           # background image.
│   └── style.css           # css file.
├── templates/
│   └── index.html          # html file.
├── app.py                  # flask app for deploying the model.
├── preprocessor.py         # python file for preprocessing.
├── requirements.txt        # List of required Python libraries.
└── README.md               # This file


Model Performance
Accuracy: 87% on the test set.
Precision and Recall: High scores for both classes, making the model reliable for spam detection in real-world applications.
Contributing
Feel free to fork the repository and contribute to this project. If you encounter any issues or have suggestions for improvements, open an issue or submit a pull request.

License
This project is open-source and available under the MIT License.

