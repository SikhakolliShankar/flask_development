from flask import Flask, render_template
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
    
@app.route('/')
def htmlfile():
    todo = Todo(title="First Todo", desc="Invest on time")
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
    
if __name__ == '__main__':
    app.run(debug=True)