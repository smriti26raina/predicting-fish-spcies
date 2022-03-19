# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 11:45:03 2022

@author: noopa
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app1=Flask(__name__)
pickle_in = open("classifier4.pkl","rb")
classifier=pickle.load(pickle_in)

@app1.route('/')
def home():
    return render_template('index.html')



@app1.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)

    
    return render_template('index.html', prediction_text='The Fish species is {}'.format(prediction))
    
    


if __name__=='__main__':
    app1.run()