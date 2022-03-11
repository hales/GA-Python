from flask import Flask, jsonify, request

app = Flask("Artists")

# List of Dictonaries for Artists including the type of art they created, their auction record amount, and the years in which they lived.
artists = [
    {
        "name": "Warhol", 
        "art_type": "Pop Art",
        "auction_record": "$105 Million",
        "years_born_dead": "1928 - 1987"
    },
    {
        "name": "Koons", 
        "art_type": "Contemporary Art",
        "auction_record": "$91 Million",
        "years_born_dead": "1955 - "
    },
    {
        "name": "DuChamp", 
        "art_type": "Conceptual Art",
        "auction_record": "$11 Million",
        "years_born_dead": "1887 - 1968"
    },
    {
        "name": "Klein", 
        "art_type": "Post-War European Art",
        "auction_record": "$36 Million",
        "years_born_dead": "1928 - 1962"
    }
]

@app.route("/")
def artists_index():
    return jsonify(artists)

@app.route("/artist/<name>")
def artist_show(name):
    for artist in artists:
        if artist["name"] == name:
            return artist

    return {"error": "does not exists"}, 404

@app.route('/artist', methods=['POST'])
def artist_create(): 
  new_artist = request.get_json() 
  artists.append(new_artist)
  return {'message': 'Artist created successfully'}, 201

@app.route('/artist/<name>', methods=['PATCH'])
def artist_update(name):
  updated_artist = request.get_json()
  for artist in artists:
    if artist['name'] == name:
      artist.update(updated_artist)
      return {'message': 'Artist updated successfully'}, 201

  return { 'error': 'Not Found' }, 404

@app.route('/artist/<name>', methods=['DELETE'])
def artist_delete(name):
  found_idx = None

  for i in range(len(artists)):
    if artists[i]['name'] == name:
      found_idx = i
      break
    
  if found_idx != None:
    artists.pop(found_idx)
    return {'message': 'Artist deleted successfully'}, 201

  return { 'error': 'Not Found' }, 404
  
app.run()