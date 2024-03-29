-- lists all sjows and all genres linked to that show, from databse
-- hbtn_0d_tvshows
-- if a show doesnt have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Result must be sorted in ASC order by the show title and genre name
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;

