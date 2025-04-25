// Creamos índices para mejorar el rendimiento
CREATE INDEX user_id_index IF NOT EXISTS FOR (u:User) ON (u.id);
CREATE INDEX artist_name_index IF NOT EXISTS FOR (a:Artist) ON (a.name);
CREATE INDEX track_name_index IF NOT EXISTS FOR (t:Track) ON (t.name);
CREATE INDEX playlist_name_index IF NOT EXISTS FOR (p:Playlist) ON (p.name);

// Carga de datos
LOAD CSV WITH HEADERS FROM 'file:///spotify_clean.csv' AS row
// LIMIT 1000000
WITH row
WHERE row.user_id IS NOT NULL
  AND row.artistname IS NOT NULL
  AND row.trackname IS NOT NULL
  AND row.playlistname IS NOT NULL
WITH
  trim(row.user_id) AS user_id,
  trim(row.artistname) AS artistname,
  trim(row.trackname) AS trackname,
  trim(row.playlistname) AS playlistname

// Crea usuario
MERGE (u:User {id: user_id})

// Crea artista
MERGE (a:Artist {name: artistname})

// Crea cancion y su relación con artista
MERGE (t:Track {name: trackname})
MERGE (t)-[:BY]->(a)

// Crea playlist y su relacion con usuario
MERGE (p:Playlist {name: playlistname})
MERGE (u)-[:CREATED]->(p)
MERGE (p)-[:CONTAINS]->(t);