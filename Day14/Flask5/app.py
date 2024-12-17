from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'dsnlnlnlndsnaefnspdnvpaqwnvsdnpszpdvnpn'


@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    session.clear()
    if request.method == 'POST':
        session['productName'] = request.form.get('productName')
        session['quantity'] = request.form.get('quantity')
        return redirect(url_for('shipping'))

    return render_template('home.html')


@app.route('/shipping', methods=['GET', 'POST'], endpoint='shipping')
def shipping():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        session['address'] = request.form.get('address')
        session['contact'] = request.form.get('contact')

        return redirect(url_for('summary'))

    return render_template('shipping.html')


@app.route('/summary', methods=['GET', 'POST'], endpoint='summary')
def shipping():
    if request.method == 'POST':
        confirm = request.form.get('confirmOrder')
        if confirm == 'yes':
            session['confirm'] = confirm
            return redirect(url_for('confirmation'))
        else:
            return """
                <p>Your previous order has been cancelled</p>
                <a href='/'>Go back to home</a>
            """
    data = {
        'name': session['name'],
        'address': session['address'],
        'contact': session['contact'],
        'productName': session['productName'],
        'quantity': session['quantity']
    }

    return render_template('getdetails.html', data=data)


@app.route('/confirmation', methods=['GET'], endpoint='confirmation')
def confirmation():
    if session.get('confirm') == 'yes':
        return render_template('confirmation.html')
    return """
       <p>This is illegal !!!</p>
       <a href='/'>Go back to home</a>
   """


if __name__ == '__main__':
    app.run(debug=True, port=5505)
