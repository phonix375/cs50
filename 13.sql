SELECT
	DISTINCT name
FROM
	stars
JOIN people ON people.id = stars.person_id
WHERE movie_id IN (
SELECT
	movie_id
FROM
	movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
WHERE name = 'Kevin Bacon'
) AND NOT name = 'Kevin Bacon';