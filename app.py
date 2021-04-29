from flask import Flask, render_template, request, redirect
from models.todo import Todo, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def home():
    todos = Todo.query.all()
    return render_template('home.html', todos=todos)


@app.route('/add-todo', methods=['GET', 'POST'])
def addTodo():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title, desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('addTodo.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.filter_by(id=id).first()
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('updateTodo.html', todo=todo)


@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=False)
