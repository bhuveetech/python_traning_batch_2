#!flask/bin/python
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import (Flask,
    jsonify,
    abort,
    request,
    make_response,
    url_for,
    render_template)
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()


# localhost:5000/
@app.route('/')
def index():
   return render_template("get_task.html", user="TestUser")


@app.route('/get_task_ui', methods=['post'])
def get_task_ui():
    print("task_id")
    task_id = request.form.get("task_id")
    print(type(task_id))
    return get_task(task_id)


@auth.verify_password
def verify_pw(username, password):
    if username == 'testuser' and password == "test":
        return True

    else:
        return False


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == int(task_id)]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
# @auth.login_required
def create_task():
    print("Inside Create Task",request.json)
    if not request.json or not 'title' in request.json:
        abort(400)

    print(type(request.json))
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json.get('title'),
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
# @auth.login_required
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json:
        abort(400)
    if 'description' in request.json:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': get_task(task[0]['id'])})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
# @auth.login_required
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})



if __name__ == '__main__':
    app.run(debug=True)