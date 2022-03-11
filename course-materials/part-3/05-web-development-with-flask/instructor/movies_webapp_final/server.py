import csv
from flask import Flask, render_template, request

app = Flask(__name__)

DATA_FILE = 'data.csv'
FIELDNAMES = ['id', 'name', 'year', 'summary']

movies = []

def load_data_file():
  with open(DATA_FILE) as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
      movies.append(row)

def append_data_file(new_row):
  with open(DATA_FILE, 'a', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
    writer.writerow(new_row)

def dump_data_file():
  with open(DATA_FILE, 'w', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
    writer.writeheader()
    for movie in movies:
      writer.writerow(movie)

@app.route('/movies')
def movies_index():
  return render_template('index.html', movies=movies)

@app.route('/movies/<id>')
def movies_show(id):
  for movie in movies:
    if movie['id'] == id:
      return render_template('show.html', movie=movie)

  return { 'error': 'Not Found' }, 404

@app.route('/movies', methods=['POST'])
def movies_create():
  new_movie = request.get_json()
  movies.append(new_movie)
  append_data_file(new_movie)
  return { 'message': 'Movie created successfully' }, 201

@app.route('/movies/<id>', methods=['PATCH'])
def movies_update(id):
  updated_movie = request.get_json()

  for movie in movies:
    if movie['id'] == id:
      movie.update(updated_movie)
      dump_data_file()
      return { 'message': 'Movie updated succesffully' }, 201

  return { 'error': 'Not Found' }, 404

@app.route('/movies/<id>', methods=['DELETE'])
def movies_delete(id):
  # 1 Using the provided id, find the  index of the item to delete
  found_idx = None
  
  for i in range(len(movies)):
    if movies[i]['id'] == id:
      found_idx = i
      break

  # 2 Using that index, pop off the item from the list
  if found_idx != None:
    movies.pop(found_idx)
    dump_data_file()
    return { 'message': 'Movie deleted succesffully' }, 201

  # 3 If the movie is not found, respond with a 404
  return { 'error': 'Not Found' }, 404

load_data_file()
app.run()
