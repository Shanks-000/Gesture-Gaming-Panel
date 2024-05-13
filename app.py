from flask import Flask, render_template
from flask import request
import module1
import module2

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/button1')
def button1():
    module1.function_for_button1()
    return render_template('test.html')

@app.route('/button2')
def button2():
    module2.function_for_button2()
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
