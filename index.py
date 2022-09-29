# Ejercicio de youtube https://www.youtube.com/watch?v=V9VU1g4IWlg

from distutils.command.config import config
import sqlite3
from flask import Flask, render_template, redirect, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy #De esta forma se importa el sqlalchemy despues de instalar el modulo a travez del pip

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/task.db'
db = SQLAlchemy(app) #Aqui esta diciendo que le mete la app a alchemy y que esto va a quedar guardado en una variable llamada db

#IMPORTANTE, se necesita crear una clase para poder crear un modelado de datos
class Task (db.Model):
    llave = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256))
    done = db.Column(db.Boolean)

@app.route('/')
def home(): # Esta funcion retorna algo al navegador
    tareas = Task.query.all()
    return render_template('index.html', lista_tareas=tareas)
#Como esta es una conexion a base de datos se necesita un DRIVER para python, y hay muchos para sqlite
#y ese es el ALCHEMY

@app.route('/create-task', methods=['POST']) # Aqui lo que vamos a hacer es mandar este dato del form y mandarlo a la clase
def create(): 
    task = Task(content=request.form['contenido'], done=False)
    db.session.add(task) #Aqui se le agrega el task hacia la base de datos
    db.session.commit()
    return redirect('/')
    
#@app.route('/about')
#def about():
#    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)