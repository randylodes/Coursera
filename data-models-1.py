
# diagram of tables with relationship connections
# basic rule: don't put the same string data in twice (use a relationship instead)
# performance becomes a factor in larger data sets
# model the real world - a table for each logical grouping of things
# is the column an object or an attribute of another object
# start with what is most essential to the application

# primary key is a unique identifier for ap particular row (ex, 'id')
# this becomes the connection point for relationships across tables
# foreign_key -> primary_key
# logical kay supports lookups in that table (ex, use it in a WHERE or ORDER BY clause)

# work outward -> in when creating the tables (allows the auto keys to be generated first)
# the JOIN operation links several tables as part of a SELECT
# must tell the JOIN how to use the keys by using an ON clause
# Ex:
# SELECT Album.title, Artist.name FROM Album JOIN Artist
#    ON Album.artist_id = Artist.id
# could alternatively use a WHERE clause
# if ON clause is omitted, then the JOIN will return all possible combinations 


