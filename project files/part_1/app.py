from flask import Flask
app = Flask(__name__)

def tasks():
    return '1-Complete Project 2-FYP Report 3-Do Gym'

@app.route('/faizan_todoapp/api/v1.0/tasks',
           methods=['GET'])
def faizan_todo_tasks():
    return tasks()


if __name__ == "__main__":
    app.run(debug=True,port=8080)