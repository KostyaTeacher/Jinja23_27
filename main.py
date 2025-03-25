from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.get("/test1/")
def test1():
    time_now = datetime.datetime.now()
    return render_template("test1.html",
                           title="Flask",
                           time=time_now)

@app.get("/")
def index():
    username = "Олександр"
    age = 20
    hobbies = ["Програмування", "Музика", "Спорт"]
    return render_template("index2.html",
                           name=username,
                           age=age,
                           hobbies=hobbies)

@app.get('/todos/')
def todos():
    tasks = [
        {"name": "Вивчити Flask", "completed": True},
        {"name": "Зрозуміти Jinja2", "completed": False},
        {"name": "Зробити домашнє завдання", "completed": False}
    ]
    return render_template('todos.html', tasks=tasks)




@app.get('/z/')
def todos():
    tasks = [
        {"name": "z", "completed": True},
        {"name": "Зрозуміти z", "completed": False},
        {"name": "Зробити домашнє завдання", "z": False}
    ]
    return render_template('todos.html', tasks=tasks)




if __name__ == '__main__':
    app.run(port=5556, debug=True)

