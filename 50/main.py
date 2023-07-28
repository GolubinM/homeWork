import sqlite3
import os
from flask import Flask, render_template, request, flash, abort

from database import DataBase

DATABASE = '/tmp/mars.db'
DEBUG = True
SECRET_KEY = "12345678998765431qwerew_qweewq"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update({'DATABASE': os.path.join(app.root_path, 'mars.db')})

menu = [
    {'title': 'Главная', 'url': '/'},
    {'title': '"Я выбираю марс!"', 'url': 'marsplease'},
    {'title': 'Ближайшие проекты', 'url': 'projects'},
    {'title': 'Условия размещения, гарантии', 'url': 'condition'},
    {'title': 'Ближайшие рейсы', 'url': 'flights'},
    {'title': 'Добавить проект', 'url': 'add_projects'},
    {'title': 'Обратная связь', 'url': 'contacts'},
]


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route('/index')
@app.route('/')
def index():
    db_con = connect_db()
    db = DataBase(db_con)

    return render_template("index.html", menu=db.get_menu(), projects=db.get_projects())


@app.route('/add_projects', methods=['GET', 'POST'])
def add_projects():
    db_con = connect_db()
    db = DataBase(db_con)

    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['text']) > 20:
            res = db.add_projects(request.form['title'], request.form['text'], request.form['url'])
            if res:
                flash('Проект добавлено успешно!', category='success')
            else:
                flash('Ошибка добавления проекта!', category='error')
        else:
            flash('Ошибка добавления проекта!', category='error')

    return render_template('add_projects.html', title='Добавление проекта', menu=db.get_menu())


@app.route('/project/<project_id>')
def show_project(project_id):
    db_con = connect_db()
    db = DataBase(db_con)

    project, text = db.get_project(project_id)
    if not project:
        print("Ошибка - not project")
        abort(404)
    return render_template('project.html', proj=project, text=text, menu=db.get_menu())


@app.route('/marsplease')
def marsplease():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template("marsplease.html", menu=db.get_menu())


@app.route('/projects')
def projects():
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template("projects.html", menu=db.get_menu())


@app.route('/condition')
def condition():
    db_con = connect_db()
    db = DataBase(db_con)

    conditions = [
        'Ваш возраст 25-45 лет',
        'Вы не имеете медицинских противопоказаний',
        'Вы готовы разделить все успехи, победы, и результаты труда с командой',
        'До 15% всех выплат по контракту переходит в Фонд Развития Новых миров',
        'Все имущество на Земле передается на хранение компании, до Вашего возвращения на Землю'
    ]
    return render_template("condition.html", menu=db.get_menu(), conditions=conditions)


@app.route('/flights')
def flights():
    db_con = connect_db()
    db = DataBase(db_con)

    flight = [{'flight_date': '2024-12-12', 'free_places': 960},
              {'flight_date': '2025-06-01', 'free_places': 760, 'ticket_class': 1, 'ticket_price': 12000}
              ]
    return render_template("flights.html", title='Дата отправления и количество свободных мест', flight=flight,
                           menu=db.get_menu())


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    db_con = connect_db()
    db = DataBase(db_con)

    if request.method == 'POST':
        return render_template("index.html", menu=db.get_menu())

    return render_template('contacts.html', title='Обратная связь', menu=db.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db_con = connect_db()
    db = DataBase(db_con)
    return render_template('page404.html', title='Страница не найдена', menu=db.get_menu()), 404


if __name__ == '__main__':
    # create_db()
    app.run(port=5001)
