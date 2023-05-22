# Importing libraries
from flask import Flask, jsonify, render_template, request
from keras.models import load_model
from PIL import Image
import numpy as np
import os
import io

# OS Environment
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Setting up Flask Application
app = Flask(__name__,static_folder='Static')

# Loading model to backend 
print("Checking backend Garbage Classifier Model")
model_filename = (os.path.join(os.getcwd(),'model','Garbage1.h5'))
print(model_filename)
model = load_model(model_filename)

# Routing Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Routing Classify page
@app.route('/classify')
def classify():
    return render_template('classify.html')

# Backend Model prediction using api
@app.route('/predict', methods=['POST'])
def predict():
    print(request.form)
    img = request.files['file'].read()
    img = Image.open(io.BytesIO(img))
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)[0]
    class_idx = np.argmax(pred)
    class_names = ['Cardboard','Glass','Metal','paper','Plastic','Trash']
    predicted_class = class_names[class_idx]
    return jsonify({'class': predicted_class})

# Routing Team page
@app.route('/team')
def team():
    return render_template('team.html')

# Routing About page
@app.route('/about')
def about():
    return render_template('about.html')

# Running Flask Application in ip address = 127.0.0.1 port = 5000
if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 5000, debug = False)