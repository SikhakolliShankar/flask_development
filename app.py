from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) 

# sqlalchemy configuration 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def  __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
@app.route('/', methods=['GET', 'POST'])
def htmlfile():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)                                        # Add a Todo
        db.session.commit()                                         # Commit all Todos
        
    allTodo = Todo.query.all()                                  # Query records
    return render_template("index.html",allTodos=allTodo)

# Show all Todos
@app.route('/show')
def showtodos():
    allTodo = Todo.query.all()
    print(allTodo)
    return "Showing Todos"

@app.route('/update/<int:sno>')
def update():
    allTodo = Todo.query.all()
    print(allTodo)
    return "Showing Todos"

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)