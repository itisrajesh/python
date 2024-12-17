from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    if request.method == 'POST':
        location = request.form.get('location')

        return redirect(url_for('summary', location=location))
    return render_template('home.html')


@app.route('/summary', methods=['GET'], endpoint='summary')
def summary():
    location = request.args.get('location')
    if location is None or location == '':
        return redirect(url_for('index'))

    df = pd.read_csv(location)
    return render_template("getdetails.html", df=df)


if __name__ == '__main__':
    app.run(debug=True, port=5505)
