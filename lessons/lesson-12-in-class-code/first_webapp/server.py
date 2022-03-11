from flask import Flask, render_template

app = Flask(__name__)

@app.route('/example')
def example_view_function():
  return render_template('example.html', user_name='Joe')

app.run()
