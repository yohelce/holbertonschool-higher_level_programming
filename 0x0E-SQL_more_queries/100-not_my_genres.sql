-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres
WHERE name NOT IN (
	SELECT tv_genres.name FROm tv_genres
	LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
	LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
