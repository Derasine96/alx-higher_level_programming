-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT  tv_show_genres, COUNT(tv_show_genres) AS genre, number_of_shows
FROM tv_shows
IINER JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY number_of_shows ASC;
