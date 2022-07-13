from flask import Flask,render_template
from flask_script import Manager
from settings import DevelopmentConfig

app = Flask(__name__)
manager = Manager(app)

app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/Data-Exploration.html')
def DataExploration():
    return render_template('Data-Exploration.html')



@app.route('/Data-Preparation.html')
def DataPreparation():
    return render_template('Data-Preparation.html')


@app.route('/Evaluation.html')
def Evaluation():
    return render_template('Evaluation.html')


@app.route('/Conclusion.html')
def Conclusion():
    return render_template('Conclusion.html')


@app.route('/Contact.html')
def Contact():
    return render_template('Contact.html')


@app.route('/Introduction.html')
def Introduction():
    return render_template('Introduction.html')



if __name__ == '__main__':
    manager.run(host='0.0.0.0',debug=True)
