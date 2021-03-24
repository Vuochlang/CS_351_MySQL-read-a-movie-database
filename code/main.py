import hw5modules as hw5

if __name__ == '__main__':
    # create all of your relations
    hw5.create_relations('root', 'YueLan!_2388', '351_a5')

    # insert and parse the data from the provided CSV file into your relations
    hw5.insert_data('tmdb_5000_movies.csv', 'root', 'YueLan!_2388', '351_a5')

    # query
    hw5.command(3, 'root', 'YueLan!_2388', '351_a5')
