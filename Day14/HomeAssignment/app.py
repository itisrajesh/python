"""
Homework Assignment:
Flask application that allows users to submit data via a web form.
Submitted data should be saved to a CSV file with a hardcoded filename and a confirmation message should be displayed once the data is successfully saved.

Flask implementation:
Use Flask to create a web application with two pages.
Implement routing to handle form submission and display success messages.

CSV File Handling:
Use a hardcoded filename (data.csv) to store the submitted data.
If the CSV file does not exist, create it and include headers (Name, Email).
Append new user data to the CSV file.

User Interface:
Page 1: A form to accept user input (e.g., name and email).
Page 2: A confirmation page displaying a message indicating that the data has been saved successfully, along with the filename
"""

from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

import csv


def save_to_csv(name, email, contact):
    filename = 'userdata.csv'
    success = False
    data = [{'name': name, 'email': email, 'contact': contact}]
    try:
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['name', 'email', 'contact']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerows(data)
            return True
    except Exception as e:
        print(e)
        return False


@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    if request.method == 'POST':
        location = request.form.get('location')
        return redirect(url_for('getdetails', location=location))
    return render_template('home.html')


@app.route('/getdetails', methods=['GET', 'POST'], endpoint='getdetails')
def getdetails():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        contact = request.form.get('contact')
        success = save_to_csv(name,email,contact)
        if success:
            message = f"Hey {name}!!! your has been successfully submitted."
        else:
            message = "There was an error processing your order. Please try again."
        return render_template('result.html', success=success, message=message)
    return render_template("getdetails.html")


if __name__ == '__main__':
    app.run(debug=True, port=5505)
