from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Task: {self.id}'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        try:
            if request.form['content']:
                task_content = request.form['content']
            else:
                raise Exception
            new_task = Todo(content=task_content)
            db.session.add(new_task)
            db.session.commit()
        except Exception as e:
            print(f'Не удалось добавить задачу в базу данных, {e}')

    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
    except Exception as e:
        print(f'Не удалось удалить задачу из базы данных, {e}')
    return redirect('/')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        try:
            if request.form['content']:
                task_to_update.content = request.form['content']
                db.session.commit()
            else:
                raise Exception
        except Exception as e:
            print(f'Не удалось обновить задачу, {e}')
        return redirect('/')
    return render_template('update.html', task=task_to_update)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
