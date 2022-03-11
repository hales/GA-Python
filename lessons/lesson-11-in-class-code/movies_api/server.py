from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
  { 'id': '1', 'name': 'Lord of the Rings', 'year': 2001 },
  { 'id': '2', 'name': 'The Avengers', 'year': 2012 },
  { 'id': '3', 'name': "Harry Potter and the Philosopher's Stone", 'year': 2001 }
]

@app.route('/movies/<id>')
def movies_show(id):
  for movie in movies:
    if movie['id'] == id:
      return movie

  return { 'error': 'Not Found' }, 404

@app.route('/movies')
def movies_index():
  return jsonify(movies)

@app.route('/movies', methods=['POST'])
def movies_create(): 
  new_movie = request.get_json() 
  movies.append(new_movie)
  return {'message': 'Movie created successfully'}, 201

@app.route('/movies/<id>', methods=['PATCH'])
def movies_update(id):
  updated_movie = request.get_json()
  for movie in movies:
    if movie['id'] == id:
      movie.update(updated_movie)
      return {'message': 'Movie updated successfully'}, 201

  return { 'error': 'Not Found' }, 404

@app.route('/movies/<id>', methods=['DELETE'])
def movies_delete(id):
  found_idx = None

  for i in range(len(movies)):
    if movies[i]['id'] == id:
      found_idx = i
      break
    
  if found_idx != None:
    movies.pop(found_idx)
    return {'message': 'Movie deleted successfully'}, 201

  return { 'error': 'Not Found' }, 404
  
app.run()
