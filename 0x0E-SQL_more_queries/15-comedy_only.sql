-- lists all comedy shows in database
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_genres.name = "Comedy" ORDER BY tv_shows.title;