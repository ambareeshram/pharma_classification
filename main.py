from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')


@app.route('/predict' , methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        result = [' no_disease', ' cirrhosis', ' hepatitis', ' fibrosis', 'suspect_disease']
        file = open('model.pkl', 'rb')
        model = pickle.load(file)

        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        albumin =float( request.form.get('albumin'))
        alkaline = float(request.form.get('alkaline'))
        alanine =float( request.form.get('alanine'))
        aspartate =float( request.form.get('aspartate'))
        bilirubin =float( request.form.get('bilirubin'))
        cholinesterase =float( request.form.get('cholinesterase'))
        cholestrol =float( request.form.get('cholestrol'))
        creatinina =float( request.form.get('creatinina'))
        gamma =float( request.form.get('gamma'))
        protein =float( request.form.get('protein'))

        main_dict = {}
        main_dict['age'] = age
        main_dict['gender'] = gender
        main_dict['albumin'] = albumin
        main_dict['alkaline'] = alkaline
        main_dict['alanine'] = alanine
        main_dict['aspartate'] = aspartate
        main_dict['bilirubin'] = bilirubin
        main_dict['cholinesterase'] = cholinesterase
        main_dict['cholestrol'] = cholestrol
        main_dict['creatinina'] = creatinina
        main_dict['gamma'] = gamma
        main_dict['protein'] = protein
        y_pred = model.predict([[age,0,albumin,alkaline,alanine,aspartate,bilirubin,cholinesterase,cholestrol,creatinina,gamma,protein]])
        result_last = result[y_pred[0]] 
        return render_template('output.html',value = result_last ,dicts = main_dict)

if __name__ == '__main__':
    app.run(debug=True)