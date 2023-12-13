-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
WHERE tv_genres.name = (SELECT tv_shows_genres FROM tv_genres WHERE  title = Dexter) AS genre_id
ORDER BY genre_id ASC;
