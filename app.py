from flask import Flask
from flask import request
from flask import render_template
import joblib

app=Flask(__name__)

#Logic is written Here
@app.route('/')
def base():
    return render_template('home.html')


@app.route('/predict', methods=['post'])
def predict():

    model=joblib.load('diabetic_80.pkl')
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    
    output=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if output==0:
        data= ["YAYAYYA","kajd"]
    else:
        data= ["YAYAYYA","kajd"]


    return render_template('predict.html',data=data)

if __name__== "__mai__":
    app.run(debug=True)


