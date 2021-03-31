import csv
import mysql.connector
import tablelist
import dictionary


class MysqlTable:

    def __init__(self, user_name, user_password, user_database):
        self.cursor = ""
        self.mysql_db = ""
        self.user = str(user_name)
        self.password = str(user_password)
        self.database = str(user_database)

    def connect(self, create_table=False, add_data=False, file_name=""):
        try:
            mysql_database = mysql.connector.connect(user=self.user,
                                                     password=self.password,
                                                     database=self.database,
                                                     charset='utf8mb4')
        except mysql.connector.Error:
            print("Something is wrong while trying to connect")
        else:
            # print("Successfully connected to the Mysql")

            my_cursor = mysql_database.cursor()
            self.mysql_db = mysql_database
            self.cursor = my_cursor

            if create_table:
                self.create_relation()
            elif add_data:
                self.insert_data(file_name)

    def create_relation(self):
        # drop tables
        for each in tablelist.drop_list:
            self.cursor.execute(each)

        # create tables
        for each in tablelist.table_list:
            self.cursor.execute(each)

        self.mysql_db.commit()

    def query(self, string):
        self.cursor.execute(string)
        output = self.cursor.fetchall()

        comma = ', '
        for each in output:
            my_list = list(each)
            print(comma.join([str(i) for i in my_list]))

    def disconnect(self):
        # disconnect mysql
        self.cursor.close()
        self.mysql_db.close()
        # print("Successfully closed mysql connection")

    def insert_data(self, file_name):

        # create dictionaries by parsing attributes with multiple values
        my_dict = dictionary.Dictionary()
        my_dict.create_dictionary(file_name)

        # insert to Genre table from dictionary
        for (key, value) in my_dict.genre_dictionary.items():
            sql = "INSERT INTO Genre (id, name) VALUES (%s, %s)"
            self.cursor.execute(sql, (key, value))

        # insert to Spoken Language from dictionary
        for (key, value) in my_dict.spoken_languages_dictionary.items():
            sql = "INSERT INTO SpokenLanguage (iso_639_1, name) VALUES (%s, %s)"
            self.cursor.execute(sql, (key, value))

        # insert to production country from dictionary
        for (key, value) in my_dict.production_countries_dictionary.items():
            sql = "INSERT INTO ProductionCountries (iso_3166_1, name) \
                    VALUES (%s, %s)"
            self.cursor.execute(sql, (key, value))

        # insert to production company from dictionary
        for (key, value) in my_dict.production_companies_dictionary.items():
            sql = "INSERT INTO ProductionCompanies (id, name) VALUES (%s, %s)"
            self.cursor.execute(sql, (key, value))

        # insert to keywords from dictionary
        for (key, value) in my_dict.keywords_dictionary.items():
            sql = "INSERT INTO Keywords (id, name) VALUES (%s, %s)"
            self.cursor.execute(sql, (key, value))

        # insert to movie by reading off from given CSV file
        try:
            csv_file = open(file_name)
        except (FileNotFoundError, FileExistsError):
            print("Error opening the CSV file")
        else:
            # read rows into a dictionary format
            reader = csv.DictReader(csv_file)

            # read a row as {column1: value1, column2: value2,...}
            for row in reader:
                sql = "INSERT INTO Movie (budget, homepage, mId, \
                        originalLanguage, title, tagline, voteAverage,\
                        voteCount, status, releaseDate, runTime, revenue, \
                        popularity, overview, originalTitle) VALUES (%s,\
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                        %s)"

                # iterate over attributes name of the Movie table
                # get value from each column and combine into a tuple
                value = []
                for attribute in tablelist.movie_attribute_list:
                    attribute_value = row[attribute]

                    # if blank, and type int or float, then set to 0
                    if attribute_value == '':
                        if attribute in tablelist.movie_int_list \
                                or tablelist.movie_float_list:
                            attribute_value = 0

                    # convert value to int or float as needed
                    if attribute in tablelist.movie_int_list:
                        attribute_value = int(attribute_value)
                    elif attribute in tablelist.movie_float_list:
                        attribute_value = float(attribute_value)

                    value += [attribute_value]

                self.cursor.execute(sql, tuple(value))
            csv_file.close()

        # create all join tables
        for each_key in my_dict.movie_dictionary.keys():
            temp = my_dict.movie_dictionary[each_key]["production_countries"]
            for each_item in temp:
                sql = "INSERT INTO FromCountry (mId, cId) VALUES (%s, %s)"
                self.cursor.execute(sql, (each_key, each_item))

            temp = my_dict.movie_dictionary[each_key]["production_companies"]
            for each_item in temp:
                sql = "INSERT INTO FromCompany (mId, cId) VALUES (%s, %s)"
                self.cursor.execute(sql, (each_key, each_item))

            temp = my_dict.movie_dictionary[each_key]["keywords"]
            for each_item in temp:
                sql = "INSERT INTO HasKeyword (mId, kId) VALUES (%s, %s)"
                self.cursor.execute(sql, (each_key, each_item))

            temp = my_dict.movie_dictionary[each_key]["genres"]
            for each_item in temp:
                sql = "INSERT INTO HasGenre (mId, gId) VALUES (%s, %s)"
                self.cursor.execute(sql, (each_key, each_item))

            temp = my_dict.movie_dictionary[each_key]["spoken_languages"]
            for each_item in temp:
                sql = "INSERT INTO HasLanguages (mId, lId) VALUES (%s, %s)"
                self.cursor.execute(sql, (each_key, each_item))

        self.mysql_db.commit()


def create_relation(user_name, user_password, user_database):
    my_sql = MysqlTable(user_name, user_password, user_database)
    my_sql.connect(create_table=True, add_data=False)
    my_sql.disconnect()


def insert_data(file, user_name, user_password, user_database):
    my_sql = MysqlTable(user_name, user_password, user_database)
    my_sql.connect(file_name=file, create_table=False, add_data=True)
    my_sql.disconnect()
