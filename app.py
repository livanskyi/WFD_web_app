from flask import Flask, render_template, url_for, request, redirect
from models.run_model_detection import run_model_detection
import os
import shutil


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['login']
        return redirect(url_for("user", username=username))
    else:
        return render_template('login.html')


@app.route("/user/<username>")
def user(username):
    return render_template('main.html', username=username)


@app.route('/processing/<username>', methods=['POST'])
def processing(username):
    user_path = __create_path(username)
    __save_uploaded_files(request.files.getlist('user_file'), user_path)

    # TODO configs
    configs = {'threshold': 0.5, 'models': [0,1]}

    result_file = run_model_detection(user_path, configs)
    return redirect(url_for('downloading', username=username, result_file=result_file), code=307)


@app.route('/download/<username>/file=<result_file>', methods=['POST'])
def downloading(username, result_file):
    return render_template('result.html', username=username, result_file=result_file)


def __create_path(username):
    user_path = f'static/files/{username}/'
    if os.path.exists(user_path):
        shutil.rmtree(user_path)
    os.makedirs(user_path)
    return user_path


def __save_uploaded_files(files_list, user_path):
    for user_file in files_list:
        user_file.save(os.path.join(user_path, user_file.filename))


if __name__ == '__main__':
    app.run(debug=True)
