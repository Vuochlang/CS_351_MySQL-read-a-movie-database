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


def parse_to_store_to_dict(data, key_name, value_name):
    temp_dictionary = {}
    if data == '[]':
        return temp_dictionary
    for i in parse_list(data):
        e = json.loads(i)
        temp_dictionary = add_to_dict(temp_dictionary, e, key_name, value_name)
    return temp_dictionary


def print_dictionary(my_dictionary):
    print(str(my_dictionary.keys()), " + ", str(len(my_dictionary)))
    print("\n", my_dictionary, "\n\n")


if __name__ == "__main__":
    movie_dictionary = {}  # ('id':{}{})
    genre_dictionary = {}  # ('id': 'name')
    keywords_dictionary = {}  # ('id': 'name')
    production_companies_dictionary = {}  # ('name', 'id')
    production_countries_dictionary = {}  # ('iso_3166_1', 'name')
    spoken_languages_dictionary = {}  # ('iso_639_1', 'name')

    # with open('tmdb_5000_movies.csv', newline='') as csvfile:
    with open('tmdb_5000_movies.csv') as csvfile:
        reader = csv.DictReader(csvfile)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            movie_id = row["id"]
            movie_dictionary[movie_id] = {}

            genre = row["genres"]
            keyword = row["keywords"]
            pro_company = row["production_companies"]
            pro_country = row["production_countries"]
            language = row["spoken_languages"]

            temp_genre = parse_to_store_to_dict(genre, key_name='id', value_name='name')
            movie_dictionary[movie_id]["genres"] = list(temp_genre.keys())
            genre_dictionary.update(temp_genre)

            temp_keyword = parse_to_store_to_dict(keyword, key_name='id', value_name='name')
            movie_dictionary[movie_id]["keywords"] = list(temp_keyword.keys())
            keywords_dictionary.update(temp_keyword)

            temp_company = parse_to_store_to_dict(pro_company, key_name='id', value_name='name')
            movie_dictionary[movie_id]["production_companies"] = list(temp_company.keys())
            production_companies_dictionary.update(temp_company)

            temp_country = parse_to_store_to_dict(pro_country, key_name='iso_3166_1', value_name='name')
            movie_dictionary[movie_id]["production_countries"] = list(temp_country.keys())
            production_countries_dictionary.update(temp_country)

            temp_language = parse_to_store_to_dict(language, key_name='iso_639_1', value_name='name')
            movie_dictionary[movie_id]["spoken_languages"] = list(temp_language.keys())
            spoken_languages_dictionary.update(temp_language)

            print("Dictionary of movie id = ", movie_id)
            print_dictionary(movie_dictionary[movie_id])

        # print_dictionary(genre_dictionary)
        # print_dictionary(keywords_dictionary)
        # print_dictionary(production_companies_dictionary)
        # print_dictionary(production_countries_dictionary)
        # print_dictionary(spoken_languages_dictionary)

        # print max value of the 'key'
        # print(max(genre_dictionary))
        # print(max(spoken_languages_dictionary))
        # print(max(production_companies_dictionary))
        # print(max(production_countries_dictionary))
        # print(max(keywords_dictionary))

    csvfile.close()
