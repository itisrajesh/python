from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/check-age', methods=['GET', 'POST'])
def check_age():
    if request.method == 'GET':
        return render_template('survey.html')
    else:
        username = request.form.get('username')
        age = int(request.form.get('age'))
        result = 'minor' if age < 18 else 'adult'

        return redirect(url_for('result_page', username=username, result=result))


@app.route('/result-page')
def result_page():
    username = request.args.get('username')
    result = request.args.get('result')
    data = {
        'username': username,
        'result': result
    }

    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
