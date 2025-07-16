from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('contacts.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Добавьте другие маршруты по аналогии

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)