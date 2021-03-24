There are several .py files:
_ dictionary.py: parse multi-values attributes into dictionaries
_ tablelist.py: contains all query commands to create and drop tables
_ sql_queries.py: contain query for part 2 to where output is in the comma delimited form
_ mysql_table.py: create relations or insert data as needed
_ hw5modules.py: module to import and use for 3 required methods

Required methods:
1. def create_relations(name, password, database)
2. def insert_data(file_name, name, password, database)
3. def command(question_number, name, password, database)

To run the code:
    Example:
        mysql_username = "root"
        mysql_password = "123456789"
        mysql_database = "hw5_db"
        csv_filename = "tmdb_5000_movies.csv"
        query_question_number = 3  # part 2 queries

    Then,
    |    import hw5modules as hw5
    |
    |    if __name__ == '__main__':
    |        # create all of your relations
    |        hw5.create_relations("root", '123456789', 'hw5_db')
    |
    |        # insert and parse the data from the provided CSV file into your relations
    |        hw5.insert_data('tmdb_5000_movies.csv', 'root', '123456789', 'hw5_db')
    |
    |        # query question 3
    |        hw5.command(3, "root", '123456789', 'hw5_db')