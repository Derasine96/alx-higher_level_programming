-- A script that uses the hbtn_0d_tvshows database to list all genres of the name Comedy
SELECT title
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
