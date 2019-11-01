from flask import Flask, render_template, request, redirect, url_for
from wtforms import TextField
from flask_wtf import Form
from pymongo import MongoClient
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:')
    message = TextField('Message')

@app.route("/", methods=['GET'])
def hello():
    form = ReusableForm()
    
    res = ''
    for entry in log.find():
        print(entry)
        res += entry['name'] + ': ' + entry['text'] + '\n'

    return render_template('index.html', 
        title = 'Chat log',
        log = res,
        form = form)

@app.route("/", methods=['POST'])
def hello_post():
    name = request.form['name']
    message = request.form['message']
    log.insert_one({'name': name, 'text': message})
    return redirect(url_for('hello'))


if __name__ == "__main__":
    client = MongoClient(port=27017, replicaSet='rs0')
    log = client.chat.log
    app.run(host='0.0.0.0', port=80)
