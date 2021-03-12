-- list all genres for the show Dexter
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.show_id WHERE tv_shows.title = "DEXTER" ORDER BY tv_genres.name;