import mysql.connector
import csv

# remove all personal info of mysql!!!!!!!!!!!
# -- mId: 459488
# -- homepage: 138
# -- title: 86
# -- tagLine: approximation
# -- voteCount: 13752
# -- releaseDate: length of MM/DD/YYYY = 10
# -- runTime: 338
# -- budget: 380000000
# -- revenue: 2787965087
# -- popularity: 875.581305
# -- overview: 1000
# -- originalTitle: 86


def connect_to_mysql(usr, my_password, my_database):
    try:
        mysql_database = mysql.connector.connect(user=usr, password=my_password, database=my_database)
    except mysql.connector.Error:
        print("Something is wrong while trying to connect")
    else:
        print("Successfully connected to the Mysql")
        return mysql_database


if __name__ == "__main__":

    # mysql_database = connect_to_mysql(usr='root', my_password='YueLan!_2388', my_database='351_a5')

    try:
        mysql_database = mysql.connector.connect(user='root', password='YueLan!_2388', database='351_a5')
    except mysql.connector.Error:
        print("Something is wrong while trying to connect")
    else:
        print("Successfully connected to the Mysql")

        my_cursor = mysql_database.cursor()
        my_cursor.execute("SHOW TABLES")
        print(my_cursor.fetchall())

        # if len(my_result) == 0:
        #     print("Empty database")
        # else:
        #     for x in my_result:
        #         print(x)

        drop_list = ["DROP TABLE IF EXISTS Movie"]
        for each in drop_list:
            my_cursor.execute(each)

        create_list = ["""
            CREATE TABLE Movie (
                mId mediumint,
                homepage varchar(150),
                originalLanguage varCHAR(2),
                title varchar(100),
                tagline varchar(200),
                voteAverage float,
                voteCount int,
                status set('Released', 'Rumored'),
                releaseDate varchar(10),
                runTime smallint,
                budget int,
                revenue int, 
                popularity float,
                overview varchar(1000),
                originalTitle varchar(100),
                primary key (mId))"""]

        create_list += ["""
                CREATE TABLE SpokenLanguage (
                    id """]

        for each in create_list:
            my_cursor.execute(each)

        add = """INSERT INTO Movie(mId, homepage, originalLanguage, title, tagline, \
                    voteAverage, voteCount, status, releaseDate, runTime, budget, revenue, \
                    popularity, overview, originalTitle) 
                VALUES (1, 'HOMEPAGE', 'EN', 'TITLE', 'TEST', 5.6, 100, 'Released', '12/12/2009', \
                342, 90000, 213, 1324134, 9.8, 'ttleoverview')"""
        my_cursor.execute(add)

        my_cursor.execute("SELECT * FROM Movie")
        print(my_cursor.fetchall())

        # disconnect mysql
        my_cursor.close()
        mysql_database.close()
        print("Successfully closed mysql connection")
