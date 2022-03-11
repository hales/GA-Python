from flask import Flask, jsonify

app = Flask(__name__)

movies = [
  { 'id': '1', 'name': 'Lord of the Rings', 'year': 2001 },
  { 'id': '2', 'name': 'The Avengers', 'year': 2012 },
  { 'id': '3', 'name': "Harry Potter and the Philosopher's Stone", 'year': 2001 }
]

@app.route('/movies')
def movies_index():
  return jsonify(movies)

@app.route('/movies/<id>')
def movies_show(id):
  for movie in movies:
    if movie['id'] == id:
      return movie

  return { 'error': 'Not Found' }, 404

app.run()
