from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('survey.html')

    else:
        fake_users = {
            'rajesh': '********',
            'ekka': 'password2',
        }

        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        if fake_users.get(username) == password:
            return redirect(url_for('dashboard', username=username))
        else:
            return '<p>You are restricted</p>'


@app.route('/dashboard')
def dashboard():
    username = request.args.get('username')
    return render_template('result.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
