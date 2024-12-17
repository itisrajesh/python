from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import urlencode

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    else:
        data = {
            'name': request.form.get('name'),
            'feedback': request.form.get('feedback'),
            'comments': request.form.get('comments'),
            'subscribe': request.form.get('subscribe')
        }
        query_string = urlencode(data)
        return redirect(url_for('result') + '?' + query_string)


@app.route('/result')
def result():
    # print(type(request.args))
    data = request.args.to_dict()
    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
