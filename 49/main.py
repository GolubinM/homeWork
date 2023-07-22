from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': '"Я выбираю марс!"', 'url': 'marsplease'},
    {'name': 'Условия размещения, гарантии', 'url': 'condition'},
    {'name': 'Ближайшие рейсы', 'url': 'flights'},
    {'name': 'Обратная связь', 'url': 'contacts'},
]


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html", menu=menu)


@app.route('/marsplease')
def marsplease():
    return render_template("marsplease.html", menu=menu)


@app.route('/condition')
def condition():
    conditions = [
        'Ваш возраст 18-35 лет',
        'Вы не имеете медицинских противопоказаний',
        'Вы готовы разделить все успехи, победы, и результаты труда с командой',
        'Вы не имеете незакрытых судимостей и/или не скрываетесь от закона, который считаете справедливым',
        'До 15% всех выплат по контракту переходит в Фонд Развития Новых миров',
        'Все имущество на Земле передается на хранение компании, до Вашего возвращения на Землю'
    ]
    return render_template("condition.html", menu=menu, conditions=conditions)


@app.route('/flights')
def flights():
    flight = [ {'flight_date': '2024-12-12', 'free_places': 960},
        {'flight_date': '2025-06-01', 'free_places': 760, 'ticket_class': 1, 'ticket_price': 12000}
    ]
    return render_template("flights.html", title='Дата отправления и количество свободных мест', flight=flight,
                           menu=menu)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        return render_template("index.html", menu=menu)

    return render_template('contacts.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
