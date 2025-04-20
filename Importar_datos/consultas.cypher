// 1. Top 10 artistas más populares (con más canciones en playlists)
MATCH (a:Artist)<-[:BY]-(t:Track)<-[:CONTAINS]-(p:Playlist)
RETURN a.name AS Artista, count(DISTINCT t) AS NumCanciones, count(DISTINCT p) AS NumPlaylists
ORDER BY NumPlaylists DESC
LIMIT 10;

// 2. Usuarios con más playlists
MATCH (u:User)-[:CREATED]->(p:Playlist)
RETURN u.id AS Usuario, count(p) AS NumPlaylists
ORDER BY NumPlaylists DESC
LIMIT 10;

// 3. Playlists más grandes (con más canciones)
MATCH (p:Playlist)-[:CONTAINS]->(t:Track)
RETURN p.name AS Playlist, count(t) AS NumCanciones
ORDER BY NumCanciones DESC
LIMIT 10;

// 4. Canciones que aparecen en más playlists
MATCH (t:Track)<-[:CONTAINS]-(p:Playlist)
RETURN t.name AS Cancion, count(DISTINCT p) AS NumPlaylists
ORDER BY NumPlaylists DESC
LIMIT 20;

// 5. Relaciones entre artistas (artistas que aparecen en las mismas playlists)
MATCH (a1:Artist)<-[:BY]-(t1:Track)<-[:CONTAINS]-(p:Playlist)-[:CONTAINS]->(t2:Track)-[:BY]->(a2:Artist)
WHERE a1 <> a2
RETURN a1.name AS Artista1, a2.name AS Artista2, count(DISTINCT p) AS PlaylistsComunes
ORDER BY PlaylistsComunes DESC
LIMIT 20;

// 6. Recomendación de canciones para un usuario específico
// (basada en artistas que ya tiene en sus playlists)
MATCH (u:User {id: "9cc0cfd4d7d7885102480dd99e7a90d6"})-[:CREATED]->(:Playlist)-[:CONTAINS]->(t1:Track)-[:BY]->(a:Artist)<-[:BY]-(t2:Track)
WHERE NOT (u)-[:CREATED]->(:Playlist)-[:CONTAINS]->(t2)
RETURN t2.name AS CancionRecomendada, a.name AS Artista, count(t1) AS Relevancia
ORDER BY Relevancia DESC
LIMIT 15;

// 7. Análisis de diversidad de playlists (número de artistas diferentes)
MATCH (p:Playlist)-[:CONTAINS]->(t:Track)-[:BY]->(a:Artist)
RETURN p.name AS Playlist, count(DISTINCT a) AS NumArtistas, count(t) AS NumCanciones
ORDER BY NumArtistas DESC
LIMIT 15;

// 8. Similaridad entre playlists (basada en canciones compartidas)
MATCH (p1:Playlist)-[:CONTAINS]->(t:Track)<-[:CONTAINS]-(p2:Playlist)
WHERE id(p1) < id(p2)
WITH p1, p2, count(t) AS cancionesComunes
MATCH (p1)-[:CONTAINS]->(t1:Track)
WITH p1, p2, cancionesComunes, count(t1) AS totalCancionesP1
MATCH (p2)-[:CONTAINS]->(t2:Track)
WITH p1, p2, cancionesComunes, totalCancionesP1, count(t2) AS totalCancionesP2
RETURN p1.name AS Playlist1, p2.name AS Playlist2,
       cancionesComunes,
       totalCancionesP1, totalCancionesP2,
       1.0*cancionesComunes/(totalCancionesP1 + totalCancionesP2 - cancionesComunes) AS jaccard
ORDER BY jaccard DESC
LIMIT 20;