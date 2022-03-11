from flask import Flask, jsonify, request, render_template
import csv

app = Flask("Artists")

DATA_FILE = 'data.csv'
FIELDNAMES = ['name','art_type','auction_record_title','auction_record_amount','year_created','url']

artists = []

def load_data_file():
  with open(DATA_FILE) as my_file:
    my_reader = csv.DictReader(my_file)
    for row in my_reader:
      artists.append(row)

def wipe_data_file():
  my_file = open(DATA_FILE, 'w+')
  my_file.close()

def write_data_file():
  with open(DATA_FILE, 'a', newline='') as my_file:
    writer = csv.DictWriter(my_file, fieldnames=FIELDNAMES)
    writer.writeheader()
    # add back rows that are not deleted
    for artist in artists:
      writer.writerow(artist)

def find_row(name):
  # update dictionary
  for i in range(len(artists)):
    if artists[i]['name'] == name:
      return i

  return { 'error': 'Not Found' }, 404  


def error_handling(entry_to_check):
  for id in entry_to_check:
    if id == 'name' or id == 'art_type' or id == 'auction_record_title' or id == 'url':
      if isinstance(entry_to_check[id], str) == False:
        return False
    if id == 'auction_record_amount' or id == 'year_created':
      if isinstance(entry_to_check[id], int) == False or entry_to_check[id] < 0:
        return False

    return True

def append_file_row(new_artist):
  with open(DATA_FILE, 'a', newline='') as my_file:
    writer = csv.DictWriter(my_file, FIELDNAMES)
    writer.writerow(new_artist)

@app.route("/")
def artists_index():
    index = "yes"
    return render_template('index.html', artists=artists, index=index)

@app.route("/artist/<name>")
def artist_show(name):
    for artist in artists:
        if artist["name"] == name:
            return render_template('index.html', artist=artist, index="no")

    return {"error": "does not exists"}, 404

@app.route('/artist', methods=['POST'])
def artist_create(): 
  new_artist = request.get_json()

  # error handling 
  if (error_handling(new_artist)):
    artists.append(new_artist) 
    append_file_row(new_artist)
  else:
    return {'message' : 'Incorrect variable types'}, 422

  return {'message': 'Artist created successfully'}, 201

@app.route('/artist/<name>', methods=['PATCH'])
def artist_update(name):
  found_idx = find_row(name)
  updated_artist = request.get_json()

  if (error_handling(updated_artist)):
    for id in updated_artist:
      artists[found_idx][id] = updated_artist[id]
  else:
    return {'message' : 'Incorrect variable types'}, 422

  wipe_data_file()
  write_data_file()

  return {'message': 'Artist updated successfully'}, 201

@app.route('/artist/<name>', methods=['DELETE'])
def artist_delete(name):
  found_idx = find_row(name)
      
  artists.pop(found_idx)
  wipe_data_file()
  write_data_file()

  return {'message': 'Artist deleted successfully'}, 201
  
load_data_file() 
app.run()