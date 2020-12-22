SELECT name
FROM (SELECT * FROM (SELECT * FROM (SELECT * FROM movies JOIN stars ON movies.id = stars.movie_id) JOIN people on people.id = person_id)
WHERE movie_id = (SELECT id FROM movies WHERE title = 'Toy Story')) ;