import csv

import mysql.connector
import tablelist
import dictionary


if __name__ == "__main__":
    csv_file = "t.csv"

    try:
        mysql_database = mysql.connector.connect(user='root', password='YueLan!_2388', database='351_a5')
    except mysql.connector.Error:
        print("Something is wrong while trying to connect")
    else:
        print("Successfully connected to the Mysql")

        my_cursor = mysql_database.cursor()

        # drop tables
        for each in tablelist.drop_list:
            my_cursor.execute(each)

        # create tables
        for each in tablelist.table_list:
            my_cursor.execute(each)

        # create dictionaries
        my_dictionary = dictionary.Dictionary()
        my_dictionary.create_dictionary(csv_file)

        # Genre table
        for (key, value) in my_dictionary.genre_dictionary.items():
            sql = "INSERT INTO Genre (id, name) VALUES (%s, %s)"
            my_cursor.execute(sql, (key, value))

        # Spoken Language
        for (key, value) in my_dictionary.spoken_languages_dictionary.items():
            sql = "INSERT INTO SpokenLanguage (iso_639_1, name) VALUES (%s, %s)"
            my_cursor.execute(sql, (key, value))

        # production country
        for (key, value) in my_dictionary.production_countries_dictionary.items():
            sql = "INSERT INTO ProductionCountries (iso_3166_1, name) VALUES (%s, %s)"
            my_cursor.execute(sql, (key, value))

        # production company
        for (key, value) in my_dictionary.production_companies_dictionary.items():
            sql = "INSERT INTO ProductionCompanies (id, name) VALUES (%s, %s)"
            my_cursor.execute(sql, (key, value))

        # keywords
        for (key, value) in my_dictionary.keywords_dictionary.items():
            sql = "INSERT INTO Keywords (id, name) VALUES (%s, %s)"
            my_cursor.execute(sql, (key, value))

        # movie
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)  # read rows into a dictionary format
            for row in reader:  # read a row as {column1: value1, column2: value2,...}
                sql = "INSERT INTO Movie (budget, homepage, mId, originalLanguage, title, tagline,\
                        voteAverage, voteCount, status, releaseDate, runTime, revenue, popularity,\
                        overview, originalTitle) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                        %s, %s, %s)"
                value = []
                value += [row["budget"], row["homepage"], row["id"], row["original_language"], row["title"]]
                value += [row["tagline"], row["vote_average"], row["vote_count"], row["status"], row["release_date"]]
                value += [row["runtime"], row["revenue"], row["popularity"], row["overview"], row["original_title"]]
                my_cursor.execute(sql, tuple(value))
        csvfile.close()

        # create all join tables
        for each_key in my_dictionary.movie_dictionary.keys():
            temp_dict = my_dictionary.movie_dictionary[each_key]["production_countries"]
            for each_item in temp_dict:
                sql = "INSERT INTO FromCountry (mId, cId) VALUES (%s, %s)"
                my_cursor.execute(sql, (each_key, each_item))

            temp_dict = my_dictionary.movie_dictionary[each_key]["production_companies"]
            for each_item in temp_dict:
                sql = "INSERT INTO FromCompany (mId, cId) VALUES (%s, %s)"
                my_cursor.execute(sql, (each_key, each_item))

            temp_dict = my_dictionary.movie_dictionary[each_key]["keywords"]
            for each_item in temp_dict:
                sql = "INSERT INTO HasKeyword (mId, kId) VALUES (%s, %s)"
                my_cursor.execute(sql, (each_key, each_item))

            temp_dict = my_dictionary.movie_dictionary[each_key]["genres"]
            for each_item in temp_dict:
                sql = "INSERT INTO HasGenre (mId, gId) VALUES (%s, %s)"
                my_cursor.execute(sql, (each_key, each_item))

            temp_dict = my_dictionary.movie_dictionary[each_key]["spoken_languages"]
            for each_item in temp_dict:
                sql = "INSERT INTO HasLanguages (mId, lId) VALUES (%s, %s)"
                my_cursor.execute(sql, (each_key, each_item))

        mysql_database.commit()

        my_cursor.execute("SELECT * FROM Genre")
        print(my_cursor.fetchall())

        my_cursor.execute("SELECT * FROM SpokenLanguage")
        print(my_cursor.fetchall())

        my_cursor.execute("SELECT * FROM FromCountry")
        print(my_cursor.fetchall())

        my_cursor.execute("SELECT * FROM HasLanguages")
        print(my_cursor.fetchall())

        # disconnect mysql
        my_cursor.close()
        mysql_database.close()
        print("Successfully closed mysql connection")
