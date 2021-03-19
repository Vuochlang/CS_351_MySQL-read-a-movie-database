import csv
import json


def parse_list(string):
    for each in string.split('}, '):
        if each[0] == '[':
            each = each[1:]
        if each[-1] != ']':
            each += "}"
        else:
            each = each[:-1]
        yield each


def add_to_dict(my_dictionary, data, key, value):
    if data[key] not in my_dictionary:
        my_dictionary[data[key]] = data[value]
    return my_dictionary


def collect_store_to_dict(my_dictionary, data, key_name, value_name):
    for i in parse_list(data):
        e = json.loads(i)
        my_dictionary = add_to_dict(my_dictionary, e, key_name, value_name)


def print_dictionary(my_dictionary):
    print(str(my_dictionary.keys()), " + ", str(len(my_dictionary)))
    print("\n", my_dictionary, "\n\n")


if __name__ == "__main__":
    genre_dictionary = {}  # ('id': 'name')
    keywords_dictionary = {}  # ('id': 'name')
    production_companies_dictionary = {}  # ('name', 'id')
    production_countries_dictionary = {}  # ('iso_3166_1', 'name')
    spoken_languages_dictionary = {}  # ('iso_639_1', 'name')

    # with open('tmdb_5000_movies.csv', newline='') as csvfile:
    with open('t.csv') as csvfile:
        reader = csv.DictReader(csvfile)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            genre = row["genres"]
            keyword = row["keywords"]
            pro_company = row["production_companies"]
            pro_country = row["production_countries"]
            language = row["spoken_languages"]

            collect_store_to_dict(genre_dictionary, genre, key_name='id', value_name='name')
            collect_store_to_dict(keywords_dictionary, keyword, key_name='id', value_name='name')
            collect_store_to_dict(production_companies_dictionary, pro_company, key_name='id', value_name='name')
            collect_store_to_dict(production_countries_dictionary, pro_country, key_name='iso_3166_1', value_name='name')
            collect_store_to_dict(spoken_languages_dictionary, language, key_name='iso_639_1', value_name='name')

        print_dictionary(genre_dictionary)
        print_dictionary(keywords_dictionary)
        print_dictionary(production_companies_dictionary)
        print_dictionary(production_countries_dictionary)
        print_dictionary(spoken_languages_dictionary)

    csvfile.close()
