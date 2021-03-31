import mysql_table as c


# MYSQL queries for part 2 where output is in the comma delimited form
def command(question_number, name, password, database):
    my_sql = c.MysqlTable(name, password, database)
    my_sql.connect()
    query_command = get_query_command(question_number)
    my_sql.query(query_command)
    my_sql.disconnect()


def get_query_command(question_number):
    if question_number == 1:
        return """SELECT AVG(budget) FROM Movie"""

    elif question_number == 2:
        return """SELECT Movie.title AS 'movie title',
                    ProductionCompanies.name AS 'production company name'
                    FROM Movie
                    INNER JOIN FromCompany
                    ON Movie.mId = FromCompany.mId
                    INNER JOIN ProductionCompanies
                    ON FromCompany.cId = ProductionCompanies.id
                    INNER JOIN FromCountry
                    ON Movie.mId = FromCountry.mId
                    INNER JOIN ProductionCountries
                    ON FromCountry.cId = ProductionCountries.iso_3166_1
                    WHERE iso_3166_1 = 'US'"""

    elif question_number == 3:
        return """SELECT title AS 'movie title', revenue
                    FROM Movie
                    ORDER BY revenue DESC
                    LIMIT 5"""

    elif question_number == 4:
        return """SELECT Movie.title, GROUP_CONCAT(Genre.name)
                    FROM Movie
                    INNER JOIN HasGenre
                    ON Movie.mId = HasGenre.mId
                    INNER JOIN Genre
                    ON HasGenre.gId = Genre.id
                    WHERE Movie.mId in (
                        SELECT Movie.mId
                        FROM Movie
                        INNER JOIN HasGenre
                        ON Movie.mId = HasGenre.mId
                        INNER JOIN Genre
                        ON HasGenre.gId = Genre.id
                        WHERE Genre.name = 'Science Fiction'
                        OR Genre.name = 'Mystery'
                        GROUP BY Movie.title
                        HAVING COUNT(*) = 2)
                    GROUP BY Movie.title"""

    elif question_number == 5:
        return """SELECT title, popularity
                    FROM Movie
                    WHERE popularity > (SELECT AVG(popularity) FROM Movie)"""
