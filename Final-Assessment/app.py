from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi
import certifi
app = Flask(__name__)

ca = certifi.where()

uri = "mongodb+srv://mikhairochelle:JMoL2Qkw0SOO1scg@cluster0.8vhapfy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, 27017)

db = client.flask_db

todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['priority']
        todos.insert_one({'content': content, 'priority': degree})
        return redirect(url_for('index'))

    
    all_todos = todos.find().collation({'locale': 'en'}).sort('content') # Add this line outside the if block! 
    return render_template('index.html', todos=all_todos) # add todos here!

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)