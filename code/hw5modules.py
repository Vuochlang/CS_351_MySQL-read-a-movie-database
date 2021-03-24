import mysql_table as c
import sql_queries as query


# create all of your relations
def create_relations(name, password, database):
    c.create_relation(name, password, database)


# insert and parse the data from the provided CSV file into your relations
def insert_data(file_name, name, password, database):
    c.insert_data(file_name, name, password, database)


# query command for part 2
def command(question_number, name, password, database):
    query.command(question_number, name, password, database)
