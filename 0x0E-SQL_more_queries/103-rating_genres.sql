-- lists all genres from hbtn_od_tvshows_rate by thier ratings
-- in descending order
-- g = tv_genres
-- sg = tv_show_genres
-- shrt = tv_show_ratings
SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS sg ON sg.`genre_id` = g.`id`
INNER JOIN `tv_show_ratings` AS shrt ON shrt.`show_id` = sg.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;

