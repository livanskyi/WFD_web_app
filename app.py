from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['login']
        return redirect(f'/user/{username}')
    else:
        return render_template('login.html')


@app.route('/user/<string:username>')
def user(username):
    return 'Welcome, ' + username


if __name__ == '__main__':
    app.run(debug=True)
