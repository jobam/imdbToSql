import csv
import sqlite3

# class SqlToCSV:

conn = sqlite3.connect('../db_output/imdb_data')
cur = conn.cursor()

print("fetching data")
cur.execute("SELECT m.idmovies, m.title, m.year, m.number, m.type, m.location, m.language,g.genre as genre,s.name as serie ,s.season as season,s.number as season_number,ai.character as character, ai.billing_position as actor_billing_position,a.lname as actor_lastname, a.fname as actor_fname, a.mname as actor_mname, a.gender as actor_gender, a.number as actor_number FROM movies m inner join movies_genres mg on mg.idmovies = m.idmovies inner join genres g on g.idgenres = mg.idgenres inner join series s on s.idmovies = m.idmovies inner join acted_in ai on ai.idmovies = m.idmovies inner join actors a on a.idactors = ai.idactors limit 100000000")

print("writing csv file")
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['idmovies', 'title', 'year','number', 'type', 'location', 'language', 'genre', 'serie', 'season', 'season_number','character', 'actor_billing_position', 'actor_lastname', 'actor_fname', 'actor_mname', 'actor_gender','actor_number'])
    while True:
        row = cur.fetchone()
        if not row: break
        writer.writerow(row)
print("done.")