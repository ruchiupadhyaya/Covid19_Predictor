from flask import Flask,render_template,redirect,request

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # return 'hello world'

@app.route('/visualization')
def visualization():
    # return render_template('index.html')
    return 'visualization'
@app.route('/machinelearning')
def machinelearning():
    # return render_template('index.html')
    return 'Machine Learning'

if __name__=='__main__':
    app.run(debug=True)